# AI authentication and failed analysis

The GitHub configuration must use `base_url`, not `api_base`. The latter was
silently ignored by the model, so the OpenAI-compatible client used its default
OpenAI endpoint with a DeepSeek key. The 2026-10-18/19 logs show authentication
errors but do not prove whether the DeepSeek key itself is valid. The configured
model name is retained; changing it cannot resolve a wrong endpoint.

Startup now makes a small completion request through the configured endpoint and
model before scraping. Missing/blank keys and whitespace are rejected locally.
401/403 diagnostics omit provider response bodies and key values. Configuration
must not contain credentials in the endpoint URL. `api_base` is rejected explicitly.

If authentication still fails after this fix, open repository Settings > Secrets
and variables > Actions and update `DEEPSEEK_API_KEY` using a valid DeepSeek API
key without quotes, spaces or newlines. Do not put it in configuration, workflow
YAML, issue comments, or logs. The workflow already maps that secret to the
matching environment variable. Verify organization/environment secret access if
applicable. GitHub does not expose secret values for inspection.

Analysis outcomes:
- Successful low scores (including zero): normal empty digest is allowed.
- Some failed items: exclude failed items, report success/failure counts and add
  an explicit incomplete-analysis warning to each digest.
- All items failed (including malformed responses): abort before saving summaries
  or notifications. CLI exits 1; the normal Actions success gate skips deployment.
- Authentication rejection: no analyzer retry; queued requests are skipped after
  the first rejection (already running concurrent requests may finish).

Run `uv sync --locked --extra dev` and `uv run pytest` for credential-free tests.
After merging, manually run **Daily Horizon Summary**. Its startup probe validates
real credentials, endpoint and model access; subsequent steps validate scraping,
analysis and publishing. This sends real API requests and can incur normal usage
costs. Do not rerun an old run to validate the fix: it uses the old commit.
Historical published posts are not rewritten by this change.
