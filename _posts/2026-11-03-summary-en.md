---
layout: default
title: "Horizon Summary: 2026-11-03 (EN)"
date: 2026-11-03
lang: en
---

> From 12 items, 12 important content pieces were selected

---

1. [Blog post urges readers to back up the websites they love](#item-1) ⭐️ 7.0/10
2. [Ubuntu's handling of a CVSS 9.8 kernel CVE sparks heated Hacker News debate](#item-2) ⭐️ 7.0/10
3. [Kyle Kingsbury: LLMs Make Maturity Signals Easier to Counterfeit](#item-3) ⭐️ 7.0/10
4. [Laptop-scale replication tests "good views beat next-token prediction" with human captions](#item-4) ⭐️ 7.0/10
5. [Willison Revisits Census AI Adoption Data Amid 'Super Intelligence' Order](#item-5) ⭐️ 6.0/10
6. [Simon Willison's rule: delete stale uv.lock files when Python 3.15 builds fail](#item-6) ⭐️ 5.0/10
7. [Reddit Asks What Ilya Sutskever Meant by 'The Models Just Want to Learn'](#item-7) ⭐️ 5.0/10
8. [Practitioner asks how to dedupe YOLO detections across multiple camera angles](#item-8) ⭐️ 5.0/10
9. [Reddit asks ML PhDs: PhD before or after the AI chatbot era?](#item-9) ⭐️ 4.0/10
10. [ML Practitioner Complains Optimizer Names Like SOAP, Shampoo, FOAM and Muon Break Literature Search](#item-10) ⭐️ 3.0/10
11. [r/MachineLearning Opens Monthly Self-Promotion Megathread](#item-11) ⭐️ 2.0/10
12. [Reddit user asks about NeurIPS accommodation updates for grant recipients in Sydney](#item-12) ⭐️ 2.0/10

---

<a id="item-1"></a>
## [Blog post urges readers to back up the websites they love](https://blog.mistys-internet.website/post/2026/10/29/if-you-love-a-website-back-it-up/) ⭐️ 7.0/10

A blog post titled "If you love a website, back it up" argues that people should personally capture and preserve the sites they care about before those sites vanish, and it sparked a wide-ranging Hacker News discussion about dead links, incomplete archives and digital preservation. Commenters swapped practical tools such as the ArchiveWeb browser extension and SingleFile, which saves a page as a single HTML file with its media bundled in. The discussion highlights how fragile the web has become: content that existed just a few years ago can now return a 404 or a parked domain, and the Internet Archive's Wayback Machine never crawled large portions of the web at all. As more information access shifts toward centralized platforms and AI systems, individual archiving becomes a hedge against both link rot and the quiet rewriting or removal of the historical record. Commenters noted that the Wayback Machine's coverage is uneven because crawlers are limited by crawl depth and frequency, so niche forums and small personal sites often fall outside its scope; ArchiveWeb's ability to selectively capture specific pages and page elements was praised, while SingleFile was recommended for quick one-off saves. Others pointed out that AI-assisted reconstruction of a lost site can only reorganize what survives elsewhere and cannot recover data that is genuinely gone.

hackernews · ingve · Nov 2, 13:25 · [Discussion](https://news.ycombinator.com/item?id=50336518)

**Background**: Link rot, also called link death or reference rot, is the tendency of hyperlinks to stop pointing at their original target as pages are moved, deleted, or their domains expire, producing 404 errors or unrelated content. Web archiving attempts to counter this by collecting and preserving web material in archival formats such as WARC so it can be replayed later, but researchers note that archives are inherently incomplete because of limits on crawl depth, crawl frequency and selective collection policies. Services like the Internet Archive's Wayback Machine are the best-known large-scale effort, yet they cannot cover the whole web, which is why personal capture tools matter.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Link_rot">Link rot - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Web_archiving">Web archiving - Wikipedia</a></li>
<li><a href="https://link.springer.com/article/10.1007/s00799-015-0153-3">Lost but not forgotten: finding pages on the unarchived web</a></li>

</ul>
</details>

**Discussion**: The Hacker News reaction was overwhelmingly supportive, with commenters describing the slow "bitrot" of their own bookmarks and one person lamenting that a forum they cared about went offline and had never been properly crawled by the Wayback Machine. Several participants argued that people should buy physical books and archive important sites while they still can, warning about centralized control over information, while others stressed that video hosted inside walled gardens is equally easy to censor and should be backed up too.

**Tags**: `#web-archiving`, `#digital-preservation`, `#link-rot`, `#hacker-news`, `#internet-culture`

---

<a id="item-2"></a>
## [Ubuntu's handling of a CVSS 9.8 kernel CVE sparks heated Hacker News debate](https://chalmovsky.com/posts/wtf-ubuntu) ⭐️ 7.0/10

A blog post titled "WTF Ubuntu?" criticising Canonical's triage and prioritisation of a critical Linux kernel CVE reached the front page of Hacker News, gathering roughly 1,242 points and 570 comments. The core complaint is that Ubuntu's security tracker labels the issue "Ubuntu Priority: High" rather than "Critical", meaning no out-of-schedule kernel update was pushed to users. Ubuntu LTS runs on a huge share of production servers and cloud instances, so how Canonical triages a kernel vulnerability directly determines how quickly millions of machines get patched. The thread also surfaces a broader industry tension between raw severity scores like CVSS and actual exploitation likelihood measured by EPSS, which increasingly drives real-world patch prioritisation. Commenters fact-checked the post and noted that the fixed kernels were sitting in the "-proposed" pocket for each LTS release (installable with `apt-get -t`, but not served by default), with one release having moved the new kernel into the updates/security pockets on October 28. Others pointed out that while the CVE carries a CVSS score of 9.8, its EPSS score is below 1%, and that most advisories describe a kernel crash or denial of service "under specific conditions" rather than the remote code execution claimed in Anthropic's write-up.

hackernews · chalmovsky · Nov 2, 14:52 · [Discussion](https://news.ycombinator.com/item?id=50337608)

**Background**: CVSS is the widely used 0–10 severity scale for vulnerabilities, where 9.8 is near the maximum; EPSS (Exploit Prediction Scoring System) instead estimates the probability that a vulnerability will actually be exploited in the wild within the next 30 days, and is often well under 1% even for high-CVSS bugs. Ubuntu assigns its own triage levels — Critical, High, Medium, Low — with Critical typically triggering an out-of-schedule security update outside the normal release cadence. Fixed packages in Ubuntu flow from the "-proposed" pocket (staging, opt-in) into the "-updates" and "-security" pockets that ordinary users receive automatically.

<details><summary>References</summary>
<ul>
<li><a href="https://www.first.org/epss/">Exploit Prediction Scoring System ( EPSS )</a></li>
<li><a href="https://ubuntu.com/security/cves">CVEs | Ubuntu</a></li>

</ul>
</details>

**Discussion**: Sentiment was split: some commenters defended Ubuntu by pointing to the low EPSS score and the availability of patched kernels in -proposed, while others attacked the tracker's vague, self-contradictory "Why this priority?" text that merely says "See ubuntu cvss score". A recurring counterargument was that the original post reads as outrage-bait — it never explains the vulnerability, its real-world impact, or the author's own exposure — and that this "I demand to speak to the manager" tone is unhelpful in open source.

**Tags**: `#ubuntu`, `#security`, `#linux-kernel`, `#cve`, `#distro-maintenance`

---

<a id="item-3"></a>
## [Kyle Kingsbury: LLMs Make Maturity Signals Easier to Counterfeit](https://simonwillison.net/2026/Nov/1/kyle-kingsbury/) ⭐️ 7.0/10

In a quote highlighted by Simon Willison, Kyle Kingsbury argues in Jepsen's ParticleDB 1.1.4 analysis that LLM use erodes trust in documentation, software, and the organizations behind them because maturity signals are now easier to counterfeit. He asks what maintainers can do to ensure correct software and accurate documentation, and how they can demonstrate that quality to users. This matters because engineers often rely on documentation polish, project maturity, and organizational reputation as proxies for quality, and LLMs can generate those proxies at low cost. If those signals become unreliable, maintainers may need new forms of verifiable evidence, which could affect how open-source and commercial software earn trust. The remark appears in the “LLM tradeoffs” section of Jepsen's analysis of ParticleDB, a multi-model database aimed at AI workloads; Jepsen tested versions 1.1.4 through 1.1.18.11.rc-22. The excerpt raises the trust problem but does not itself prescribe a concrete verification mechanism, leaving the question open for maintainers.

rss · Simon Willison · Nov 1, 16:49

**Background**: Kyle Kingsbury, also known as Aphyr, created Jepsen, an independent project that stress-tests distributed databases and consensus systems against their correctness and consistency claims. Jepsen analyses are widely read because they can reveal serious bugs behind marketing claims. ParticleDB is a database marketed for AI agents and AI workloads, and its Jepsen report provides the context for this quote. LLMs can generate plausible documentation, code, and project materials at low cost, which is the source of the trust concern.

<details><summary>References</summary>
<ul>
<li><a href="https://jepsen.io/analyses/particledb-1.1.4">Jepsen: ParticleDB 1.1.4</a></li>
<li><a href="https://jepsen.io/">Distributed Systems Safety Research</a></li>
<li><a href="https://particledb.ai/">ParticleDB | The database for AI agents</a></li>

</ul>
</details>

**Tags**: `#LLMs`, `#trust`, `#software-quality`, `#documentation`, `#Jepsen`

---

<a id="item-4"></a>
## [Laptop-scale replication tests "good views beat next-token prediction" with human captions](https://www.reddit.com/r/MachineLearning/comments/1xlzoze/smallscale_check_of_good_views_beat_nexttoken/) ⭐️ 7.0/10

An independent researcher reproduced the Balestriero & LeCun (2026) "good views beat next-token prediction" claim at laptop scale, using 10,000 COCO photos with 5 human-written captions each, frozen DINOv2-base image features, and a matched 11M-parameter 4-layer text encoder across three training regimes. With the same data, 3,000 steps, batch size 256 and a VICReg-style anti-collapse loss, good views (two different captions of the same photo) reached 0.320 mutual 10-NN alignment on 1,000 test photos, versus 0.192 for bad views (one caption with masked spans) and 0.148 for next-token prediction, against a chance level of 0.010. The original paper's largest run used captions produced by an image captioner, which raised the possibility that image information leaked into the text and inflated the alignment result; this check shows the ordering survives when only human captions are used, strengthening the claim's credibility. It matters for the debate over whether next-token prediction is the right objective for learning aligned, world-model-like representations, a central argument in LeCun's JEPA programme. The study is far smaller than the original (11M parameters and 8,000 training photos versus 109M and up to 72B), uses a VICReg-style variance/covariance regularizer instead of the paper's SIGReg, and requires knowing which captions describe the same photo, which human annotators could do because they saw the image. A stricter retrieval metric (R@1 with one fitted rotation) shows a much narrower gap of 0.084 vs 0.063 vs 0.057, and next-token prediction's best learning rate landed at the top of the searched range, with an extra learning-rate step added after the first search and disclosed in the repository.

reddit · r/MachineLearning · /u/Traditional_Frame763 · Nov 2, 15:08

**Background**: The Platonic Representation Hypothesis argues that models trained on different modalities and objectives tend to converge toward similar internal representations of the world, which is why a text encoder can be compared to a frozen vision encoder like DINOv2 by measuring nearest-neighbour overlap between their embeddings. DINOv2 is a self-supervised vision model whose features are widely used as a fixed reference for visual semantics, so freezing it isolates what the text encoder learns. The Balestriero & LeCun line of work studies whether objectives built on "good views" — multiple distinct descriptions of the same image — align text and image representations faster than next-token prediction, and relies on anti-collapse regularizers such as VICReg or SIGReg to stop the encoder from mapping everything to one point.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2304.07193">DINOv 2 : Learning Robust Visual Features without Supervision</a></li>
<li><a href="https://sellerbubble.github.io/platonic-representation-hypothesis-on-world-models/">Platonic Representation Hypothesis on World Models</a></li>
<li><a href="https://medium.com/@shreyanshjain05/beyond-llms-yann-lecuns-pure-pixel-world-model-just-solved-jepa-s-biggest-problem-10c1532a86a5">Yann LeCun ’s LeWorldModel: Killing JEPA's Collapse Hack | Medium</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#representation-learning`, `#reproducibility`, `#multimodal-learning`, `#self-supervised-learning`

---

<a id="item-5"></a>
## [Willison Revisits Census AI Adoption Data Amid 'Super Intelligence' Order](https://simonwillison.net/2026/Nov/2/census-bureau-super-intelligence/) ⭐️ 6.0/10

Simon Willison rebuilt the Apollo Global Management AI-adoption chart using the U.S. Census Bureau's latest Business Trends and Outlook Survey data, published October 22, 2026, and in the process discovered that the Bureau's survey question was broadened in November 2025 — from asking about "AI in producing goods or services" to "AI in any business function" — making the old and new series non-comparable. He also reported that the Bureau has run afoul of Executive Order 14434, the September 29, 2026 "Super Intelligence" order, which he calls "asinine." The episode shows how a single wording change in a widely cited government survey can invalidate a year of trend lines, which matters for anyone — analysts, economists, journalists — who quoted the earlier "AI adoption is declining at large firms" narrative. It also illustrates the growing entanglement of federal statistical agencies with AI policy directives, since the Census Bureau's datasets are a primary source for measuring the real-world spread of AI. The Bureau's biweekly survey samples 200,000 businesses out of 1.2 million and rotates its panel so each firm responds only every twelve weeks, with data released on alternating Thursdays at 10am; under the broader question, adoption for firms with 250+ employees reaches 40.7%, versus 33.5% for 100–249, 27.9% for 50–99 and about 21–23% for the smallest size bands. The chart deliberately leaves a shaded gap — spanning the 2025 government shutdown and the wait for six observations under the new wording — and applies a six-survey trailing average separately to each question, with no bridging of the break.

rss · Simon Willison · Nov 2, 13:31

**Background**: The Business Trends and Outlook Survey (BTOS) is the Census Bureau's rapid-response business survey, launched to give near-real-time readings on the U.S. economy, and it has become one of the most-cited measures of AI adoption because it asks firms directly whether they use AI. In September 2025, Apollo Global Management chief economist Torsten Slok published a chart built on BTOS numbers that appeared to show AI adoption plateauing or declining at large companies; Willison had earlier used that same chart as a test case for GPT-5's and Claude's data-analysis tools. Executive Order 14434, signed September 29, 2026 and titled "Inaugurating the Era of Super Intelligence," is the policy document Willison references, though his post does not detail its provisions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.whitehouse.gov/presidential-actions/2026/09/inaugurating-the-era-of-super-intelligence/">Inaugurating The Era Of Super Intelligence – The White House</a></li>
<li><a href="https://www.federalregister.gov/documents/2026/10/02/2026-20321/inaugurating-the-era-of-super-intelligence">Inaugurating the Era of Super Intelligence - Federal Register</a></li>
<li><a href="https://www.apolloacademy.com/ai-adoption-rate-trending-down-for-large-companies/">AI Adoption Rate Trending Down for Large... - Apollo Academy</a></li>

</ul>
</details>

**Tags**: `#AI adoption`, `#Census Bureau`, `#executive order`, `#data analysis`, `#AI policy`

---

<a id="item-6"></a>
## [Simon Willison's rule: delete stale uv.lock files when Python 3.15 builds fail](https://simonwillison.net/2026/Nov/1/delete-uv-lock-first/) ⭐️ 5.0/10

Simon Willison shared a troubleshooting rule of thumb he now relies on since moving to Python 3.15: "If in doubt, delete the uv.lock file." He describes the failure mode where a lockfile pins a dependency (in his example `watchfiles==1.1.1`) that has no Python 3.15 wheel, so uv falls back to building from source and `maturin.build_wheel` fails because PyO3's maximum supported interpreter version is 3.14; deleting the lockfile and re-running `uv run pytest` resolves it. This is a concrete, real-world manifestation of the lag between a new CPython release and the native-extension ecosystem catching up: packages built with Rust/PyO3 via maturin can only produce wheels for interpreter versions the bindings already support. For anyone adopting Python 3.15 early, it turns an opaque build error into a one-command fix. Willison notes that most of his projects are libraries, which deliberately do not commit a `uv.lock` (a library shouldn't lock versions for its downstream consumers), so the lockfiles are leftover artifacts of local `uv run` commands and are already listed in `.gitignore`. That means deleting them is safe and cheap — the rule applies to disposable local lockfiles, not to applications that intentionally commit a lockfile for reproducible builds.

rss · Simon Willison · Nov 1, 23:24

**Background**: `uv` is an extremely fast Python package and project manager written in Rust that replaces tools like pip and pip-tools; its `uv.lock` is a universal lockfile pinning exact versions of a project's dependencies and all transitive dependencies across operating systems, architectures and Python versions. Wheels are prebuilt binary packages — installing one is fast, while a source distribution must be compiled locally. For extensions written in Rust, maturin (formerly pyo3-pack) builds the wheel using PyO3 bindings, and PyO3 can only target Python interpreter versions it explicitly supports, so a brand-new Python release such as 3.15 may be rejected until PyO3 adds support.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.astral.sh/uv/concepts/projects/sync/">Locking and syncing | uv - docs.astral.sh</a></li>
<li><a href="https://pyo3.rs/main/building-and-distribution/multiple-python-versions.html">Supporting multiple Python versions - PyO3 user guide</a></li>
<li><a href="https://www.maturin.rs/">Introduction - Maturin User Guide</a></li>

</ul>
</details>

**Tags**: `#Python`, `#uv`, `#dependency-management`, `#packaging`, `#developer-tooling`

---

<a id="item-7"></a>
## [Reddit Asks What Ilya Sutskever Meant by 'The Models Just Want to Learn'](https://www.reddit.com/r/MachineLearning/comments/1xlyr77/what_did_ilya_sutskever_mean_when_he_said_the/) ⭐️ 5.0/10

A post on r/MachineLearning revisits a pre-OpenAI remark from Ilya Sutskever — "Look. The models, they just want to learn. You have to understand this." — and asks the community to interpret it, with the poster explicitly pushing back on Dario Amodei's reading that it simply means "give the model good data, enough space and sane numerical conditioning, and training will do its job." The quote is an early articulation of the intuition behind the scaling hypothesis, so how it is interpreted touches on why large models trained with simple objectives generalize at all — a core assumption behind today's foundation-model arms race that many practitioners still treat as unsettled. The poster notes the remark dates to roughly a decade ago, questions why the model — rather than the optimizer or gradient descent itself — is the thing being personified, and argues that if the meaning were purely practical, Sutskever would likely have phrased the advice more plainly; the thread is philosophical rather than a technical result, and no substantive comment discussion is available in the provided content.

reddit · r/MachineLearning · /u/XTXinverseXTY · Nov 2, 14:32

**Background**: Training dynamics refers to how a network's loss and internal representations evolve during optimization, and researchers often study the geometry of the loss 'landscape' to explain why gradient descent finds generalizing solutions despite non-convexity. Sutskever's phrase 'don't condition them badly numerically' points at practical failure modes such as poorly scaled inputs, activations or learning rates that make optimization unstable. The 'models just want to learn' framing is a deliberately Zen-like way of saying that a sufficiently large network with a good gradient signal will reduce loss on its own, which is the intuition later formalized into scaling laws and the 'bitter lesson' that general methods beat hand-engineered ones.

<details><summary>References</summary>
<ul>
<li><a href="https://www.offconvex.org/2018/11/07/optimization-beyond-landscape/">Understanding optimization in deep learning by analyzing trajectories...</a></li>
<li><a href="https://ai-blog.it/blog/optimization-landscapes-neural-networks">Optimization Landscapes and Why Neural Networks Train at All</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#AI-philosophy`, `#training-dynamics`, `#model-behavior`, `#reddit-discussion`

---

<a id="item-8"></a>
## [Practitioner asks how to dedupe YOLO detections across multiple camera angles](https://www.reddit.com/r/MachineLearning/comments/1xloo4i/how_to_handle_object_deduplication_across/) ⭐️ 5.0/10

A developer posted to r/MachineLearning asking how to deduplicate the same physical object detected by YOLO across 3–4 user-uploaded photos of one scene taken from different angles (front, side, close-up), so each unique object is counted and described only once per session. The question is specifically concerned with very small crops — roughly 20x22 pixels, saved as lightweight .webp images — which makes matching far harder than with full-resolution detections. The goal is to avoid re-running expensive downstream AI calls (such as vision-language descriptions) on objects already processed from an earlier photo, which directly affects inference cost and latency in production pipelines. Multi-view re-identification of tiny crops is a well-known hard problem, so the answer pattern is relevant to anyone building photo-based inventory, cataloging, or inspection apps on top of YOLO. At ~20x22 pixels a crop retains very little discriminative appearance information, so raw pixel comparison or generic CNN embeddings are unreliable and the object may look different under each angle and lighting condition. Because sessions are isolated, matching only needs to happen within a single user's small photo set, which rules out training a dedicated re-ID model and favors lightweight similarity heuristics such as embedding cosine distance, perceptual hashing, or class-plus-spatial-context constraints.

reddit · r/MachineLearning · /u/Expert-Ad598 · Nov 2, 05:15

**Background**: Object re-identification (Re-ID) is the task of recognizing the same physical entity across different images, frames, or camera views, and it is a long-standing challenge in surveillance and multi-camera systems where viewpoints, scale, and lighting all vary. YOLO is a family of real-time object detectors that outputs bounding boxes and class labels, which are typically cropped and passed to further models for attribute extraction. Small-object detection research shows that objects below roughly 32x32 pixels lose discriminative features during deep network processing, which is why tiny crops are especially difficult to match; common mitigations include tiling/sliding-window inference and embedding-based similarity search in a vector database.

<details><summary>References</summary>
<ul>
<li><a href="https://zilliz.com/blog/milvus-and-surveillance-how-vector-dbs-transform-multi-camera-tracking">Vector Databases: Transforming Multi- Camera Tracking... - Zilliz blog</a></li>
<li><a href="https://inass.org/wp-content/uploads/2025/04/2025083109-2.pdf">Semantic-Aware Image Deduplication : Leveraging Object ...</a></li>
<li><a href="https://towardsdatascience.com/increasing-performance-when-detecting-small-objects-using-data-crops-d9b8daabd18/">Increasing Performance When Detecting Small Objects Using ... Introducing SAHI and Sliding Window Functions for Small ... Enhanced lightweight detection of small and tiny objects in ... Tiny object detection: An in-depth survey of techniques ... What Is Object Re-Identification (Re-ID)? - roboflow.com</a></li>

</ul>
</details>

**Tags**: `#object-detection`, `#YOLO`, `#re-identification`, `#deduplication`, `#computer-vision`

---

<a id="item-9"></a>
## [Reddit asks ML PhDs: PhD before or after the AI chatbot era?](https://www.reddit.com/r/MachineLearning/comments/1xlt9wm/ml_phds_would_you_rather_have_done_your_phd/) ⭐️ 4.0/10

A user on r/MachineLearning posted a discussion prompt asking ML PhD students and graduates whether, given the choice, they would rather have completed their PhD before ChatGPT and other AI chatbots became widely available or in today's AI-saturated research era. The thread invites personal reflections on how timing relative to the chatbot boom shaped research topics, tooling, and career prospects. The question touches a real fault line in ML research culture: pre-chatbot PhDs were trained in an era of smaller models and scarcer compute, while current students face both powerful AI assistants and intense competition in a crowded field. The answers could inform prospective students weighing when and how to pursue graduate study in machine learning. The original post is a short, open-ended question with no data, poll, or methodology behind it, so responses are anecdotal and shaped by self-selection among commenters. It is tagged as a discussion topic on r/MachineLearning, where such career-oriented prompts typically draw opinion rather than technical evidence.

reddit · r/MachineLearning · /u/Hope999991 · Nov 2, 10:04

**Background**: ChatGPT's late-2022 release popularized large language models and made AI assistants a routine part of research and coding workflows. For ML PhD students, this shifted what skills matter (prompting, evaluation, tool use) and raised questions about which research directions remain novel when models can already generate code and literature summaries. A PhD typically takes four to six years, so a cohort that started before 2022 has experienced a markedly different research environment from one starting today.

**Tags**: `#ML PhD`, `#AI chatbots`, `#career advice`, `#research culture`, `#community discussion`

---

<a id="item-10"></a>
## [ML Practitioner Complains Optimizer Names Like SOAP, Shampoo, FOAM and Muon Break Literature Search](https://www.reddit.com/r/MachineLearning/comments/1xl7yv0/why_do_all_nn_optimizers_have_weird_names_d/) ⭐️ 3.0/10

A Reddit user on r/MachineLearning complained that neural network optimizer names such as SOAP, Shampoo, FOAM and Muon return mostly irrelevant results in literature searches because the names are not unique. The poster noted that Adam would suffer the same problem were it not already so famous, and said the issue has caused considerable wasted time when trying to find relevant papers. The complaint highlights a practical pain point in a fast-moving research area: as new optimizers proliferate, ambiguous names make it harder for practitioners and newcomers to find the right papers, code and discussions. It touches on a broader question of how the ML community should name algorithms so that search, documentation and tooling remain usable. The specific offenders named are SOAP (which builds on Shampoo by combining it with Adam-style preconditioning), Shampoo (a second-order preconditioned stochastic tensor optimization method), FOAM, and Muon, which collides with the physics term for a subatomic particle. The author concedes that Muon is 'a bit better' but still suffers from the same search-noise problem.

reddit · r/MachineLearning · /u/Future_Pace_5290 · Nov 1, 16:51

**Background**: Optimizers are the algorithms that update a neural network's weights during training, and Adam (with AdamW) has been the default choice for years. Researchers have long explored higher-order or preconditioned methods such as Shampoo, which uses matrix preconditioners to adapt updates per parameter tensor, and recently Muon, which applies matrix-aware, spectral-norm-based updates to hidden-layer parameters; SOAP further combines Shampoo's preconditioning with Adam's second-moment estimates. Because these methods are frequently given short, evocative names, they often collide with common words and with terms from other fields, complicating keyword-based literature search.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2409.11321">SOAP: Improving and Stabilizing Shampoo using Adam SOAP: Improving and Stabilizing Shampoo using Adam GitHub - nikhilvyas/SOAP SOAP: Improving and Stabilizing Shampoo using Adam SOAP: IMPROVING AND STABILIZING SHAMPOO USING ADAM GitHub - NoteDance/SOAP: TensorFlow implementation for "SOAP ... OPT2024: 16th Annual Workshop on Optimization for Machine ...</a></li>
<li><a href="https://kellerjordan.github.io/posts/muon/">Muon : An optimizer for hidden layers in neural networks</a></li>
<li><a href="https://proceedings.mlr.press/v80/gupta18a/gupta18a.pdf">Shampoo : Preconditioned Stochastic Tensor Optimization</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#optimizers`, `#naming`, `#searchability`, `#community discussion`

---

<a id="item-11"></a>
## [r/MachineLearning Opens Monthly Self-Promotion Megathread](https://www.reddit.com/r/MachineLearning/comments/1xlmffv/d_selfpromotion_thread/) ⭐️ 2.0/10

The AutoModerator on r/MachineLearning posted a recurring self-promotion megathread where users can share personal projects, startups, products, collaboration requests, and blogs. The thread will remain active until the next one is posted, and users are asked to disclose payment and pricing details for any products or services. By funneling promotional posts into a single thread, the moderators aim to keep the main subreddit feed focused on technical discussion and questions. For ML practitioners building side projects or startups, this becomes the sanctioned channel for reaching a large technical audience without risking a ban for spam. The thread explicitly bans link shorteners, link aggregator sites, and auto-subscribe links, and warns that any abuse of trust will result in bans. The post also notes it is framed as an experiment that will be cancelled if the community dislikes it, and encourages users to redirect new promotional posts into this thread.

reddit · r/MachineLearning · /u/AutoModerator · Nov 2, 03:15

**Background**: Subreddits like r/MachineLearning rely on volunteer moderators and bots such as AutoModerator to enforce posting rules. Self-promotion is a common source of friction in technical communities, since it can flood the main feed with low-value marketing, so many subreddits create periodic megathreads as a compromise. These meta threads contain no technical content themselves and serve purely as a housekeeping mechanism.

**Tags**: `#reddit`, `#machine-learning`, `#community-meta`, `#self-promotion`, `#moderation`

---

<a id="item-12"></a>
## [Reddit user asks about NeurIPS accommodation updates for grant recipients in Sydney](https://www.reddit.com/r/MachineLearning/comments/1xlzumq/any_update_with_the_accomodation_from_neurips_d/) ⭐️ 2.0/10

A Reddit user on r/MachineLearning asked whether NeurIPS organizers have issued any accommodation updates for attendees who received financial grants, specifically for the Sydney edition of the conference. The post is a short query with no answers or official information included. Travel and lodging costs are the biggest practical barrier for grant-funded attendees, so clarity on accommodation directly affects whether recipients can actually attend. For a conference held in a relatively expensive and far-flung city like Sydney, delays in housing information can force attendees to book expensive last-minute flights and hotels. The question comes from a financial grant recipient and remains unanswered in the provided content, with no official statement from NeurIPS organizers cited. It also underscores the coordination gap between grant award notifications and the logistical details that recipients need in order to commit to travel.

reddit · r/MachineLearning · /u/Fantastic-Nerve-4056 · Nov 2, 15:14

**Background**: NeurIPS (Conference on Neural Information Processing Systems) is one of the largest annual AI/ML research conferences, drawing tens of thousands of attendees. Like many major academic conferences, it runs a financial grant or travel award program that helps students and researchers with limited funding cover registration, travel, and lodging. NeurIPS rotates its host city each year and has announced Sydney as a future venue, which means many grant recipients will face long-haul international travel and unfamiliar, higher-cost accommodation markets.

**Tags**: `#NeurIPS`, `#conference logistics`, `#accommodation`, `#financial grants`, `#machine learning community`

---