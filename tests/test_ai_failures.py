import asyncio
import json
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import httpx
import pytest
from openai import AuthenticationError

from src.ai.analyzer import ContentAnalyzer, AnalysisFailedError
from src.ai.client import AIValidationError, OpenAIClient, validate_ai_startup
from src.models import AIConfig
from test_analyzer import _make_item


def auth_error():
    return AuthenticationError('secret-must-not-appear', response=httpx.Response(401, request=httpx.Request('POST', 'https://example.com')), body=None)


def config():
    return AIConfig(provider='openai', model='deepseek-v4-flash', api_key_env='DEEPSEEK_API_KEY', base_url='https://api.deepseek.com')


def test_github_config_routes_to_deepseek(monkeypatch):
    monkeypatch.setenv('DEEPSEEK_API_KEY', 'test-key')
    cfg = AIConfig(**json.load(open('data/config.github.json'))['ai'])
    assert str(OpenAIClient(cfg).client.base_url) == 'https://api.deepseek.com'


@pytest.mark.parametrize('key', ['', '   ', 'key\n'])
def test_invalid_key_prevents_request(monkeypatch, key):
    monkeypatch.setenv('DEEPSEEK_API_KEY', key)
    with pytest.raises(AIValidationError):
        asyncio.run(validate_ai_startup(config()))


def test_preflight_auth_is_safe(monkeypatch):
    monkeypatch.setenv('DEEPSEEK_API_KEY', 'test-key')
    client = SimpleNamespace(complete=AsyncMock(side_effect=auth_error()))
    monkeypatch.setattr('src.ai.client.create_ai_client', lambda cfg: client)
    with pytest.raises(AIValidationError, match='authentication rejected') as error:
        asyncio.run(validate_ai_startup(config()))
    assert 'secret-must-not-appear' not in str(error.value)
    assert error.value.__suppress_context__


def test_auth_not_retried_and_remaining_skipped(capsys):
    client = SimpleNamespace(complete=AsyncMock(side_effect=auth_error()))
    with pytest.raises(AnalysisFailedError, match='authentication rejected'):
        asyncio.run(ContentAnalyzer(client).analyze_batch([_make_item('1'), _make_item('2')]))
    assert client.complete.await_count == 1
    assert 'secret-must-not-appear' not in capsys.readouterr().out


@pytest.mark.parametrize('all_fail', [False, True])
def test_request_failures(monkeypatch, all_fail):
    analyzer = ContentAnalyzer(SimpleNamespace())
    async def analyze(item):
        if all_fail or item.id == '2':
            raise RuntimeError('unavailable')
        item.ai_score = 0.0
    monkeypatch.setattr(analyzer, '_analyze_item', analyze)
    items = [_make_item('1'), _make_item('2')]
    if all_fail:
        with pytest.raises(AnalysisFailedError):
            asyncio.run(analyzer.analyze_batch(items))
    else:
        assert [i.id for i in asyncio.run(analyzer.analyze_batch(items))] == ['1']
        assert items[1].ai_score is None


def test_normal_zero_score_is_success():
    client = SimpleNamespace(complete=AsyncMock(return_value='{"score": 0}'))
    assert len(asyncio.run(ContentAnalyzer(client).analyze_batch([_make_item('1')]))) == 1


@pytest.mark.parametrize('failure', ['auth', 'all', 'partial', 'zero'])
def test_orchestrator_publication(monkeypatch, tmp_path, failure):
    from src.models import Config
    from src.orchestrator import HorizonOrchestrator
    monkeypatch.chdir(tmp_path)
    cfg = Config(ai=config(), sources={}, filtering={})
    storage = Mock()
    storage.save_daily_summary.return_value = 'summary.md'
    orchestrator = HorizonOrchestrator(cfg, storage)
    monkeypatch.setattr('src.orchestrator.validate_ai_startup', AsyncMock())
    monkeypatch.setattr(orchestrator, 'fetch_all_sources', AsyncMock(return_value=[_make_item('1'), _make_item('2')]))
    monkeypatch.setattr(orchestrator, 'merge_cross_source_duplicates', lambda items: items)
    analyzer = ContentAnalyzer(SimpleNamespace())
    async def analyze(item):
        if failure == 'auth':
            raise auth_error()
        if failure == 'all' or (failure == 'partial' and item.id == '2'):
            raise RuntimeError('failure')
        item.ai_score = 0
    monkeypatch.setattr(analyzer, '_analyze_item', analyze)
    monkeypatch.setattr(orchestrator, '_analyze_content', analyzer.analyze_batch)
    if failure in {'auth', 'all'}:
        with pytest.raises(AnalysisFailedError):
            asyncio.run(orchestrator.run())
        storage.save_daily_summary.assert_not_called()
        assert not (tmp_path / 'docs').exists()
    else:
        asyncio.run(orchestrator.run())
        summary = storage.save_daily_summary.call_args.args[1]
        assert ('AI analysis incomplete' in summary) == (failure == 'partial')


