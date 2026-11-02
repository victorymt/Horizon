---
layout: default
title: "Horizon Summary: 2026-11-03 (ZH)"
date: 2026-11-03
lang: zh
---

> 从 12 条内容中筛选出 12 条重要资讯。

---

1. [博客文章呼吁读者备份自己珍爱的网站](#item-1) ⭐️ 7.0/10
2. [Ubuntu 处理 CVSS 9.8 内核漏洞的方式在 Hacker News 引发激辩](#item-2) ⭐️ 7.0/10
3. [Kyle Kingsbury：LLM 让成熟度信号更易被伪造](#item-3) ⭐️ 7.0/10
4. [笔记本规模复现：用人类标注验证“好视角优于下一词预测”](#item-4) ⭐️ 7.0/10
5. [Willison 重制人口普查局 AI 采用图表，并关联"超级智能"行政令](#item-5) ⭐️ 6.0/10
6. [Simon Willison 的经验法则：Python 3.15 构建失败时删除过期的 uv.lock 文件](#item-6) ⭐️ 5.0/10
7. [Reddit 讨论：Ilya Sutskever 说“模型只想学习”到底是什么意思](#item-7) ⭐️ 5.0/10
8. [开发者求助：如何在多角度照片间对 YOLO 检测结果去重](#item-8) ⭐️ 5.0/10
9. [Reddit 热议：机器学习博士生更愿在 AI 聊天机器人时代前后读博？](#item-9) ⭐️ 4.0/10
10. [开发者吐槽 SOAP、Shampoo、FOAM、Muon 等优化器名字导致文献检索困难](#item-10) ⭐️ 3.0/10
11. [r/MachineLearning 开设每月自我推广集中帖](#item-11) ⭐️ 2.0/10
12. [Reddit 用户询问 NeurIPS 悉尼会场针对资助获得者的住宿安排进展](#item-12) ⭐️ 2.0/10

---

<a id="item-1"></a>
## [博客文章呼吁读者备份自己珍爱的网站](https://blog.mistys-internet.website/post/2026/10/29/if-you-love-a-website-back-it-up/) ⭐️ 7.0/10

一篇题为"If you love a website, back it up"（如果你爱一个网站，就把它备份下来）的博客文章主张，人们应当亲自抓取并保存自己在乎的网站，以免它们消失；这篇文章在 Hacker News 上引发了一场关于死链、不完整的网络存档与数字保存的广泛讨论。评论者们在讨论中分享了 ArchiveWeb 浏览器扩展和 SingleFile 等实用工具，后者可以把一个页面连同其媒体资源一起保存成单个 HTML 文件。 这场讨论凸显了当今网络的脆弱性：几年前还存在的内现在可能已经返回 404 错误或变成停放域名，而互联网档案馆的 Wayback Machine 根本没有抓取过网络中的很大一部分内容。随着信息获取越来越向中心化平台和 AI 系统集中，个人存档成为抵御链接失效以及历史记录被悄然改写或删除的一种手段。 评论者指出，Wayback Machine 的覆盖并不均衡，因为爬虫受抓取深度和抓取频率的限制，小众论坛和小型个人网站往往落在其范围之外；ArchiveWeb 能够有选择地抓取特定页面和页面元素的能力受到称赞，而 SingleFile 则被推荐用于快速的一次性保存。其他人则指出，借助 AI 重建已消失的网站只能重新组织在别处幸存下来的内容，无法恢复真正已经丢失的数据。

hackernews · ingve · 11月2日 13:25 · [社区讨论](https://news.ycombinator.com/item?id=50336518)

**背景**: 链接失效（link rot，也称链接死亡或引用腐坏）是指超链接随着页面被移动、删除或域名过期而不再指向原本目标的现象，其结果往往是 404 错误或指向无关内容。网络存档试图通过以 WARC 等存档格式收集和保存网络材料来对抗这一趋势，以便日后回放，但研究者指出，由于抓取深度、抓取频率和选择性采集政策的限制，网络存档本质上永远是不完整的。互联网档案馆的 Wayback Machine 是最著名的大规模存档项目，但它无法覆盖整个网络，这正是个人抓取工具显得重要的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Link_rot">Link rot - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Web_archiving">Web archiving - Wikipedia</a></li>
<li><a href="https://link.springer.com/article/10.1007/s00799-015-0153-3">Lost but not forgotten: finding pages on the unarchived web</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的反应以支持为主，评论者描述了自己书签缓慢"腐坏"的过程，其中一人还感叹自己在意的一个论坛下线了，而 Wayback Machine 从未好好抓取过它。多位参与者主张人们应当购买纸质书并在为时未晚时存档重要网站，并对信息的中心化控制发出警告；也有人强调，托管在封闭平台内的视频同样容易被审查，因此也需要备份。

**标签**: `#web-archiving`, `#digital-preservation`, `#link-rot`, `#hacker-news`, `#internet-culture`

---

<a id="item-2"></a>
## [Ubuntu 处理 CVSS 9.8 内核漏洞的方式在 Hacker News 引发激辩](https://chalmovsky.com/posts/wtf-ubuntu) ⭐️ 7.0/10

一篇题为《WTF Ubuntu?》的博客文章批评 Canonical 对某个高危 Linux 内核 CVE 的分级与处置方式，并在 Hacker News 登上首页，获得约 1242 分和 570 条评论。文章的核心不满在于：Ubuntu 安全跟踪页将该问题标记为“Ubuntu Priority: High”而非“Critical”，因此官方没有为用户推送计划外的内核更新。 Ubuntu LTS 被大量生产服务器和云实例使用，因此 Canonical 如何对一个内核漏洞进行分级，直接决定数百万台机器获得补丁的速度。这场讨论还折射出整个行业的更大矛盾：CVSS 这类“原始严重性”评分与 EPSS 所衡量的“实际被利用概率”之间该如何取舍，而后者正日益成为现实补丁优先级排序的依据。 有评论者对文章内容做了事实核查，指出修复后的内核其实已经存在于各 LTS 版本的 “-proposed” 仓库中（可通过 `apt-get -t` 安装，但默认不会下发），其中某个版本已于 10 月 28 日将新内核推入 updates/security 仓库。也有人指出，该 CVE 的 CVSS 评分为 9.8，但 EPSS 分数低于 1%，而且多数安全公告描述的是“在特定条件下”导致内核崩溃或拒绝服务，而非 Anthropic 文章中声称的远程代码执行。

hackernews · chalmovsky · 11月2日 14:52 · [社区讨论](https://news.ycombinator.com/item?id=50337608)

**背景**: CVSS 是广泛使用的 0–10 漏洞严重性评分，9.8 已接近满分；而 EPSS（漏洞利用预测评分系统）则估计某漏洞在未来 30 天内被真实利用的概率，即便是高 CVSS 漏洞，该值也常常远低于 1%。Ubuntu 有自己的分级体系——Critical、High、Medium、Low，其中 Critical 通常会触发超出正常节奏的计划外安全更新。在 Ubuntu 中，修复后的软件包会从 “-proposed” 仓库（预发布、需手动选择）流入普通用户自动接收的 “-updates” 与 “-security” 仓库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.first.org/epss/">Exploit Prediction Scoring System ( EPSS )</a></li>
<li><a href="https://ubuntu.com/security/cves">CVEs | Ubuntu</a></li>

</ul>
</details>

**社区讨论**: 评论情绪明显分化：一部分人为 Ubuntu 辩护，强调该漏洞 EPSS 分数很低、且修复内核已在 -proposed 中可取；另一部分人则抨击跟踪页上那句含糊且自相矛盾的“为什么是这个优先级”说明——它只写了“See ubuntu cvss score”。还有一种反复出现的反驳意见认为，原博客更像是为煽动情绪而写：文章既未说明漏洞本身，也未说明其现实影响或作者自身的暴露情况，而这种“我要找你们经理”的语气在开源社区里毫无助益。

**标签**: `#ubuntu`, `#security`, `#linux-kernel`, `#cve`, `#distro-maintenance`

---

<a id="item-3"></a>
## [Kyle Kingsbury：LLM 让成熟度信号更易被伪造](https://simonwillison.net/2026/Nov/1/kyle-kingsbury/) ⭐️ 7.0/10

在 Simon Willison 摘录的一段评论中，Kyle Kingsbury 于 Jepsen 对 ParticleDB 1.1.4 的分析里指出，LLM 的使用会侵蚀人们对文档、软件及其背后组织的信任，因为过去用来判断系统成熟度的信号如今更容易被伪造。他追问维护者应如何确保软件正确、文档准确，并向用户证明其质量。 这很重要，因为工程师常把文档完善程度、项目成熟度和组织声誉当作质量的替代指标，而 LLM 能以极低成本生成这些表象。一旦这些信号不再可靠，维护者可能需要新的可验证证据，这将影响开源和商业软件赢得信任的方式。 该评论出现在 Jepsen 对面向 AI 工作负载的多模型数据库 ParticleDB 的分析中的“LLM tradeoffs”部分；Jepsen 测试了 1.1.4 至 1.1.18.11.rc-22 等版本。这段摘录提出了信任问题，但并未给出具体的验证机制，因此维护者如何证明质量仍是开放问题。

rss · Simon Willison · 11月1日 16:49

**背景**: Kyle Kingsbury（又名 Aphyr）创建了 Jepsen，这是一个独立项目，通过对分布式数据库和共识系统进行压力测试来验证其正确性与一致性声明。Jepsen 的分析报告因能揭示营销宣传背后的严重缺陷而广受关注。ParticleDB 是一款面向 AI 智能体和 AI 工作负载宣传的数据库，本次引述正出自 Jepsen 对其的测试报告。LLM 能以低成本生成看似专业的文档、代码和项目材料，这正是信任问题的来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jepsen.io/analyses/particledb-1.1.4">Jepsen: ParticleDB 1.1.4</a></li>
<li><a href="https://jepsen.io/">Distributed Systems Safety Research</a></li>
<li><a href="https://particledb.ai/">ParticleDB | The database for AI agents</a></li>

</ul>
</details>

**标签**: `#LLMs`, `#trust`, `#software-quality`, `#documentation`, `#Jepsen`

---

<a id="item-4"></a>
## [笔记本规模复现：用人类标注验证“好视角优于下一词预测”](https://www.reddit.com/r/MachineLearning/comments/1xlzoze/smallscale_check_of_good_views_beat_nexttoken/) ⭐️ 7.0/10

一位独立研究者以笔记本规模复现了 Balestriero 与 LeCun（2026）提出的“好视角优于下一词预测”结论：使用 10,000 张 COCO 图片、每张 5 条人类撰写的描述，图像侧采用冻结的 DINOv2-base 特征，文本侧在三种训练方式下共用同一个 1100 万参数的 4 层编码器。在相同数据、3000 步训练、批大小 256 和 VICReg 式防坍缩损失下，好视角（同一张照片的两条不同描述）在 1,000 张测试照片上的互 10 近邻对齐得分为 0.320，而坏视角（单条描述加掩码片段）为 0.192，下一词预测为 0.148，随机水平为 0.010。 原论文最大规模的实验使用的是图像描述模型生成的文本，这带来一种可能：图像信息通过描述文本泄漏进文本侧，从而虚高了对齐效果；此次检验表明，仅使用人类描述时这一排序依然成立，从而增强了该结论的可信度。这对于“下一词预测是否是学习对齐的、类世界模型表征的正确目标”这一争论意义重大，而这也正是 LeCun 的 JEPA 路线的核心论点。 该研究的规模远小于原论文（1100 万参数、8,000 张训练图片，而原论文为 1.09 亿参数、最高 720 亿），并使用 VICReg 式的方差/协方差正则项替代论文中的 SIGReg，同时需要知道哪些描述对应同一张照片——人类标注者因为看过图片才能做到这一点。更严格的检索指标（配合一次拟合旋转的 R@1）显示差距明显缩小，为 0.084 对 0.063 对 0.057；此外，下一词预测的最佳学习率落在搜索范围的上界，且作者在首次搜索后又追加了一档学习率，并在代码仓库中作了说明。

reddit · r/MachineLearning · /u/Traditional_Frame763 · 11月2日 15:08

**背景**: “柏拉图表征假说”认为，在不同模态和目标上训练的模型会趋于收敛到相似的世界内部表征，因此可以通过比较嵌入之间的最近邻重合度，将文本编码器与 DINOv2 这类冻结的视觉编码器进行对照。DINOv2 是一种自监督视觉模型，其特征被广泛用作视觉语义的固定参照，冻结它便能隔离出文本编码器所学到的内容。Balestriero 与 LeCun 的一系列工作研究的是：以“好视角”——同一张图片的多条不同描述——构建的目标，是否比下一词预测更快地对齐文本与图像表征；这类方法依赖 VICReg 或 SIGReg 等防坍缩正则项，以避免编码器把所有输入映射到同一点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2304.07193">DINOv 2 : Learning Robust Visual Features without Supervision</a></li>
<li><a href="https://sellerbubble.github.io/platonic-representation-hypothesis-on-world-models/">Platonic Representation Hypothesis on World Models</a></li>
<li><a href="https://medium.com/@shreyanshjain05/beyond-llms-yann-lecuns-pure-pixel-world-model-just-solved-jepa-s-biggest-problem-10c1532a86a5">Yann LeCun ’s LeWorldModel: Killing JEPA's Collapse Hack | Medium</a></li>

</ul>
</details>

**标签**: `#machine-learning`, `#representation-learning`, `#reproducibility`, `#multimodal-learning`, `#self-supervised-learning`

---

<a id="item-5"></a>
## [Willison 重制人口普查局 AI 采用图表，并关联"超级智能"行政令](https://simonwillison.net/2026/Nov/2/census-bureau-super-intelligence/) ⭐️ 6.0/10

Simon Willison 使用美国人口普查局于 2026 年 10 月 22 日发布的最新《商业趋势与展望调查》数据，重新绘制了阿波罗全球管理公司的 AI 采用率图表；在此过程中他发现，普查局在 2025 年 11 月把调查问题从"在生产商品或服务中使用 AI"扩大为"在任何业务职能中使用 AI"，导致新旧数据序列不可比。他还提到，普查局已与 2026 年 9 月 29 日签署的第 14434 号行政令（即他所称"愚蠢的""超级智能"行政令）产生了冲突。 这一事件说明：政府调查中一处措辞调整，就足以让一整年的趋势线失效，这对那些曾引用"大企业 AI 采用率正在下降"说法的人（分析师、经济学家、记者）具有直接影响。它也表明联邦统计机构与 AI 政策指令之间的牵扯日益加深，因为人口普查局的数据集是衡量 AI 在现实中普及程度的主要来源。 普查局的双周调查从 120 万家企业中抽取 20 万家，并轮换样本组，使每家企业每十二周才被调查一次，数据在隔周的周四上午 10 点发布；在扩大后的问题口径下，员工 250 人以上企业的采用率为 40.7%，100–249 人为 33.5%，50–99 人为 27.9%，而最小规模组约为 21–23%。该图表有意留出一段阴影空档——涵盖 2025 年政府停摆以及等待新措辞下六次观测值的时期——并对两种问题口径分别计算六次调查的移动平均值，不做跨断点的衔接。

rss · Simon Willison · 11月2日 13:31

**背景**: 《商业趋势与展望调查》（BTOS）是人口普查局的快速反应式企业调查，目的是近乎实时地反映美国经济状况；由于它直接询问企业是否使用 AI，已成为被引用最多的 AI 采用率衡量指标之一。2025 年 9 月，阿波罗全球管理公司首席经济学家 Torsten Slok 发布了一张基于 BTOS 数据的图表，似乎显示大企业的 AI 采用率趋于停滞甚至下降；Willison 此前曾把这张图表当作测试 GPT-5 和 Claude 数据分析工具的案例。Willison 所提到的第 14434 号行政令于 2026 年 9 月 29 日签署，标题为"开启超级智能时代"，但他的文章并未详述该命令的具体条款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.whitehouse.gov/presidential-actions/2026/09/inaugurating-the-era-of-super-intelligence/">Inaugurating The Era Of Super Intelligence – The White House</a></li>
<li><a href="https://www.federalregister.gov/documents/2026/10/02/2026-20321/inaugurating-the-era-of-super-intelligence">Inaugurating the Era of Super Intelligence - Federal Register</a></li>
<li><a href="https://www.apolloacademy.com/ai-adoption-rate-trending-down-for-large-companies/">AI Adoption Rate Trending Down for Large... - Apollo Academy</a></li>

</ul>
</details>

**标签**: `#AI adoption`, `#Census Bureau`, `#executive order`, `#data analysis`, `#AI policy`

---

<a id="item-6"></a>
## [Simon Willison 的经验法则：Python 3.15 构建失败时删除过期的 uv.lock 文件](https://simonwillison.net/2026/Nov/1/delete-uv-lock-first/) ⭐️ 5.0/10

Simon Willison 分享了他切换到 Python 3.15 后开始依赖的一条排查经验法则：“拿不准时，就删掉 uv.lock 文件”。他描述了具体的失败场景：锁文件把某个依赖固定在一个尚无 Python 3.15 wheel 的版本上（文中例子是 `watchfiles==1.1.1`），于是 uv 退回到从源码构建，而 `maturin.build_wheel` 因为 PyO3 最高只支持到 Python 3.14 而报错；删除该文件并重新运行 `uv run pytest` 通常即可解决。 这是新版 CPython 发布与原生扩展生态跟进之间存在时间差的一个具体而真实的体现：通过 maturin 使用 Rust/PyO3 构建的包，只能为绑定已支持的 Python 版本生成 wheel。对于早早升级到 Python 3.15 的开发者来说，这条经验把一个晦涩的构建错误变成了只需一条命令就能解决的常规操作。 Willison 指出，他的大多数项目都是库，而库刻意不提交 `uv.lock`（库不应当为下游使用者锁定版本），因此这些锁文件只是本地 `uv run` 命令留下的产物，并且早已被列入 `.gitignore`。这意味着删除它们既安全又低成本——这条法则适用于一次性的本地锁文件，而不适用于那些为可复现构建而有意提交锁文件的应用程序。

rss · Simon Willison · 11月1日 23:24

**背景**: `uv` 是一个用 Rust 编写的极快的 Python 包与项目管理器，用于替代 pip、pip-tools 等工具；它的 `uv.lock` 是一种通用锁文件，为项目依赖及其全部传递依赖锁定精确版本，可跨操作系统、架构和 Python 版本通用。wheel 是预编译的二进制包，安装极快，而源码分发包（sdist）则需要在本地编译。对于用 Rust 编写的扩展，maturin（前身是 pyo3-pack）借助 PyO3 绑定来构建 wheel，而 PyO3 只能面向它明确支持的 Python 解释器版本，因此像 3.15 这样的全新 Python 版本可能会在 PyO3 跟进之前被拒绝。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.astral.sh/uv/concepts/projects/sync/">Locking and syncing | uv - docs.astral.sh</a></li>
<li><a href="https://pyo3.rs/main/building-and-distribution/multiple-python-versions.html">Supporting multiple Python versions - PyO3 user guide</a></li>
<li><a href="https://www.maturin.rs/">Introduction - Maturin User Guide</a></li>

</ul>
</details>

**标签**: `#Python`, `#uv`, `#dependency-management`, `#packaging`, `#developer-tooling`

---

<a id="item-7"></a>
## [Reddit 讨论：Ilya Sutskever 说“模型只想学习”到底是什么意思](https://www.reddit.com/r/MachineLearning/comments/1xlyr77/what_did_ilya_sutskever_mean_when_he_said_the/) ⭐️ 5.0/10

r/MachineLearning 上的一篇帖子重新翻出了 Ilya Sutskever 在 OpenAI 成立前不久说过的一句话——“听着，这些模型，它们就是想要学习，你必须理解这一点”——并请社区解读其含义；发帖人明确不认同 Dario Amodei 的诠释，即这句话只是说“给模型好数据、足够的空间和正常的数值条件，训练自然会完成它的工作”。 这句话是规模假设（scaling hypothesis）背后直觉的早期表述，因此对它的解读直接关系到“为什么用简单目标训练的大模型竟然能泛化”这一核心问题——这也是当下基础模型竞赛所依赖的核心假设，而不少从业者仍认为该问题尚无定论。 发帖人指出这句话大约出自十年前，并质疑为何被拟人化的是“模型”而不是优化器或梯度下降本身；他还认为，如果含义纯粹是操作层面的建议，Sutskever 大概会用更平实的方式表述。该讨论偏向哲学思辨而非技术成果，且所提供的材料中不包含实质性的评论内容。

reddit · r/MachineLearning · /u/XTXinverseXTY · 11月2日 14:32

**背景**: 训练动力学（training dynamics）研究的是网络在优化过程中损失和内部表示如何演化；研究者常通过分析损失“景观”（optimization landscape）的几何性质，来解释为何梯度下降在非凸情形下仍能找到具备泛化能力的解。Sutskever 所说的“不要在数值上把它们条件化得很糟”，指的是输入、激活值或学习率缩放不当导致优化不稳定的常见失效模式。而“模型就是想要学习”这种说法，是一种刻意的禅宗式表达，意思是：只要网络足够大、梯度信号足够好，它自己就会把损失降下去——这一直觉后来被形式化为缩放定律（scaling laws）以及“通用方法胜过手工设计”的“苦涩教训”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.offconvex.org/2018/11/07/optimization-beyond-landscape/">Understanding optimization in deep learning by analyzing trajectories...</a></li>
<li><a href="https://ai-blog.it/blog/optimization-landscapes-neural-networks">Optimization Landscapes and Why Neural Networks Train at All</a></li>

</ul>
</details>

**标签**: `#machine-learning`, `#AI-philosophy`, `#training-dynamics`, `#model-behavior`, `#reddit-discussion`

---

<a id="item-8"></a>
## [开发者求助：如何在多角度照片间对 YOLO 检测结果去重](https://www.reddit.com/r/MachineLearning/comments/1xloo4i/how_to_handle_object_deduplication_across/) ⭐️ 5.0/10

一位开发者在 r/MachineLearning 发帖求助：用户会上传同一场景的 3–4 张不同角度照片（正面、侧面、特写），如何对 YOLO 在这些照片中检测到的同一物理对象进行去重，使每个唯一对象在每个会话中只被计数和描述一次。该问题特别关注尺寸极小、约 20x22 像素、保存为轻量 .webp 图像的裁剪块，这比使用全分辨率检测结果进行匹配要困难得多。 其目标是避免对早前照片中已经处理过的对象重复调用昂贵的下游 AI 服务（例如视觉语言模型描述），这直接影响生产流水线的推理成本与延迟。微小裁剪块的多视角重识别是公认的难题，因此这一问题的解法对任何基于 YOLO 构建拍照盘点、商品编目或巡检类应用的人都具有参考价值。 在约 20x22 像素的尺度下，裁剪块保留的判别性外观信息非常有限，因此直接做像素比对或使用通用 CNN 嵌入都不可靠，而且同一对象在不同角度和光照下外观差异明显。由于各会话相互隔离，匹配只需在单个用户的小规模照片集合内进行，这排除了训练专用重识别模型的做法，更适合采用嵌入余弦距离、感知哈希，或“类别 + 空间上下文”约束之类的轻量相似度策略。

reddit · r/MachineLearning · /u/Expert-Ad598 · 11月2日 05:15

**背景**: 对象重识别（Re-ID）是指在不同图像、视频帧或摄像头视角中识别出同一物理实体的任务，在视角、尺度与光照都不断变化的监控和多摄像头系统中一直是长期难题。YOLO 是一类实时目标检测模型，输出边界框和类别标签，通常会被裁剪后送入后续模型提取属性。小目标检测研究表明，小于约 32x32 像素的对象在深度网络处理过程中会丢失判别性特征，这正是微小裁剪块难以匹配的原因；常见的缓解手段包括切片/滑窗推理，以及在向量数据库中进行基于嵌入的相似度检索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zilliz.com/blog/milvus-and-surveillance-how-vector-dbs-transform-multi-camera-tracking">Vector Databases: Transforming Multi- Camera Tracking... - Zilliz blog</a></li>
<li><a href="https://inass.org/wp-content/uploads/2025/04/2025083109-2.pdf">Semantic-Aware Image Deduplication : Leveraging Object ...</a></li>
<li><a href="https://towardsdatascience.com/increasing-performance-when-detecting-small-objects-using-data-crops-d9b8daabd18/">Increasing Performance When Detecting Small Objects Using ... Introducing SAHI and Sliding Window Functions for Small ... Enhanced lightweight detection of small and tiny objects in ... Tiny object detection: An in-depth survey of techniques ... What Is Object Re-Identification (Re-ID)? - roboflow.com</a></li>

</ul>
</details>

**标签**: `#object-detection`, `#YOLO`, `#re-identification`, `#deduplication`, `#computer-vision`

---

<a id="item-9"></a>
## [Reddit 热议：机器学习博士生更愿在 AI 聊天机器人时代前后读博？](https://www.reddit.com/r/MachineLearning/comments/1xlt9wm/ml_phds_would_you_rather_have_done_your_phd/) ⭐️ 4.0/10

一位用户在 r/MachineLearning 版块发帖提问：如果可以重新选择，正在攻读或已完成机器学习博士的人，是更愿意在 ChatGPT 等 AI 聊天机器人普及之前完成博士学业，还是更愿意在当下这个 AI 无处不在的时代读博？该帖希望收集个人经验，探讨所处时代如何影响研究方向、工具使用和职业前景。 这个问题触及机器学习研究文化中的一条真实分界线：聊天机器人出现之前读博的人成长于模型更小、算力更稀缺的时代，而现在的学生既拥有强大的 AI 助手，也面临日益拥挤领域的激烈竞争。相关讨论可以为正在权衡何时以及如何攻读机器学习研究生的准学生提供参考。 原帖只是一个简短的开放式提问，没有数据、投票或研究方法支撑，因此回答多为个人轶事，并受到评论者自我选择的影响。该帖在 r/MachineLearning 上被归为讨论类话题，这类偏职业发展的问题通常引发观点交流而非技术性证据。

reddit · r/MachineLearning · /u/Hope999991 · 11月2日 10:04

**背景**: ChatGPT 于 2022 年底发布后，大语言模型迅速普及，AI 助手成为科研和编程工作中的日常工具。对机器学习博士生而言，这改变了哪些技能更重要（如提示设计、评估、工具使用），也引发了新的疑问：当模型已经能生成代码和文献综述时，哪些研究方向仍具新意。博士通常需要四到六年，因此 2022 年前入学的学生与今天入学的学生所经历的研究环境截然不同。

**标签**: `#ML PhD`, `#AI chatbots`, `#career advice`, `#research culture`, `#community discussion`

---

<a id="item-10"></a>
## [开发者吐槽 SOAP、Shampoo、FOAM、Muon 等优化器名字导致文献检索困难](https://www.reddit.com/r/MachineLearning/comments/1xl7yv0/why_do_all_nn_optimizers_have_weird_names_d/) ⭐️ 3.0/10

一位 Reddit 用户在 r/MachineLearning 上吐槽说，SOAP、Shampoo、FOAM 和 Muon 这类神经网络优化器的名称在文献检索时会返回大量完全不相关的结果，因为这些名字并不唯一。该用户还指出，如果不是因为 Adam 已经足够出名，它也会有同样的问题，并表示这一问题让他在查找相关资料时浪费了很多时间。 这一抱怨揭示了快速发展的研究领域中的一个实际痛点：随着新优化器不断涌现，含义模糊的名称让从业者和新入行者更难找到正确的论文、代码和讨论。它还触及一个更广泛的问题，即机器学习社区应如何为算法命名，才能让搜索、文档和工具链保持可用。 被点名的具体对象包括：SOAP（在 Shampoo 基础上结合 Adam 式预条件的方法）、Shampoo（一种二阶预条件随机张量优化方法）、FOAM，以及与物理学中次原子粒子同名的 Muon。发帖人承认 Muon 的名字“稍好一些”，但仍然面临同样的检索噪声问题。

reddit · r/MachineLearning · /u/Future_Pace_5290 · 11月1日 16:51

**背景**: 优化器是在训练过程中更新神经网络权重的算法，多年来 Adam（以及 AdamW）一直是默认选择。研究者长期在探索更高阶或带预条件的方法，例如 Shampoo 通过矩阵预条件器为每个参数张量自适应地调整更新量；近来的 Muon 则对隐藏层参数采用矩阵感知、基于谱范数的更新方式；SOAP 进一步把 Shampoo 的预条件与 Adam 的二阶矩估计结合起来。由于这些方法常被赋予简短而形象的名字，它们经常与常见词汇及其他领域的术语撞名，从而给基于关键字的文献检索带来麻烦。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2409.11321">SOAP: Improving and Stabilizing Shampoo using Adam SOAP: Improving and Stabilizing Shampoo using Adam GitHub - nikhilvyas/SOAP SOAP: Improving and Stabilizing Shampoo using Adam SOAP: IMPROVING AND STABILIZING SHAMPOO USING ADAM GitHub - NoteDance/SOAP: TensorFlow implementation for "SOAP ... OPT2024: 16th Annual Workshop on Optimization for Machine ...</a></li>
<li><a href="https://kellerjordan.github.io/posts/muon/">Muon : An optimizer for hidden layers in neural networks</a></li>
<li><a href="https://proceedings.mlr.press/v80/gupta18a/gupta18a.pdf">Shampoo : Preconditioned Stochastic Tensor Optimization</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#optimizers`, `#naming`, `#searchability`, `#community discussion`

---

<a id="item-11"></a>
## [r/MachineLearning 开设每月自我推广集中帖](https://www.reddit.com/r/MachineLearning/comments/1xlmffv/d_selfpromotion_thread/) ⭐️ 2.0/10

r/MachineLearning 的 AutoModerator 发布了一个定期自我推广集中帖，用户可以在其中分享个人项目、初创公司、产品、合作需求以及博客。该帖会一直保持活跃直到下一个帖子发布，并且用户被要求披露任何产品或服务的收费与定价信息。 通过将推广类帖子集中到一个帖子里，版主希望让主版面的信息流继续聚焦于技术讨论和提问。对于正在做副业项目或创业的机器学习从业者来说，这个帖子成为获得大量技术受众关注的合规渠道，而不必冒因刷屏被封禁的风险。 该帖明确禁止短链接、链接聚合网站和自动订阅链接，并警告任何滥用信任的行为都会导致封禁。帖子还说明这是一次实验，如果社区不喜欢就会被取消，并鼓励用户把新的推广帖子改为发布到这个集中帖中。

reddit · r/MachineLearning · /u/AutoModerator · 11月2日 03:15

**背景**: 像 r/MachineLearning 这样的 subreddit 依靠志愿版主和 AutoModerator 之类的机器人来执行发帖规则。自我推广是技术社区中常见的矛盾来源，因为它会用低价值的营销内容淹没主信息流，因此许多 subreddit 会设立定期集中帖作为折中方案。这类元帖子本身不包含技术内容，纯粹是社区管理机制的一部分。

**标签**: `#reddit`, `#machine-learning`, `#community-meta`, `#self-promotion`, `#moderation`

---

<a id="item-12"></a>
## [Reddit 用户询问 NeurIPS 悉尼会场针对资助获得者的住宿安排进展](https://www.reddit.com/r/MachineLearning/comments/1xlzumq/any_update_with_the_accomodation_from_neurips_d/) ⭐️ 2.0/10

一位 Reddit 用户在 r/MachineLearning 上发帖，询问 NeurIPS 主办方是否已就获得财务资助的参会者的住宿安排发布任何更新，并特别说明是针对悉尼举办的这一届会议。该帖只是一则简短的提问，没有附带答案或官方信息。 差旅与住宿费用是依靠资助参会的学者面临的最大实际障碍，因此住宿安排的明确程度直接决定获资助者能否真正到场。对于在悉尼这样距离远、消费高的城市举办的会议，住宿信息迟迟不公布会迫使参会者临时预订昂贵的机票和酒店。 该问题来自一位获得财务资助的参会者，在现有内容中尚未得到答复，也没有引用 NeurIPS 主办方的任何官方说明。它还凸显了资助结果通知与获资助者实际安排行程所需的后勤细节之间的协调缺口。

reddit · r/MachineLearning · /u/Fantastic-Nerve-4056 · 11月2日 15:14

**背景**: NeurIPS（神经信息处理系统大会）是规模最大的年度人工智能与机器学习研究会议之一，参会者数以万计。与许多大型学术会议一样，它设有财务资助或差旅补助项目，帮助资金有限的学生和研究人员支付注册费、交通和住宿费用。NeurIPS 每年轮换举办城市，并已宣布悉尼将作为未来的一站，这意味着许多获资助者需要面对长途国际旅行以及陌生且价格更高的住宿市场。

**标签**: `#NeurIPS`, `#conference logistics`, `#accommodation`, `#financial grants`, `#machine learning community`

---