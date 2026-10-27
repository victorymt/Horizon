---
layout: default
title: "Horizon Summary: 2026-10-28 (EN)"
date: 2026-10-28
lang: en
---

> From 19 items, 19 important content pieces were selected

---

1. [CPython's experimental JIT compiler is being removed](#item-1) ⭐️ 8.0/10
2. [Wikipedia's WikiProject AI Cleanup Takes On AI-Generated Text](#item-2) ⭐️ 7.0/10
3. [US Government Withholds Secret FISA Court Ruling on Section 702 Spying](#item-3) ⭐️ 7.0/10
4. [Anthropic accused of training Claude on pirated Stanford professors' books](#item-4) ⭐️ 7.0/10
5. [When AI agents write the code, what must engineers still know?](#item-5) ⭐️ 7.0/10
6. [OpenAI Releases GPT-6.1 Terra, a Mid-Tier Model Focused on Visual Reasoning and Computer Use](#item-6) ⭐️ 7.0/10
7. [Papers with Code Revived as Apache 2.0 Open-Source Project Under Hugging Face](#item-7) ⭐️ 7.0/10
8. [Simon Willison evaluates webframe, a Go tool that runs web pages like programs](#item-8) ⭐️ 6.0/10
9. [GPU Kernel-Dev Setup Notes: CUDA 13 Drops Maxwell, Pascal and Volta](#item-9) ⭐️ 6.0/10
10. [Apple's New M6-Powered iMac Sparks Debate Over Value and Local AI](#item-10) ⭐️ 5.0/10
11. [ChatGPT Tells Tech-Support Users to Contact 404 Media](#item-11) ⭐️ 5.0/10
12. [Why do RL environment startups sell to labs instead of training their own models?](#item-12) ⭐️ 5.0/10
13. [Master's student asks MLSys how to handle negative real-robot results](#item-13) ⭐️ 5.0/10
14. [Developer releases ApexW, a memory-saving PyTorch optimizer for large GPU workloads](#item-14) ⭐️ 5.0/10
15. [Independent Researcher's KS3 Spline Regressor Outpaces MLP on 4D Mandelbulb Fit](#item-15) ⭐️ 5.0/10
16. [uv 0.13.6 adds new CPython builds, memory-use cuts, and NVIDIA GPU wheel detection preview](#item-16) ⭐️ 3.0/10
17. [ML PhD student asks how to do 'method research' without PI guidance](#item-17) ⭐️ 3.0/10
18. [Reddit user seeks non-EMA teacher designs for stable self-distillation](#item-18) ⭐️ 3.0/10
19. [Empty GitHub Event: Torvalds Pushed Zero Commits to Linux](#item-19) ⭐️ 1.0/10

---

<a id="item-1"></a>
## [CPython's experimental JIT compiler is being removed](https://lwn.net/SubscriberLink/1102102/0c00e4d550f25f8c/) ⭐️ 8.0/10

CPython's experimental just-in-time compiler — the copy-and-patch JIT merged in Python 3.13 under PEP 744 — is being removed from the main branch. The reversal follows the stalled effort to promote it to a supported feature via PEP 836 ("JIT Go Brrr: The Path to a Supported JIT Compiler for CPython"), after the Steering Council asked for a new PEP. This is a significant reversal for Python's performance roadmap: the JIT was one of the flagship runtime projects of the last few years, and part of its stated hope was to offset the overhead introduced by free-threading (PEP 703). Its removal shifts the burden of Python performance work back onto third-party tools and extensions rather than the core interpreter. The JIT was always off by default, required a compatible LLVM toolchain to build, and delivered only modest speedups on most workloads; along the way it accumulated optimizations such as automatic refcount-operation removal and new type-based specializations. Notably, the project had only recently picked up momentum before the Steering Council requested a new PEP and the decision to remove it was taken.

hackernews · f311a · Oct 27, 11:17 · [Discussion](https://news.ycombinator.com/item?id=50257419)

**Background**: CPython is the reference implementation of Python: it compiles source code to bytecode and then interprets that bytecode instruction by instruction. A JIT (just-in-time compiler) instead translates frequently executed bytecode into native machine code while the program runs; CPython 3.13 introduced one as an experimental, opt-in feature described in PEP 744. The implementation uses a "copy-and-patch" design, stitching together precompiled machine-code templates rather than running a full optimizing compiler at runtime, which makes it comparatively cheap to build and maintain. Separately, PEP 703's free-threading work removes the global interpreter lock so threads can run Python code in parallel, at the cost of extra per-object synchronization overhead.

<details><summary>References</summary>
<ul>
<li><a href="https://peps.python.org/pep-0744/">PEP 744 - JIT Compilation | peps.python.org</a></li>
<li><a href="https://peps.python.org/pep-0836/">PEP 836 - JIT Go Brrr: The Path to a Supported JIT Compiler for CPython</a></li>
<li><a href="https://github.com/python/cpython/blob/main/Tools/jit/README.md">cpython/Tools/jit/README.md at main · python/cpython</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were largely disappointed but split on the merits: some lamented the loss of a technically exciting project and of a potential counterweight to free-threading overhead, while others called the decision reasonable given existing options like Cython, Numba, PyPy and C extensions. One popular suggestion was a decorator that lets developers write inline Cython and compile it eagerly, effectively letting users opt into a JIT, and another thread asked why so many Python JIT efforts have failed while Ruby and JavaScript have long had working JITs, pointing to funding and incentives as a likely factor.

**Tags**: `#Python`, `#JIT`, `#CPython`, `#performance`, `#language-design`

---

<a id="item-2"></a>
## [Wikipedia's WikiProject AI Cleanup Takes On AI-Generated Text](https://spectrum.ieee.org/wikipedia-wikiproject-ai-writing-cleanup) ⭐️ 7.0/10

IEEE Spectrum reports on Wikipedia's WikiProject AI Cleanup, a volunteer collaboration dedicated to identifying and removing AI-generated text from articles, and on how the encyclopedia's stance is shifting toward also using AI as a cleanup tool. The story drew strong engagement on Hacker News (384 points, 175 comments), where editors shared first-hand experiences with low-quality AI edits. Wikipedia is one of the most heavily consulted knowledge sources on the web, so a flood of plausible-sounding but fabricated AI text directly threatens the reliability people depend on. The story also illustrates a broader tension across platforms: the same generative models that pollute content are increasingly being deployed to detect and clean it up. According to the project's own guide, AI cleanup is typically coordinated at the AI noticeboard (AINB) but carried out across the whole wiki, and the guidance is explicitly framed as advice rather than binding policy. Even the core term is unsettled: an academic article published in January 2026 noted that "AI slop" has "so far resisted formal definition."

hackernews · rbanffy · Oct 27, 11:08 · [Discussion](https://news.ycombinator.com/item?id=50257326)

**Background**: Wikipedia is written and maintained almost entirely by unpaid volunteers, and topical "WikiProjects" are informal groups of editors who coordinate work on a shared area of interest. "AI slop" refers to low-quality machine-generated text or images produced in bulk, typically generic, lacking original information, and aimed at volume rather than accuracy. As generative models became widely available, patrollers began encountering edits with telltale signs — broken formatting, fabricated citations, links attached to the wrong keywords — which led to the creation of a dedicated cleanup project.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_slop">AI slop - Wikipedia</a></li>
<li><a href="https://www.stealthgpt.ai/blog/how-to-fix-ai-slop">What Is AI Slop ? The Complete Guide to Spotting, Avoiding, and...</a></li>

</ul>
</details>

**Discussion**: Commenters broadly welcomed the cleanup effort, but the discussion was far from one-sided: one user described fixing broken, fabricated AI text only to be immediately reverted by Wikipedia's own AI bot and giving up, while another traced a low-value AI-heavy edit to a participant in one of Wikipedia's school outreach programs. Several praised Wikipedia for a nuanced position — protecting human input while admitting AI still has a place — quoting its line that "Yesterday, AI was something to clean up. Today, it's a tool to help us with the cleanup. Tomorrow, it will be the air we breathe."

**Tags**: `#AI-generated content`, `#Wikipedia`, `#content moderation`, `#community discussion`, `#knowledge platforms`

---

<a id="item-3"></a>
## [US Government Withholds Secret FISA Court Ruling on Section 702 Spying](https://www.wired.com/story/the-us-government-is-hiding-a-secret-court-ruling-about-how-it-spies-on-americans/) ⭐️ 7.0/10

A Wired report reveals that the US government is keeping a secret Foreign Intelligence Surveillance Court ruling under Section 702 hidden from the public, even as lawmakers debate the surveillance authority. Senator Ron Wyden has separately warned that multiple administrations have relied on a classified interpretation of Section 702 and refused to declassify it, saying Americans will be "stunned" when it eventually becomes public. The news matters because Section 702 is the legal backbone for much of the US intelligence community's warrantless collection of foreign communications, and incidental collection sweeps in Americans' messages without a warrant. A secret court ruling that shapes how that data is queried or shared means the public and even many legislators may be debating the authority without knowing its actual scope, weakening democratic oversight of surveillance. Section 702 authority is granted through annual certifications approved by the Foreign Intelligence Surveillance Court (FISC), a court established by the 1978 FISA law, and it is officially targeted only at non-US persons abroad. The gap at issue is "incidental collection": communications between a foreign target and a US person are captured and can be searched, which critics describe as a domestic backdoor, while the government argues collection is targeted rather than accidental.

hackernews · helterskelter2 · Oct 27, 14:06 · [Discussion](https://news.ycombinator.com/item?id=50259604)

**Background**: The Foreign Intelligence Surveillance Act of 1978 created a specialized court, the FISC, to review government requests for surveillance warrants against foreign spies operating inside the United States; its proceedings are secret and largely ex parte. In 2008 Congress added Section 702 via the FISA Amendments Act, allowing the intelligence community to collect foreign intelligence on national security threats without individual warrants, subject to annual certifications. Because most internet traffic passes through the US, this collection inevitably captures communications involving Americans, a phenomenon the intelligence community calls "incidental collection."

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_States_Foreign_Intelligence_Surveillance_Court">United States Foreign Intelligence Surveillance Court - Wikipedia</a></li>
<li><a href="https://www.eff.org/pages/Incidental-collection">‘ Incidental ,’ Not Accidental, Collection | Electronic Frontier Foundation</a></li>
<li><a href="https://www.intelligence.gov/foreign-intelligence-surveillance-act/incidental-collection-in-a-targeted-intelligence-program">Incidental Collection in a Targeted Intelligence Program</a></li>

</ul>
</details>

**Discussion**: Commenters were broadly critical: many argued secret courts are incompatible with democracy and should be abolished, and several noted that surveillance of Americans is a rare bipartisan agreement. Others were skeptical that anything has changed since the Snowden and Lavabit revelations, arguing that backdoors in hardware, software, and network infrastructure are well known and that the public has largely given up challenging them.

**Tags**: `#surveillance`, `#privacy`, `#section-702`, `#civil-liberties`, `#security`

---

<a id="item-4"></a>
## [Anthropic accused of training Claude on pirated Stanford professors' books](https://stanforddaily.com/2026/10/27/professors-books-pirated-to-train-claude/) ⭐️ 7.0/10

The Stanford Daily reported that Anthropic pirated the works of more than 10 Stanford professors in order to train its Claude models, based on interviews and email statements from the affected faculty. The article focuses on the professors' push for a licensing model rather than on any court finding, and it does not allege that the training itself was ruled illegal. The story lands amid a wave of author lawsuits and settlements over AI training data, and it puts a prestigious university's own faculty at the center of a debate their institution is also helping to shape through AI research. How such disputes resolve will determine whether AI labs must license books at scale, which directly affects authors, publishers, and the cost structure of future model training. Much of the discussion hinges on what economists call "transaction costs": as Stanford's Paul Goldstein argued, millions of individual copyrighted works may be copied in a single training run, making per-work licensing practically impossible. Commentators also note the scale is small next to datasets such as Books3, which bundled roughly 191,000 pirated books, and that this follows Anthropic's reported $1.5 billion settlement with authors.

hackernews · car · Oct 27, 15:28 · [Discussion](https://news.ycombinator.com/item?id=50260814)

**Background**: Large language models are typically trained on enormous text corpora assembled from the web and from book collections, and some of those collections were built from pirate sources. Books3, a set of about 191,000 books scraped from shadow libraries, was included in The Pile, an 825 GiB open-source dataset released by EleutherAI in 2020 and widely used for LLM training. Shadow libraries such as Library Genesis make paywalled scholarly articles and books freely downloadable, and their use in AI training has become a central front in copyright litigation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theatlantic.com/technology/archive/2023/09/books3-database-generative-ai-training-copyright-infringement/675363/">These 183,000 Books Are Fueling the Biggest Fight in ... Authors, here is a quick way to check out if your books were ... You Just Found Out Your Book Was Used to Train AI. Now What? Meta Allegedly Used Books3, a Dataset of… – AI Incident 996</a></li>
<li><a href="https://en.wikipedia.org/wiki/The_Pile_(dataset)">The Pile ( dataset ) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Library_Genesis">Library Genesis - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters (307 points, 169 comments) focused less on the allegation than on enforcement disparities, invoking the Aaron Swartz/JSTOR case to argue that individuals face criminal charges while companies treat similar conduct as a civil settlement. Others pushed back on framing the copying as "slave labor," questioned the headline's accuracy, and debated whether high transaction costs can justify unlicensed use at all.

**Tags**: `#AI copyright`, `#Anthropic`, `#training data`, `#intellectual property`, `#AI ethics`

---

<a id="item-5"></a>
## [When AI agents write the code, what must engineers still know?](https://blog.adrq.dev/here-be-monsters-what-do-you-still-need-to-know-when-agents-do-the-work) ⭐️ 7.0/10

A blog post on blog.adrq.dev titled "Here be monsters: What do you still need to know when agents do the work?" argues that as AI agents take over more code writing, engineers must retain system-level understanding, testing rigor, and awareness of product risk. The post sparked a Hacker News discussion of roughly 53 comments and 120 points, where practitioners shared concrete practices they use to stay in control of agent-written code. Code generation is increasingly delegated to AI agents, so the bottleneck for engineering teams is shifting from writing code to reviewing, verifying, and understanding it. The discussion offers a practical playbook for that transition, which affects how teams are staffed, how deliverables are defined, and what skills are worth hiring for. Commenters recommend making sequence diagrams an explicit deliverable, probing agents about time and space complexity and cache locality, and running black-box tests whose expected behavior is written down as documentation. One recurring caveat is that the real failure mode is product failure — angry users, security incidents, downtime — not developer discomfort, so review effort should be weighted accordingly.

hackernews · adrq · Oct 27, 13:23 · [Discussion](https://news.ycombinator.com/item?id=50258868)

**Background**: AI coding agents are tools that can autonomously write, edit, and run code across a repository with limited human intervention, rather than just autocompleting a single line. Because a reviewer may never have written the generated code, the discussion centers on "boxes and lines" understanding — knowing the components of a system and how they interact, rather than knowing every implementation detail. The title references the old mapmaking phrase "here be monsters," used to mark unexplored and risky territory.

**Discussion**: Commenters largely agreed that system-level understanding is the durable skill: mrothroc compared it to managing a team where more code is written than you could personally grasp, and described encouraging sequence diagrams as a deliverable. trjordan pushed back on framing the problem as developer discomfort, arguing that product failure is what actually matters, while lordnacho described building large testing harnesses that check complexity classes and cache locality. LewisOrton offered a dissenting note, questioning whether humans really hold capabilities that AI will not soon acquire.

**Tags**: `#AI agents`, `#software engineering`, `#developer productivity`, `#code review`, `#testing`

---

<a id="item-6"></a>
## [OpenAI Releases GPT-6.1 Terra, a Mid-Tier Model Focused on Visual Reasoning and Computer Use](https://simonwillison.net/2026/Oct/26/gpt-61-terra/) ⭐️ 7.0/10

OpenAI released GPT-6.1 Terra, which it describes as a fast, efficient model that combines detailed visual reasoning and precise computer use with clearer, more natural writing, calling it a significant step up from GPT-5.6 Terra. It is priced at $1 per million input tokens and $5 per million output tokens — roughly half the price of GPT-5.6 Terra and GPT-6.1 Sol, and about 10x the price of GPT-6 Luna. Terra occupies the same middle tier as Anthropic's Sonnet, which makes it a practical but ambiguous choice for developers who must decide when a cheaper model is good enough. Because computer-use agents often run long, repetitive automation loops, a model tuned for fast, inexpensive GUI interaction could meaningfully lower the cost of agentic workflows. Simon Willison notes that Terra's mid-tier slot — neither the cheapest nor the most expensive — makes it harder to know when to reach for it, and his "max" reasoning-level pelican test cost 11.3161 cents and took 4 minutes and 11 seconds. OpenAI's Ted Sanders said Terra is better than Astra and Sol at technical communication, roughly similar on vision and computer use but much faster, and somewhat worse at most other tasks.

rss · Simon Willison · Oct 26, 23:53

**Background**: Computer use refers to an AI model's ability to operate a graphical user interface the way a person would — reading the screen, clicking buttons, typing into fields and navigating menus — by combining vision with reasoning. Visual reasoning describes a multimodal model's capacity to interpret and reason over images such as charts, diagrams and technical drawings rather than just text. OpenAI now ships a tiered family (Luna, Terra, Sol, Astra), and Terra is the mid-range option, much as Sonnet is the balanced workhorse tier in Anthropic's Claude lineup. Prices are quoted per million tokens, so a cheaper tier matters most for long, repeated automated tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use">Automate web and desktop apps with computer use</a></li>
<li><a href="https://www.anthropic.com/claude/sonnet">Claude Sonnet \ Anthropic</a></li>
<li><a href="https://www.nature.com/articles/s42256-024-00963-y">Visual cognition in multimodal large language models - Nature</a></li>

</ul>
</details>

**Discussion**: In the Hacker News thread linked from the post, OpenAI's Ted Sanders framed Terra as a pragmatic midrange API option — cheaper than Sol but far smarter than Luna for vision, computer use and communication — while conceding it is not a "bombshell" release for existing subscribers. Willison's commentary echoes that read, treating the release as an incremental but useful update rather than a major capability jump.

**Tags**: `#OpenAI`, `#GPT-6.1 Terra`, `#LLM releases`, `#computer use`, `#visual reasoning`

---

<a id="item-7"></a>
## [Papers with Code Revived as Apache 2.0 Open-Source Project Under Hugging Face](https://www.reddit.com/r/MachineLearning/comments/1xgoadu/papers_with_code_is_now_opensource_p/) ⭐️ 7.0/10

A community-driven revival of Papers with Code has been released as an open-source project under the Apache 2.0 license, hosted in the Hugging Face GitHub organization at github.com/huggingface/paperswithcode. The site tracks trending AI research, benchmarks and state-of-the-art (SOTA) results, and exposes both a public API and an accompanying MCP server, with a Python FastAPI backend and a React frontend running on a Hetzner VPS. The original Papers with Code was a widely used reference for benchmark leaderboards and paper-to-code links, and its shutdown by Meta left a real gap for researchers comparing model results. Because the revival is open source and openly hosted under Hugging Face, the community can now contribute features directly instead of depending on a single closed platform that could disappear again. The author says the site was built over the past couple of months with AI coding assistants Claude and Codex, and the whole stack lives in a single monorepo on the same Hetzner VPS that serves the app. The frontend mostly calls various API endpoints to visualize papers, and the public API plus MCP server mean AI agents and external tools can query paper, benchmark and SOTA data programmatically.

reddit · r/MachineLearning · /u/NielsRogge · Oct 27, 09:54

**Background**: Papers with Code was a popular site that linked machine-learning papers to their official code implementations and maintained leaderboards of state-of-the-art (SOTA) results — the best reported scores on standard benchmarks such as ImageNet, SQuAD or GLUE. Meta acquired it and later shut it down, prompting various replacement efforts. MCP (Model Context Protocol) is an open standard that lets AI applications like Claude, ChatGPT or Cursor connect to external tools and data through MCP servers, so shipping one here lets coding agents pull benchmark data directly.

<details><summary>References</summary>
<ul>
<li><a href="https://www.coursera.org/articles/papers-with-code">What Happened to Papers With Code + What to Use Instead</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )?</a></li>
<li><a href="https://www.codesota.com/guides/enthusiast/sota-tracker">SOTA Tracker Guide | Track State-of-the-Art ML Models | CodeSOTA</a></li>

</ul>
</details>

**Tags**: `#papers-with-code`, `#open-source`, `#machine-learning`, `#benchmarks`, `#research-tools`

---

<a id="item-8"></a>
## [Simon Willison evaluates webframe, a Go tool that runs web pages like programs](https://simonwillison.net/2026/Oct/26/webframe-evaluation/) ⭐️ 6.0/10

Simon Willison published a research report evaluating webframe, a small Go project by Jeff Lindsay that takes a URL or local file, executes it inside a hidden headless system webview, and pipes console.log() output to stdout and exceptions to stderr. For the evaluation he had Claude Opus 5.5 run the tool through its paces, build exploratory prototypes, and assess it both as a web scraper following the patterns of his own shot-scraper javascript command and as a potential sandboxing tool. The write-up highlights a much lighter alternative to Playwright-based scraping: webframe reuses the browser engine already installed on the machine instead of bundling one, which keeps the binary small and the dependency surface narrow. That makes it interesting to developers who want scriptable page execution or lightweight isolation without pulling in a full automation stack. webframe is built on the glaze library, which exposes the system webview — WKWebView on macOS, WebKitGTK on Linux, and WebView2 on Windows — so nothing is bundled but the target machine must actually have that webview available, with WebKitGTK being a separate package on Linux. Willison frames it as a much smaller counterpart to his shot-scraper javascript command because it does not depend on Playwright, though the published note itself is short and partially truncated.

rss · Simon Willison · Oct 26, 16:15

**Background**: A headless browser lets software load and render web pages without a visible window, which is the basis of most modern web scraping and page-automation tooling. Playwright is a popular framework that bundles its own browser builds, giving consistency at the cost of large downloads; shot-scraper is Simon Willison's command-line tool that uses Playwright for screenshots and for running JavaScript against a page via its javascript subcommand. glaze is a CGo-free Go toolkit that instead drives the WebView already present in the operating system, and webframe layers the "run a page like a program" interface on top of it.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/crgimenes/glaze">crgimenes/ glaze : Glaze : a CGo-free desktop WebView toolkit for Go ...</a></li>
<li><a href="https://webkitgtk.org/">The WebKitGTK Project</a></li>

</ul>
</details>

**Tags**: `#web-scraping`, `#headless-browser`, `#golang`, `#developer-tools`, `#sandboxing`

---

<a id="item-9"></a>
## [GPU Kernel-Dev Setup Notes: CUDA 13 Drops Maxwell, Pascal and Volta](https://www.reddit.com/r/MachineLearning/comments/1xgisgo/practical_notes_on_setting_up_a_gpu_kerneldev/) ⭐️ 6.0/10

A GPU kernel-engineering practitioner published a setup checklist for a free video series, flagging that CUDA 13 no longer supports Maxwell, Pascal and Volta GPUs, so owners of those cards must fall back to a CUDA 12 toolkit. The notes also cover compute-capability-to-feature mapping (7.5 Turing, 8.0/8.6 Ampere, 8.9 Ada, 9.0 Hopper), the fact that GPUs launch asynchronously so naive Python timers mostly measure queueing, and the ERR_NVGPUCTRPERM error that blocks Nsight Compute counter access for non-admin users. GPU kernel work is increasingly common among ML engineers, and these environment-level traps silently produce wrong benchmarks or block profiling entirely, wasting hours of debugging. The CUDA 13 cutoff in particular affects anyone still running older data-center or consumer cards, and knowing the compute-capability tiers determines which features — tensor cores, FP8, TMA/WGMMA — are even available to you. The post notes that GTX 16-series cards are Turing but lack tensor cores, FP8 requires Ada or Hopper, and Hopper-only features like TMA and WGMMA need an H100 that most people must rent; it also warns that the CUDA version in the nvidia-smi header is only the maximum the driver supports, and that pip-installed PyTorch bundles its own CUDA runtime so torch.cuda.is_available() says nothing about whether nvcc exists. Recommended practice is to warm up, synchronize and use CUDA events averaged over several iterations, reporting dtype alongside throughput computed as roughly 2*M*N*K FLOPs.

reddit · r/MachineLearning · /u/Winter_Mistake_3185 · Oct 27, 04:12

**Background**: CUDA is NVIDIA's parallel-computing platform, and nvcc is its compiler for writing custom GPU kernels; the "compute capability" number identifies a GPU's architecture generation and thus which instructions it supports. CUDA 13 removed support for several older generations, a recurring pattern in NVIDIA's toolkit releases. Because kernel launches return immediately and execute asynchronously on the GPU, timing them correctly requires explicit synchronization primitives such as CUDA events rather than host-side wall-clock timers.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/asynchronous-execution.html">2.5. Asynchronous Execution — CUDA Programming Guide</a></li>
<li><a href="https://research.colfax-intl.com/cutlass-tutorial-wgmma-hopper/">CUTLASS Tutorial: Fast Matrix-Multiplication with WGMMA on NVIDIA...</a></li>
<li><a href="https://www.codegenes.net/blog/pytorch-cuda-async-for-measuring-time/">PyTorch CUDA Async for Time Measurement — codegenes.net</a></li>

</ul>
</details>

**Tags**: `#CUDA`, `#GPU programming`, `#kernel engineering`, `#profiling`, `#environment setup`

---

<a id="item-10"></a>
## [Apple's New M6-Powered iMac Sparks Debate Over Value and Local AI](https://www.apple.com/imac/) ⭐️ 5.0/10

Apple has introduced a new iMac built around the M6 chip, its first 2nm Apple silicon SoC, which pairs a 12-core CPU and 12-core GPU with a dual 16-core Neural Engine. The M6 was announced on August 25, 2026 alongside the M5 Ultra and shipped on September 22, 2026, but the iMac itself remains a familiar 24-inch all-in-one design. The refresh matters less for its silicon than for what it signals about Apple's all-in-one strategy: buyers must pay a substantial premium over a Mac mini for a machine whose display and internals cannot be reused or upgraded. For developers and AI tinkerers, the base M6 also sits on the wrong side of the memory-bandwidth divide that determines whether a Mac can run large local models at all. Community members point out that a comparable Mac mini configuration costs roughly $900 versus about $1,700 for the iMac, with the gap attributed to a 24-inch display, keyboard, and mouse that many consider outdated. The iMac still cannot be used as an external display or docking-station target, and Apple offers no larger 27-inch or 32-inch 6K option.

hackernews · notfried · Oct 27, 13:02 · [Discussion](https://news.ycombinator.com/item?id=50258538)

**Background**: Apple's M-series chips are ARM-based systems-on-chip that integrate CPU, GPU, and unified memory on a single package, replacing Intel processors in the Mac lineup starting with the M1 in 2020. Because the CPU and GPU share the same memory pool, memory bandwidth varies sharply across tiers: base and Pro chips have far less of it than the Max and Ultra variants, which is why the latter are preferred for running large language models locally via frameworks such as MLX. The M6 generation moves to a 2nm process and, per Apple, delivers its biggest gains in AI compute through a doubled Neural Engine.

<details><summary>References</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/">Apple introduces M6 and M5 Ultra for a big leap in ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_M6">Apple M6 - Wikipedia</a></li>
<li><a href="https://github.com/dmitryryabkov/local-ai-mac">GitHub - dmitryryabkov/local-ai-mac: Practical guide to ...</a></li>

</ul>
</details>

**Discussion**: Commenters were largely skeptical: some long-time iMac buyers complained that the machines are overbuilt yet designed to become obsolete in about seven years, and recommended a Mac mini plus Studio Display instead. Others attacked the price-to-performance ratio against the Mac mini, asked for larger 6K screens and the return of target display mode, and argued that memory bandwidth—not chip generation—should decide a Mac purchase for local AI work, with one user preferring an M1 Max with 64GB over an M5 Pro.

**Tags**: `#Apple`, `#iMac`, `#hardware`, `#consumer electronics`, `#local AI`

---

<a id="item-11"></a>
## [ChatGPT Tells Tech-Support Users to Contact 404 Media](https://simonwillison.net/2026/Oct/26/jason-koebler/) ⭐️ 5.0/10

Jason Koebler, co-founder of 404 Media, observed that ChatGPT increasingly responds to people's ordinary tech-support questions by suggesting that they have uncovered something journalistically newsworthy and that 404 Media specifically can help them. The behavior stems from users turning to ChatGPT because big tech platforms make it nearly impossible to reach a human support agent. The anecdote illustrates a concrete, real-world failure mode for large language models: confidently routing users toward a real news outlet that has no obligation or ability to fix their problem. It also highlights how the collapse of human customer support at major platforms is pushing users into unreliable AI substitutes. The remark is drawn from a 404 Media article documenting the pattern; it is a short quoted excerpt rather than a systematic study, so the frequency and precise prompt conditions behind the misdirection are not quantified. The error is a classic hallucination — plausible-sounding but fabricated guidance delivered with unwarranted confidence.

rss · Simon Willison · Oct 26, 19:00

**Background**: AI hallucinations are responses generated by models such as ChatGPT that contain false or misleading information presented as fact, often in a plausible tone; this includes fabricated citations and invented recommendations. Because LLMs predict likely text rather than verify facts, they can blend real entities — like an established tech-news outlet — into advice where those entities do not belong. Meanwhile, many large platforms have replaced or hidden human support behind help centers and chatbots, leaving users to seek answers wherever they can.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_hallucinations">AI hallucinations</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-hallucinations">What are AI hallucinations? - IBM</a></li>

</ul>
</details>

**Tags**: `#ChatGPT`, `#AI hallucinations`, `#customer support`, `#journalism`, `#OpenAI`

---

<a id="item-12"></a>
## [Why do RL environment startups sell to labs instead of training their own models?](https://www.reddit.com/r/MachineLearning/comments/1xggw1k/what_is_the_value_proposition_of_rl_environment/) ⭐️ 5.0/10

A Reddit r/MachineLearning discussion by u/arnavneedshelp questions the value proposition of the wave of startups building RL environments and selling them to frontier labs such as Anthropic and OpenAI, noting he has been "bombarded" with outreach from such companies. The poster argues that if a startup can build an environment that no current model solves but that is still trainable via RL, it could plausibly raise venture funding and train its own model instead of selling the environment. The post probes whether the "environment layer" being built by data and RL-environment vendors is a durable moat or merely a temporary input to labs that already own the training stack. The answer shapes how investors and founders value the growing ecosystem of companies selling RL environments and evaluations, and whether those firms end up as suppliers or as future model developers. The poster lays out the burden of proof such a company faces — showing that a frontier model currently fails the task and that the task is solvable through RL, ideally with a measurable signal such as "gradient information per example" — and offers three explanations: his assumptions about pretraining and infrastructure difficulty are wrong, past environment collection is hard and gatekept by a few labs, or these startups will eventually train their own models. He also cites open-source models lagging the frontier by roughly three months as evidence that frontier progress is mostly new RL environments or very strong distillation.

reddit · r/MachineLearning · /u/arnavneedshelp · Oct 27, 02:37

**Background**: RLVR (Reinforcement Learning with Verifiable Rewards) is a post-training paradigm in which rewards come from objective, rule-based verifiers — for example, checking whether a math answer or unit test passes — rather than from a learned reward model; it underpins work such as DeepSeek-R1 and the GRPO algorithm. An "RL environment" is the task setup and verifier that an agent is trained inside, so whoever owns novel, hard, verifiable environments controls a scarce input to frontier training. A commercial market has emerged in which firms such as Mercor, Surge AI and Mechanize build and sell such environments and evaluations to frontier labs.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2506.14245">[2506.14245] Reinforcement Learning with Verifiable Rewards...</a></li>
<li><a href="https://www.reinforcement-learning.com/kb/rlvr">RLVR : RL with Verifiable Rewards, Explained</a></li>
<li><a href="https://dreaming.press/posts/rl-environments-ai-agent-training-moat.html">The RL Environment Boom: Why Training AI Agents Is Suddenly...</a></li>

</ul>
</details>

**Tags**: `#reinforcement-learning`, `#AI-startups`, `#RLVR`, `#frontier-models`, `#business-strategy`

---

<a id="item-13"></a>
## [Master's student asks MLSys how to handle negative real-robot results](https://www.reddit.com/r/MachineLearning/comments/1xguzyz/what_to_do_with_my_paper_for_mlsys_conference_r/) ⭐️ 5.0/10

A master's student built a hardware accelerator for diffusion-based action generation in robot policies and found that offline outputs had extremely small median absolute deviation from the original model, yet real-robot pick-and-place performance degraded. They are asking the MLSys community whether to submit only the strong offline results or also include the failed deployment, and how to frame and measure the gap. The question highlights a core evaluation gap in ML systems for robotics: offline numerical fidelity to a reference model does not guarantee closed-loop task success after deployment. How MLSys reviewers and authors handle negative real-world results affects benchmarking standards for accelerator and policy-system papers. The student suspects tail errors and closed-loop error compounding explain why a tiny median deviation still causes failure, and asks whether to report percentiles, per-step error, or closed-loop success rate in simulation. They also seek advice from people who have submitted systems papers containing negative real-world deployment results.

reddit · r/MachineLearning · /u/Significant_Bee_2025 · Oct 27, 15:05

**Background**: Diffusion Policy represents a robot's visuomotor policy as a conditional denoising diffusion process that generates action sequences, and it has become a common approach for imitation-learning-based manipulation. MLSys is an interdisciplinary conference at the intersection of machine learning and systems, covering efficient inference, hardware acceleration, and AI-driven system optimization. In closed-loop robot control, small per-step deviations can accumulate over time, so offline deviation metrics are often poor predictors of real-world task success.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2303.04137">[2303.04137] Diffusion Policy: Visuomotor Policy Learning via ... Diffusion Policy: Visuomotor Policy Learning via Action Diffusion Diffusion Policy Diffusion Policy: Generating Robot Actions by Denoising Diffusion Policy - robots-that-learn.github.io Adaptive Diffusion Policy: Efficient Robot Action Generation ... Diffusion policy: Visuomotor policy learning via action diffusion</a></li>
<li><a href="https://diffusion-policy.cs.columbia.edu/">Diffusion Policy</a></li>
<li><a href="https://mlsys.org/">MLSys - 2027 Conference</a></li>

</ul>
</details>

**Tags**: `#MLSys`, `#robotics`, `#diffusion models`, `#hardware acceleration`, `#evaluation metrics`

---

<a id="item-14"></a>
## [Developer releases ApexW, a memory-saving PyTorch optimizer for large GPU workloads](https://www.reddit.com/r/MachineLearning/comments/1xgqtxp/i_built_a_pytorch_optimizer_for_large_gpu/) ⭐️ 5.0/10

A developer has released ApexW, a hobbyist PyTorch optimizer that combines compact optimizer states with a Triton-based execution path and is asking for feedback on GitHub. In optimizer-only micro-benchmarks with a few large tensors, it reported roughly 1.5x faster optimizer steps and about 50% lower optimizer-state memory versus PyTorch's fused AdamW. Optimizer-state memory is a major contributor to out-of-memory failures when fine-tuning transformers and large language models, so halving it could let teams increase batch size or model size without buying new GPUs. However, the gains are so far limited to micro-benchmarks and have not been validated on full training runs. The author openly notes that workloads with many small tensors regress badly: at 128M parameters spread across many small tensors, PyTorch native took 16.1 ms/step while ApexW took 76.0 ms/step, about 0.21x speedup. The automatic execution mode does not consistently reproduce the speedup, and in an end-to-end MLP test PyTorch was still slightly faster overall because of its deep C++ integration.

reddit · r/MachineLearning · /u/Ready_Parking_5435 · Oct 27, 12:11

**Background**: Adam and AdamW-style optimizers maintain first- and second-moment estimates for every parameter, which can consume roughly as much GPU memory as the model weights themselves and become a bottleneck for large-model training. PyTorch's fused AdamW reduces kernel-launch overhead by combining optimizer operations, while Triton is a Python-like language and compiler for writing custom GPU kernels. ApexW tries to combine a Triton kernel path with more compact optimizer states to target the same memory and speed constraints.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.pytorch.org/docs/2.14/generated/torch.optim.AdamW.html">AdamW — PyTorch 2.14 documentation</a></li>
<li><a href="https://christianjmills.com/posts/cuda-mode-notes/lecture-006/">GPU MODE Lecture 6: Optimizing Optimizers in PyTorch – Christian...</a></li>
<li><a href="https://arxiv.org/pdf/2501.07237">GWT: Scalable Optimizer State Compression for Large Language...</a></li>

</ul>
</details>

**Tags**: `#pytorch`, `#optimizers`, `#gpu-memory-efficiency`, `#triton`, `#machine-learning-systems`

---

<a id="item-15"></a>
## [Independent Researcher's KS3 Spline Regressor Outpaces MLP on 4D Mandelbulb Fit](https://www.reddit.com/r/MachineLearning/comments/1xg36lw/fitting_a_4d_mandelbulb_with_ks3_vs_mlp_r/) ⭐️ 5.0/10

An independent researcher released KS3, the third version of K-Splanifolds (KS), a K-dimensional Hermite spline manifold algorithm intended for general-purpose fast regression. In a demonstration video, KS3 fit a 4D Mandelbulb via gradient descent on random samples, converging in roughly 116 seconds versus about 346 seconds for a standard MLP, while showing nearly identical GPU latency. If spline-manifold regressors can match neural network inference latency while converging faster during training, they could become a practical alternative building block for regression tasks in geometry fitting, noise removal, and financial prediction. The work is also notable as solo independent research, though the claims are self-reported and have not yet been independently replicated or peer reviewed. All benchmarks come from a single task—fitting a 4D Mandelbulb—and the researcher reports that the advantage varies by workload, ranging from considerably faster convergence than MLP on noise removal, geometric fitting, and financial prediction to roughly "neck and neck" on LLMs. Only KS1 has an accompanying paper; KS2 and KS3 are documented primarily through code on GitHub, and the author is seeking donated 8x H100 access to attempt a NanoGPT speedrun record using KS3.

reddit · r/MachineLearning · /u/1ncehost · Oct 26, 17:22

**Background**: The Mandelbulb is a three-dimensional fractal developed in 2009 by Daniel White and Paul Nylander as an attempt to find a 3D analogue of the Mandelbrot set; it can be extended beyond three dimensions using n-spherical coordinates, which is what the "4D" version refers to. Fitting such a fractal is a useful stress test for a regressor because it requires approximating highly detailed, high-frequency geometry from random samples. KS (K-Splanifolds) is the author's own linear-scaling compute and memory spline-manifold approach to regression and interpolation, positioned as a competitor to the multilayer perceptron (MLP), the standard fully-connected neural network. The NanoGPT speedrun is a community benchmark in which people race to train a 124M-parameter GPT to a target loss in the shortest wall-clock time, with records having fallen from about 45 minutes originally to around two minutes today.

<details><summary>References</summary>
<ul>
<li><a href="https://agihunt.info/en/p/1a179685352c4af45e6f9756507">KS3 spline regression beats MLP convergence… · AGI Hunt</a></li>
<li><a href="https://github.com/curvedinf/k-splanifolds">GitHub - curvedinf/k-splanifolds: Linear-scaling compute ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mandelbulb">Mandelbulb - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#regression`, `#splines`, `#neural networks`, `#GPU`

---

<a id="item-16"></a>
## [uv 0.13.6 adds new CPython builds, memory-use cuts, and NVIDIA GPU wheel detection preview](https://github.com/astral-sh/uv/releases/tag/0.13.6) ⭐️ 3.0/10

uv 0.13.6, released on 2026-10-26, adds CPython 3.11.18, 3.12.16, 3.13.18, 3.14.10 and 3.15.2 to its managed Python catalog, fixes several configuration and environment-handling bugs, and lands a batch of memory and parsing performance improvements. The release also extends preview features, most notably automatic detection of NVIDIA GPU capabilities when selecting compatible wheel variants. Although this is a routine patch release, the memory reductions for resolving, locking and upgrading large workspaces directly affect teams running big multi-package projects, where uv's speed advantage is a main reason for adoption. The GPU-aware wheel-variant detection preview points toward a future where tools like PyTorch and flash-attn ship multiple hardware-specific wheels and uv picks the right one automatically, instead of users hand-pinning CUDA build indexes. The GPU detection work sits behind the preview `wheel-variants` feature, and the release also makes uv report which unsupported properties caused a wheel variant to be considered incompatible. Bug fixes include preventing `uv run --active --script` and `uv sync --active --script` from deleting non-virtual-environment directories, using `AMD64` for `platform_machine` on x86-64 Windows, preserving free-threaded builds during `uv python upgrade`, and avoiding panics when rendering containment markers with local versions.

github · astral-releases-bot[bot] · Oct 27, 00:47

**Background**: uv is an extremely fast Python package and project manager written in Rust by Astral, positioned as a drop-in replacement for pip, pip-tools, virtualenv and related tools. "Wheel variants" is an emerging packaging proposal in which a single package publishes multiple prebuilt wheels for different hardware backends, such as CPU versus various CUDA versions, so installers can pick the best match for the host machine. Today that selection is largely manual for projects like PyTorch, which is why automatic variant detection is a notable direction for uv.

<details><summary>References</summary>
<ul>
<li><a href="https://pytorch.org/blog/pytorch-wheel-variants/">PyTorch Wheel Variants, the Frontier of Python Packaging</a></li>
<li><a href="https://github.com/astral-sh/uv/issues/16522">Automatic CPU/GPU wheel variant selection for all packages ...</a></li>
<li><a href="https://github.com/wheelnext/nvidia-variant-provider">GitHub - wheelnext/nvidia-variant-provider</a></li>

</ul>
</details>

**Tags**: `#python`, `#package-manager`, `#uv`, `#release-notes`, `#tooling`

---

<a id="item-17"></a>
## [ML PhD student asks how to do 'method research' without PI guidance](https://www.reddit.com/r/MachineLearning/comments/1xgdl42/how_to_do_method_research_when_i_feel_i_have_no/) ⭐️ 3.0/10

A third-year ML PhD student in a small healthcare-focused lab posted on r/MachineLearning asking how to actually do "method research," since their new PI demands it but offers only the Transformers paper and his own work as examples. The student says two years of shifting between topics produced no results, their lab lacks the data for foundation models, and their PI labels every idea too incremental, too applied, or not impactful enough, leaving them without a defined research question. The thread captures a widespread but rarely documented failure mode in ML PhD training: junior researchers in small or newly founded labs receive abstract expectations ("do method research", "be impactful") without concrete scaffolding for scoping a problem. Because top-conference publications are effectively a prerequisite for ML research jobs, this kind of mentorship gap directly shapes who stays in the field and what work gets produced. The lab is only four years old with no PhD graduates yet, and its healthcare datasets are described as "very small," which rules out the large-scale pretraining behind foundation models. The student also notes that the PI's own paper, offered as a model of method research, would fail the PI's current criteria for being too incremental — highlighting how inconsistently the bar is being defined.

reddit · r/MachineLearning · /u/Adventurous_Marroon · Oct 27, 00:06

**Background**: "Method research" in ML usually means contributing a new algorithm, architecture, objective function, or training procedure that generalizes beyond one dataset, in contrast to applied work that adapts existing methods to a specific domain problem. The Transformer paper ("Attention Is All You Need," 2017) is the canonical example: it proposed an architecture built solely on attention mechanisms, dispensing with recurrence and convolutions, and it is cited precisely because the idea transferred far beyond the translation task it was evaluated on. Foundation models, by contrast, are models trained on vast, broad datasets so they can be adapted to many downstream tasks — which is why a lab with small healthcare datasets cannot compete on that axis.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/1706.03762">Abstract page for arXiv paper 1706.03762: Attention Is All You Need</a></li>
<li><a href="https://en.wikipedia.org/wiki/Foundation_model">Foundation model - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#academic-advice`, `#phd-life`, `#machine-learning-research`, `#mentorship`, `#research-methodology`

---

<a id="item-18"></a>
## [Reddit user seeks non-EMA teacher designs for stable self-distillation](https://www.reddit.com/r/MachineLearning/comments/1xgwagz/teachers_other_than_ema_for_distillation_r/) ⭐️ 3.0/10

A Reddit user on r/MachineLearning asked the community for papers or repositories describing teacher formulations for self-distillation other than the standard Exponential Moving Average (EMA) teacher. The user specifically wants teachers that co-evolve with the student, as EMA does, while remaining stable enough to prevent the student from drifting, citing Self-Distillation Fine Tuning (SDFT) as their reference point. The teacher design is the central stability lever in self-distillation, so alternatives to EMA could unlock more responsive, less lag-prone training for continual learning and on-policy fine-tuning setups such as SDFT. Since the question drew no substantive answers, it also highlights a visible gap in synthesized literature on non-EMA teacher mechanisms. The request is narrow and technical: the ideal teacher must both track the student's improvement and damp update noise, which is precisely the trade-off EMA's decay rate controls. Notably, no papers, repositories, or empirical comparisons were supplied in the thread, so the item offers no synthesis or evidence.

reddit · r/MachineLearning · /u/ifaposto · Oct 27, 15:53

**Background**: Self-distillation trains a model on targets produced by a teacher derived from itself, and in methods like Mean Teacher and SDFT that teacher is an EMA of the student's weights, updated as a slow-moving average so targets stay synced yet stable. This mirrors teacher-student paradigms used in semi-supervised and self-supervised pipelines such as DINO-style training, where EMA normalization techniques have been proposed to further stabilize EMA-teacher learning. The core problem is that a teacher that follows the student too closely propagates noise and causes drift, while one that lags too far behind provides stale supervision.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/knowledge-distillation-with-mean-teacher-model">Mean Teacher Model for Knowledge Distillation</a></li>
<li><a href="https://arxiv.org/pdf/2101.08482">Exponential Moving Average Normalization for Self-supervised ...</a></li>
<li><a href="https://arxiv.org/abs/2601.19897">[2601.19897] Self-Distillation Enables Continual Learning</a></li>

</ul>
</details>

**Tags**: `#knowledge-distillation`, `#self-distillation`, `#machine-learning`, `#research-question`, `#reddit`

---

<a id="item-19"></a>
## [Empty GitHub Event: Torvalds Pushed Zero Commits to Linux](https://github.com/torvalds/linux) ⭐️ 1.0/10

A GitHub push-event notification for the torvalds/linux repository reported that Linus Torvalds pushed zero commits, meaning no actual code changes were delivered to the kernel tree. The item carries no diff, no commit message, and no accompanying commentary, making it a null event rather than a real development. This has no bearing on the Linux kernel or its development process, since nothing in the repository changed; it is purely an artifact of how GitHub's event/webhook stream surfaces push activity. Its only practical value is as a reminder that automated event feeds can emit hollow notifications that monitoring or news pipelines should filter out. GitHub delivers push events through its webhook and Events API infrastructure, and such payloads can appear even when the compared commit range is empty, for example when a branch reference is updated without new commits. The item's 1.0/10 score and 'noise' tag reflect that there is no diff, commit metadata, or discussion to analyze.

github · torvalds · Oct 26, 17:22

**Background**: GitHub records repository activity as events and can forward them to external services via webhooks, which send an HTTP POST payload with headers such as X-GitHub-Event to identify the event type. A push event normally describes the commits, branch, and pusher, but the payload can still be emitted when the effective set of new commits is empty. Because feeds that aggregate these events often surface them verbatim, a zero-commit push can end up looking like news even though nothing happened.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.github.com/en/webhooks/webhook-events-and-payloads">Webhook events and payloads - GitHub Docs</a></li>
<li><a href="https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows">Events that trigger workflows - GitHub Docs</a></li>

</ul>
</details>

**Tags**: `#github`, `#linux`, `#empty-event`, `#noise`, `#kernel`

---