def test_cli_exits_nonzero_on_ai_failure(monkeypatch):
    import src.main as main
    monkeypatch.setattr("sys.argv", ["horizon"])
    monkeypatch.setattr(main.StorageManager, "load_config", lambda self: Mock())
    monkeypatch.setattr(main.HorizonOrchestrator, "run", AsyncMock(side_effect=AnalysisFailedError("All AI requests failed")))
    with pytest.raises(SystemExit) as result:
        main.main()
    assert result.value.code == 1


def test_legacy_endpoint_typo_rejected():
    cfg = config().model_copy(update={"base_url": None})
    cfg = AIConfig(**cfg.model_dump(), api_base="https://api.deepseek.com")
    with pytest.raises(AIValidationError, match="api_base"):
        asyncio.run(validate_ai_startup(cfg))


def test_startup_probe_uses_configured_reasoning_budget(monkeypatch):
    monkeypatch.setenv('DEEPSEEK_API_KEY', 'test-key')
    client = SimpleNamespace(complete=AsyncMock(return_value='{"ok":true}'))
    monkeypatch.setattr('src.ai.client.create_ai_client', lambda cfg: client)
    cfg = config().model_copy(update={"max_tokens": 4096})
    asyncio.run(validate_ai_startup(cfg))
    assert client.complete.call_args.kwargs['max_tokens'] == 4096


@pytest.mark.parametrize('finish_reason', ['length', 'stop'])
def test_empty_completion_diagnostic_does_not_expose_reasoning(monkeypatch, finish_reason):
    monkeypatch.setenv('DEEPSEEK_API_KEY', 'test-key')
    client = OpenAIClient(config())
    response = SimpleNamespace(usage=None, choices=[SimpleNamespace(
        finish_reason=finish_reason,
        message=SimpleNamespace(content='', reasoning_content='private-reasoning'),
    )])
    monkeypatch.setattr(client, '_do_request', AsyncMock(return_value=response))
    with pytest.raises(AIValidationError) as error:
        asyncio.run(client.complete('system', 'user'))
    assert 'private-reasoning' not in str(error.value)
    assert ('max_tokens' in str(error.value)) == (finish_reason == 'length')


def test_live_fetch_rejects_historical_date(monkeypatch, tmp_path):
    from src.models import Config
    from src.orchestrator import HorizonOrchestrator
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv('HORIZON_REPORT_DATE', '2000-01-01')
    fetch = AsyncMock()
    orchestrator = HorizonOrchestrator(Config(ai=config(), sources={}, filtering={}), Mock())
    monkeypatch.setattr(orchestrator, 'fetch_all_sources', fetch)
    with pytest.raises(ValueError, match='historical'):
        asyncio.run(orchestrator.run())
    fetch.assert_not_called()


def test_raw_input_survives_analysis_failure(monkeypatch, tmp_path):
    from src.models import Config
    from src.orchestrator import HorizonOrchestrator
    monkeypatch.chdir(tmp_path)
    orchestrator = HorizonOrchestrator(Config(ai=config(), sources={}, filtering={}), Mock())
    monkeypatch.setattr('src.orchestrator.validate_ai_startup', AsyncMock())
    monkeypatch.setattr(orchestrator, 'fetch_all_sources', AsyncMock(return_value=[_make_item('1')]))
    monkeypatch.setattr(orchestrator, '_analyze_content', AsyncMock(side_effect=AnalysisFailedError('failed')))
    with pytest.raises(AnalysisFailedError):
        asyncio.run(orchestrator.run())
    archive, = (tmp_path / 'data/raw').glob('*.json')
    payload = json.loads(archive.read_text())
    assert payload['items'][0]['id'] == '1'
    assert payload['since'] < payload['fetched_at']
    assert not (tmp_path / 'docs').exists()
