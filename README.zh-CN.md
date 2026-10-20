# Awesome Edge–Cloud LLM & Agent Collaboration

[English](README.md) | **简体中文**

收集 **LLM/Agent 端云协同**（含机器人与具身 agent）的论文、代码与数据集，按“优化什么”分类，重点关注端云之间交换什么，以及这些内容如何转化为端侧可复用能力。

**范围截至 2026-10-18 · 52 篇 · 46 篇核心工作 + 6 篇邻近工作。** 日期为所链接 arXiv 版本日期，首次提交日期另存于数据文件。本文献清单不是穷尽性综述，也不是统一性能排行榜。

多数近期工作为 preprint；录用信息采用作者在 arXiv/项目页的报告。代码仅收录论文关联的作者链接；“未定位”不等于不存在。收益以作者实验为准，真实设备、服务器模拟和无线仿真应分别理解。

## 导航

- [Skill、计划与轨迹协同](#skills)
- [路由与求助决策](#routing)
- [上下文与模态选择](#context)
- [个性化与知识迁移](#personalization)
- [协同训练与联邦优化](#training)
- [Token 级协同解码](#decoding)
- [具身与机器人端云协同](#embodied)
- [邻近工作与迁移机会](#adjacent)
- [实验依据与边界](docs/evidence.md)
- [研究问题与评估口径](docs/research-agenda.md)
- [文献数据](data/papers.json) · [BibTeX](references.bib) · [贡献指南](CONTRIBUTING.md)

## 分类视角

| 优化对象 | 典型决策 | 代表工作 |
| --- | --- | --- |
| 指导内容 | 云端返回什么结构、多细的指导？ | Co-Skill, EcoAgent |
| 执行位置 | 哪个 query 或 agent step 需要云端？ | Hera, GAPG |
| 上传内容 | 哪些模态与 observation 值得上传？ | TMO, Co-Skill |
| 端侧能力 | 生成什么训练数据，适配哪些参数组件？ | CDCDA-PLM, CIDERS |
| 训练协议 | 训练放在哪里，传 activation、低维更新还是 scalar？ | MobiLLM, FedKRSO, FedKSeed, pAirZero |
| 协同解码 | draft、验证与 rejection 恢复如何协作？ | AceSpec, Speculation at a Distance |
| 具身控制 | 机器人与远端算力之间如何划分感知、策略推理与控制，以应对时延与带宽限制？ | CloudEdgeVLA, RoboECC, EcoVLA |

分类是主入口，论文可以跨多个优化对象；例如 Co-Skill 同时涉及上传轨迹和下发指导。

## 建议阅读顺序

- 内容与 skill：**Co-Skill → EcoAgent → TMO**。
- 长程 agent 路由：**Hera → GAPG**。
- 个性化：**CIDERS → CDCDA-PLM**。
- Forward-only 训练：**FedKSeed → pAirZero**，以 **FedKRSO** 作一阶子空间对照。
- 解码系统：**AceSpec → Speculation at a Distance**，同时检查延迟与吞吐。
- GUI agent 的上传内容：**CORE → PAAC → PrivacyGuard**。
- 机器人：**CloudEdgeVLA → RoboECC → EcoVLA**，区分模拟时延与真实测试平台。

<a id="skills"></a>

## Skill、计划与轨迹协同

| 版本日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10-13 · v2 | **CoMIC** — [CoMIC: Collaborative Memory and Insights Circulation for Long-Horizon LLM Agents in Web Cloud-Edge Systems](https://arxiv.org/abs/2606.00756v2) | 端侧 Web agent 借助以子目标为单位的分层记忆在本地执行；云端 LLM 评审异步评估上传的子目标轨迹、筛选可复用经验，并按规范化子目标标识把指导分发回所有端侧 agent，全程不更新模型参数。 | [paper](https://arxiv.org/abs/2606.00756v2) · 代码未定位 · [evidence](docs/evidence.md#2606-00756) |
| 2026-10-09 · v1 | **SLM Interpreter** — [Should SLMs be in the Driver's Seat? A Study of Local Models as Interpreters in Cloud-Written Agent Programs](https://arxiv.org/abs/2610.14209v1) | 云端 LLM 为用户任务写一段在设备上运行的 Python 程序，程序只在需要解读用户数据的有界问题上通过普通函数调用本地 SLM；执行出错时把 stack trace 发回 LLM 重写，最多尝试五次。 | [paper](https://arxiv.org/abs/2610.14209v1) · 代码未定位 · [evidence](docs/evidence.md#2610-14209) |
| 2026-09-26 · v1 | **REBASE** — [REBASE: Device-Cloud Experience Coherence for GUI Agents Across App Updates](https://arxiv.org/abs/2609.32130v1) | 让手机 GUI agent 缓存的操作路径在应用更新后仍与云端副本一致：云端在新版本上重放，端侧执行前逐步校验，校验失败时逐级上传证据，直到云端返回按版本索引、可供整个设备群复用的补丁。 | [paper](https://arxiv.org/abs/2609.32130v1) · 代码未定位 · [evidence](docs/evidence.md#2609-32130) |
| 2026-09-17 · v2 | **Co-Skill** — [Co-Skill: A Collaborative Communication Framework for Skill Evolution](https://arxiv.org/abs/2609.16008v2) | 合并上传轨迹的公共前缀，并按端侧执行失败逐步细化下发的 skill tree。 | [paper](https://arxiv.org/abs/2609.16008v2) · 代码未定位 · [evidence](docs/evidence.md#2609-16008) |
| 2026-04-27 · v1 | **GoClick** — [GoClick: Lightweight Element Grounding Model for Autonomous GUI Interaction](https://arxiv.org/abs/2604.23941v1) | 一个 2.3 亿参数的编码器-解码器 GUI 元素定位模型；在其端云 agent 设定中，云端 VLM 规划器（如 GPT-4o）输出动作意图或目标元素的功能描述，GoClick 在端侧根据同一张截图定位元素。 | [paper](https://arxiv.org/abs/2604.23941v1) · [code](https://github.com/ZJULiHongxin/GoClick) · [evidence](docs/evidence.md#2604-23941) |
| 2026-04-09 · v1 | **AdecPilot** — [Administrative Decentralization in Edge-Cloud Multi-Agent for Mobile Automation](https://arxiv.org/abs/2604.07767v1) | 云端只负责与界面无关的战略设计，输出抽象里程碑；端侧双模态 agent 团队负责战术规划与定位、在没有云端介入时自我纠错，并用分层隐式终止协议判断何时停止。 | [paper](https://arxiv.org/abs/2604.07767v1) · 代码未定位 · [evidence](docs/evidence.md#2604-07767) |
| 2025-11-17 · v3 | **EcoAgent** — [EcoAgent: An Efficient Device-Cloud Collaborative Multi-Agent Framework for Mobile Automation](https://arxiv.org/abs/2505.05440v3) | 云端规划，端侧观察与验证，上传简洁屏幕摘要，用反馈闭环触发调整。 | [paper](https://arxiv.org/abs/2505.05440v3) · [code](https://github.com/Yi-Biao/EcoAgent) · [evidence](docs/evidence.md#2505-05440) |

<a id="routing"></a>

## 路由与求助决策

| 版本日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10-13 · v1 | **EdgeWise** — [EdgeWise: Bringing Long-Horizon Agents to the Edge via Selective Cloud Delegation](https://arxiv.org/abs/2610.17560v1) | 端侧 SLM 作为长程 coding agent 任务的主求解者，只把选中的步骤交给云端 LLM；是否委托由外部 judge 决定，或由经过 SFT 和 step-level RL（对每个委托决策单独分配 credit）训练的 SLM 自己决定。 | [paper](https://arxiv.org/abs/2610.17560v1) · 代码未定位 · [evidence](docs/evidence.md#2610-17560) |
| 2026-10-13 · v1 | **EC2-Bench** — [Empowering Edge Agents: A Systematic Analysis of Edge-Cloud Collaboration in LLM Agent Execution](https://arxiv.org/abs/2610.17816v1) | 构建 EC2-Bench：128 个可执行的数字工作区 agent 任务，从任务完成度、云端费用与端侧 FLOPs、标注的敏感信息被云端看到的比例三方面打分，并用它比较 query 路由、逐步路由、端侧主导的委托和端侧主导的咨询四种协同方式。 | [paper](https://arxiv.org/abs/2610.17816v1) · [code](https://github.com/OpenBMB/EC2-Bench) · [evidence](docs/evidence.md#2610-17816) |
| 2026-10-10 · v2 | **Local-First Intelligence** — [Local-First Intelligence via Proactive SLM Collaborating with Feedback-Providing LLM](https://arxiv.org/abs/2604.17827v2) | 用 RL 训练端侧 SLM 在多轮中决定何时、以何种请求向云端 LLM 求助，云端 LLM 只经提示、可以回答或要求澄清；奖励综合答案质量、交互必要性、澄清反馈与隐私泄露惩罚，训练数据来自合成的隐私增强 QA 数据集 PrivQA。 | [paper](https://arxiv.org/abs/2604.17827v2) · 代码未定位 · [evidence](docs/evidence.md#2604-17827) |
| 2026-10-05 · v3 | **OpenPhone** — [OpenPhone: Mobile Agentic Foundation Models](https://arxiv.org/abs/2510.22009v3) | 默认由经 SFT 再 GRPO 调优的 3B 端侧 GUI agent 执行；定期监控发现重复动作、偏离预期轨迹或动作质量不足时，把任务切换给云端 MLLM。 | [paper](https://arxiv.org/abs/2510.22009v3) · [code](https://github.com/HKUDS/PhoneCLI) · [evidence](docs/evidence.md#2510-22009) |
| 2026-09-27 · v1 | **On-Device Operation Caches** — [On Device Agentic Operation Caches -- Classifier-Centric NL-to-Action Generation](https://arxiv.org/abs/2609.33141v1) | 把高频的自然语言到操作请求转成对缓存操作模板的分类，由端侧微调的小模型完成；置信度高的命中在本地执行，低置信度请求交给云端模型。 | [paper](https://arxiv.org/abs/2609.33141v1) · 代码未定位 · [evidence](docs/evidence.md#2609-33141) |
| 2026-07-31 · v1 | **SPECTRA** — [SPECTRA: On-Device Cognitive Perturbation and Trajectory Analysis for Autonomous Edge-Cloud GUI Grounding](https://arxiv.org/abs/2609.35775v1) | 通过遮挡关键视觉锚点、测量端侧模型 prefill 阶段隐藏状态轨迹的漂移程度，判断端侧 GUI 定位 agent 是否需要请求云端，请求决策无需自回归解码。 | [paper](https://arxiv.org/abs/2609.35775v1) · 代码未定位 · [evidence](docs/evidence.md#2609-35775) |
| 2026-05-28 · v1 | **Hybrid MAS** — [When Cloud Agents Meet Device Agents: Lessons from Hybrid Multi-Agent Systems](https://arxiv.org/abs/2605.30102v1) | 把两种多 agent 架构改造成端云混合推理：云端监督者为端侧执行者做规划、验证与重规划（PEVR），以及先执行后验证的变体（EVA）；系统测量骨干模型与监督频率如何影响准确率、API 成本和估算的端侧能耗。 | [paper](https://arxiv.org/abs/2605.30102v1) · 代码未定位 · [evidence](docs/evidence.md#2605-30102) |
| 2026-05-23 · v1 | **Hera** — [Hera: Learning Long-Horizon Coordination for Device-Cloud Collaborative LLM Agents](https://arxiv.org/abs/2605.24598v1) | 外部协调器先模仿学习，再以长程任务结果与云调用成本做 RL，逐步选择端或云。 | [paper](https://arxiv.org/abs/2605.24598v1) · 代码未定位 · [evidence](docs/evidence.md#2605-24598) |
| 2026-05-23 · v4 | **GAPG** — [Bridging On-Device and Cloud LLMs for Collaborative Reasoning: A Unified Methodology for Local Routing and Post-Training](https://arxiv.org/abs/2509.24050v4) | 通过自适应策略梯度联合训练端侧推理与内部求助决策。 | [paper](https://arxiv.org/abs/2509.24050v4) · 代码未定位 · [evidence](docs/evidence.md#2509-24050) |
| 2026-03-09 · v2 | **MCCom** — [Balancing Latency and Accuracy of Code Completion via Local-Cloud Model Cascading](https://arxiv.org/abs/2603.05974v2) | 把本地小代码模型与云端 LLM 级联用于行级补全：小模型先用推测解码生成候选，建议被拒绝后才调用云端模型，被拒的候选还用来在云端阶段前重排检索到的代码片段。 | [paper](https://arxiv.org/abs/2603.05974v2) · [code](https://github.com/ZJU-CTAG/MCCom) · [evidence](docs/evidence.md#2603-05974) |
| 2025-12-26 · v1 | **MAI-UI** — [MAI-UI Technical Report: Real-World Centric Foundation GUI Agents](https://arxiv.org/abs/2512.22047v1) | 一组 GUI agent 模型，其端侧版本同时监控自身轨迹：当轨迹偏离指令且上下文不含隐私敏感数据时，把后续步骤连同错误摘要交给云端 agent，双方共享端侧统一的轨迹记忆。 | [paper](https://arxiv.org/abs/2512.22047v1) · [code](https://github.com/Tongyi-MAI/MAI-UI) · [evidence](docs/evidence.md#2512-22047) |
| 2025-02-06 · v1 | **Division-of-Thoughts** — [Division-of-Thoughts: Harnessing Hybrid Language Model Synergy for Efficient On-Device Agents](https://arxiv.org/abs/2502.04392v1) | 把用户查询分解为子任务并构建依赖图以并行推理，用 SLM 上一个由执行反馈训练的插件式适配头决定每个子任务交给本地 SLM 还是云端 LLM。 | [paper](https://arxiv.org/abs/2502.04392v1) · [code](https://github.com/tsinghua-fib-lab/DoT) · [evidence](docs/evidence.md#2502-04392) |

<a id="context"></a>

## 上下文与模态选择

| 版本日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10-18 · v2 | **PAAC** — [PAAC: Privacy-Aware Agentic Device-Cloud Collaboration](https://arxiv.org/abs/2605.08646v2) | 让规划者与执行者的分工对齐端云信任边界：云端 agent 只在带类型的占位符上规划；端侧 agent 提出需要遮挡的片段并把每步结果浓缩为要点；由确定性注册表完成替换与还原，使动作可直接在端侧执行。 | [paper](https://arxiv.org/abs/2605.08646v2) · 代码未定位 · [evidence](docs/evidence.md#2605-08646) |
| 2026-10-12 · v1 | **PrivacyGuard** — [PrivacyGuard: Source-Linked Sanitization and Locally Resolvable PII References for Cloud GUI Agents](https://arxiv.org/abs/2610.16778v1) | 云端 GUI agent 的端侧中介：对指令和截图中碎片化或形式变化的 PII 按完整来源范围改写，替换为会话级结构化引用；规划器可以使用这些引用，端侧在执行前于本地解析回真实值。 | [paper](https://arxiv.org/abs/2610.16778v1) · [code](https://github.com/betterzian/PrivacyGuard) · [evidence](docs/evidence.md#2610-16778) |
| 2026-09-26 · v1 | **PriCon** — [Ask Without Telling: Local SLMs Consult Cloud LLMs Without Revealing Task Intent](https://arxiv.org/abs/2609.32642v1) | 在本地 SLM 咨询云端 LLM 时隐藏任务意图，而不只是敏感数值：SLM 把任务改写成可还原的数学形式，必要时再包装成另一领域的语义替身，云端返回的指导或代码由本地映射回原任务。 | [paper](https://arxiv.org/abs/2609.32642v1) · 代码未定位 · [evidence](docs/evidence.md#2609-32642) |
| 2026-07-10 · v5 | **TMO** — [Device-Cloud Collaborative LLM Inference with Multi-Modal, Multi-Task, Multi-Turn Conversations](https://arxiv.org/abs/2502.11007v5) | 以资源约束 RL 联合选择推理位置与模态来源，提供 M4A1 数据集。 | [paper](https://arxiv.org/abs/2502.11007v5) · [code](https://github.com/liangqiyuan/TMO) · [evidence](docs/evidence.md#2502-11007) |
| 2026-05-29 · v2 | **MaskClaw** — [MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution](https://arxiv.org/abs/2605.28646v2) | GUI agent 的端侧隐私仲裁器：在截图离开可信环境之前提取本地屏幕证据、检索与用户身份和任务相关的策略规则，决定放行、遮挡或询问用户，并把用户的纠正转成经沙箱校验的隐私 skill。 | [paper](https://arxiv.org/abs/2605.28646v2) · [code](https://github.com/Theodora-Y/MaskClaw) · [evidence](docs/evidence.md#2605-28646) |
| 2026-04-26 · v3 | **Available but Invisible** — [Anonymization-Enhanced Privacy Protection for Mobile GUI Agents: Available but Invisible](https://arxiv.org/abs/2602.10139v3) | 在手机与云端 GUI agent 之间放一层本地中介：把指令、XML 和截图中检测到的 PII 替换为保留类型的占位符，在匿名化界面上代为执行 agent 的动作，需要原始值时只做范围受限的本地计算。 | [paper](https://arxiv.org/abs/2602.10139v3) · [code](https://github.com/one-step-beh1nd/gui_privacy_protection) · [evidence](docs/evidence.md#2602-10139) |
| 2025-10-17 · v1 | **CORE** — [CORE: Reducing UI Exposure in Mobile Agents via Collaboration Between Cloud and Local LLMs](https://arxiv.org/abs/2510.15455v1) | 在手机上按 XML 布局把屏幕划成语义块；本地 LLM 为每个块推测一个子任务，云端 LLM 从候选中选定当前子任务，再只在本地 LLM 排名靠前的块中选择目标元素。 | [paper](https://arxiv.org/abs/2510.15455v1) · [code](https://github.com/Entropy-Fighter/CORE) · [evidence](docs/evidence.md#2510-15455) |
| 2025-04-05 · v2 | **CAMP** — [Contextual Augmented Multi-Model Programming (CAMP): A Hybrid Local-Cloud Copilot Framework](https://arxiv.org/abs/2410.15285v2) | IDE 内的本地检索模块动态索引代码符号，为云端 LLM 组装带上下文的提示；实现为 Xcode 沙箱内的 Copilot for Xcode 插件。 | [paper](https://arxiv.org/abs/2410.15285v2) · [code](https://github.com/intitni/CopilotForXcode) · [evidence](docs/evidence.md#2410-15285) |

<a id="personalization"></a>

## 个性化与知识迁移

| 版本日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10-07 · v1 | **Skill-SLM** — [Skill-SLM: Agent Skill-driven Small Language Models for Reliable Robot Operation](https://arxiv.org/abs/2610.10812v1) | 离线用 GPT-5.5 归纳带 skill 的文法与 skill 库、合成任务分解与编排数据，再微调机载 SLM，使其在运行时无需调用云端即可分解机器人任务、组合 skill 生成操作代码。 | [paper](https://arxiv.org/abs/2610.10812v1) · 代码未定位 · [evidence](docs/evidence.md#2610-10812) |
| 2026-09-14 · v1 | **CIDERS** — [CIDERS: Cloud-Edge LLM Collaborative Learning via Accelerating Personalized Bilevel Optimization](https://arxiv.org/abs/2609.15664v1) | 以双层优化和共识校正连接云端 backbone 知识迁移与端侧 messenger 个性化。 | [paper](https://arxiv.org/abs/2609.15664v1) · 代码未定位 · [evidence](docs/evidence.md#2609-15664) |
| 2026-01-27 · v2 | **CDCDA-PLM** — [Towards On-Device Personalization: Cloud-device Collaborative Data Augmentation for Efficient On-device Language Model](https://arxiv.org/abs/2508.21313v2) | 云端扩增少量用户历史，生成个性化训练内容，支持端侧 PEFT 与后续本地推理。 | [paper](https://arxiv.org/abs/2508.21313v2) · 代码未定位 · [evidence](docs/evidence.md#2508-21313) |

<a id="training"></a>

## 协同训练与联邦优化

| 版本日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-04-14 · v1 | **pAirZero** — [Three Birds, One Stone: Solving the Communication-Memory-Privacy Trilemma in LLM Fine-tuning Over Wireless Networks with Zeroth-Order Optimization](https://arxiv.org/abs/2604.12401v1) | 结合零阶更新与 over-the-air 聚合，联合设计发射功率、噪声和隐私预算。 | [paper](https://arxiv.org/abs/2604.12401v1) · 代码未定位 · [evidence](docs/evidence.md#2604-12401) |
| 2026-02-03 · v1 | **FedKRSO** — [FedKRSO: Communication and Memory Efficient Federated Fine-Tuning of Large Language Models](https://arxiv.org/abs/2602.03019v1) | 共享随机子空间，聚合低维更新累积量；使用 first-order projected gradient。 | [paper](https://arxiv.org/abs/2602.03019v1) · 代码未定位 · [evidence](docs/evidence.md#2602-03019) |
| 2025-02-27 · v1 | **MobiLLM** — [MobiLLM: Enabling LLM Fine-Tuning on the Mobile Device via Server Assisted Side Tuning](https://arxiv.org/abs/2502.20421v1) | 端侧保留 frozen backbone，单向传输量化 activation，由云端完成 side-network 反向传播。 | [paper](https://arxiv.org/abs/2502.20421v1) · 代码未定位 · [evidence](docs/evidence.md#2502-20421) |
| 2024-05-27 · v5 | **FedKSeed** — [Federated Full-Parameter Tuning of Billion-Sized Language Models with Communication Cost under 18 Kilobytes](https://arxiv.org/abs/2312.06353v5) | 通过零阶优化、有限 seed 池与标量梯度通信，实现联邦全参数微调。 | [paper](https://arxiv.org/abs/2312.06353v5) · [code](https://github.com/alibaba/FederatedScope/tree/FedKSeed) · [evidence](docs/evidence.md#2312-06353) |

<a id="decoding"></a>

## Token 级协同解码

| 版本日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10-06 · v1 | **DySCo** — [DySCo: Dynamic Sharding for Collaborative Edge-Cloud LLM Inference with Depth-Synchronized Batching](https://arxiv.org/abs/2610.08268v1) | 按会话在某一层把同一个 LLM 切成端侧前缀和云端后缀，KV cache 留在各自的 shard 上；不同切分深度的会话先推进到最深的切点，再对共同的后缀层做批处理。 | [paper](https://arxiv.org/abs/2610.08268v1) · [code](https://github.com/Large-scale-Sustainable-Computing-LSC/dysco-artifact) · [evidence](docs/evidence.md#2610-08268) |
| 2026-09-05 · v2 | **Speculation at a Distance** — [Speculation at a Distance: Where Edge-Cloud Speculative Decoding Actually Pays Off](https://arxiv.org/abs/2606.25091v2) | 分析 RTT 约束下分布式 speculative decoding 的适用区间，强调多租户云端容量。 | [paper](https://arxiv.org/abs/2606.25091v2) · 代码未定位 · [evidence](docs/evidence.md#2606-25091) |
| 2026-09-02 · v1 | **AceSpec** — [AceSpec: An Asymmetric Edge-Cloud Collaborative Framework for Communication-Efficient LLM Inference](https://arxiv.org/abs/2609.02514v1) | 预先构造本地恢复分支，用上行索引与下行稀疏分布优化 speculative decoding 通信。 | [paper](https://arxiv.org/abs/2609.02514v1) · 代码未定位 · [evidence](docs/evidence.md#2609-02514) |

<a id="embodied"></a>

## 具身与机器人端云协同

| 版本日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10-02 · v2 | **Communication-Aware Robot Execution** — [Communication-Aware Robot Execution for Cloud Inference under Spatially Heterogeneous Connectivity](https://arxiv.org/abs/2606.31497v2) | 把机器人在哪里发出下一次云端请求当作运动决策：估计一次请求—响应所需的时间窗，借助通信地图在执行当前云端生成的动作原语的同时驶向信号良好的请求点。 | [paper](https://arxiv.org/abs/2606.31497v2) · 代码未定位 · [evidence](docs/evidence.md#2606-31497) |
| 2026-09-21 · v1 | **Cloud, Edge, or Split?** — [Cloud, Edge, or Split? Profiling Onboard and Split Vision-Language Model Deployment for Drone AI](https://arxiv.org/abs/2609.25415v1) | 对 SmolVLM-256M 在无人机巡检中的全机载、全云端和拆分三种部署做性能剖析，拆分方案上传投影后的视觉 token 而非 JPEG 图像；结论是最优部署取决于网络条件和图像分辨率。 | [paper](https://arxiv.org/abs/2609.25415v1) · 代码未定位 · [evidence](docs/evidence.md#2609-25415) |
| 2026-09-16 · v3 | **CloudEdgeVLA** — [Latency-Tolerant Cloud-Edge Collaborative Vision-Language-Action Models via Emergent Representational Specialization](https://arxiv.org/abs/2608.00569v3) | 把 VLA 策略拆开：云端 VLA 把可能延迟的观测编码成变化缓慢的任务特征，端侧轻量动作头把最近收到的特征与当前本地视觉融合；训练时用新鲜帧与随机延迟帧配对同一动作目标，机器人从不阻塞等待云端。 | [paper](https://arxiv.org/abs/2608.00569v3) · 代码未定位 · [evidence](docs/evidence.md#2608-00569) |
| 2026-09-07 · v1 | **ComVLA** — [ComVLA: Communication-Aware Split Inference for VLA Models in 6G-Connected Robotics](https://arxiv.org/abs/2609.07838v1) | 在机器人端用语言到视觉的交叉注意力为视觉 token 打分，只把无线信道容量允许数量的高分 token 传给云端 VLA。 | [paper](https://arxiv.org/abs/2609.07838v1) · 代码未定位 · [evidence](docs/evidence.md#2609-07838) |
| 2026-08-16 · v1 | **EcoVLA** — [EcoVLA: Energy-Efficient Device-Edge Co-Inference for Vision-Language-Action Models under Real-Time Constraints](https://arxiv.org/abs/2608.15502v1) | 为自回归和扩散式 VLA 构建与范式无关的端—边协同推理运行时，借助延迟和能耗预测器调度机器人与边缘服务器之间的分阶段映射，在 20 Hz 输出约束下最大化每焦耳动作数。 | [paper](https://arxiv.org/abs/2608.15502v1) · 代码未定位 · [evidence](docs/evidence.md#2608-15502) |
| 2026-04-27 · v2 | **RoboECC** — [RoboECC: Multi-Factor-Aware Edge-Cloud Collaborative Deployment for VLA Models](https://arxiv.org/abs/2603.20711v2) | 依据 VLA 的编码器、LLM 主干和动作解码器结构建模并结合硬件画像寻找切分点，再随网络带宽波动调整部署。 | [paper](https://arxiv.org/abs/2603.20711v2) · 代码未定位 · [evidence](docs/evidence.md#2603-20711) |
| 2026-03-12 · v2 | **RAPID** — [RAPID: Redundancy-Aware and Compatibility-Optimal Edge-Cloud Partitioned Inference for Diverse VLA Models](https://arxiv.org/abs/2603.07949v2) | 在机器人与云端之间切分 VLA 推理，并依据运动学决定何时调用云端：在高频本体感知回路中监测关节加速度与冗余度，只在高重要性阶段触发云端推理并中止过时的缓存动作块。 | [paper](https://arxiv.org/abs/2603.07949v2) · 代码未定位 · [evidence](docs/evidence.md#2603-07949) |
| 2026-03-06 · v1 | **Knowledge-Driven Mobile Agentic AI** — [Knowledge-driven Reasoning for Mobile Agentic AI: Concepts, Approaches, and Directions](https://arxiv.org/abs/2603.05831v1) | 提出把历史任务中可复用的决策结构提炼成由结构化、检索型和流程型知识组成的紧凑知识包，经带宽受限链路同步后注入机载推理，使中断后的重规划不必回到云端。 | [paper](https://arxiv.org/abs/2603.05831v1) · 代码未定位 · [evidence](docs/evidence.md#2603-05831) |
| 2024-08-19 · v1 | **EC-Drive** — [Edge-Cloud Collaborative Motion Planning for Autonomous Driving with Large Language Models](https://arxiv.org/abs/2408.09972v1) | 在车端运行小型 LLM 做运动规划，用数据漂移检测只把新障碍物、交通模式变化或低置信度样本上传给云端 GPT-4。 | [paper](https://arxiv.org/abs/2408.09972v1) · 代码未定位 · [evidence](docs/evidence.md#2408-09972) |

<a id="adjacent"></a>

## 邻近工作与迁移机会

以下工作提供可迁移思路，但不能当作已验证的 LLM/Agent 端云协同方法。

| 版本日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10-06 · v1 | **HintKD** — [HintKD: Hint Knowledge Distillation for Bandwidth-Constrained Cloud-Edge Inference](https://arxiv.org/abs/2610.08412v1) | 将 teacher 指导编码为 codebook 索引，由 student 的 FiLM adapter 解释。 | [paper](https://arxiv.org/abs/2610.08412v1) · 代码未定位 · [evidence](docs/evidence.md#2610-08412) |
| 2026-07-21 · v1 | **Broken Gates** — [Broken Gates: Re-evaluating Web Bot Defenses in the Age of LLM Agents](https://arxiv.org/abs/2607.18659v1) | 测量商业验证码破解服务和六个 LLM 浏览器 agent 在云端托管、自托管、AI 浏览器与浏览器扩展四种部署下对抗 hCaptcha、reCAPTCHA v2/v3 和 Turnstile 的表现；只有浏览器扩展形态的 agent 能稳定以可接受的信任分通过 reCAPTCHA v3，作者把差异归因于执行环境的真实性而非行为。 | [paper](https://arxiv.org/abs/2607.18659v1) · 代码未定位 · [evidence](docs/evidence.md#2607-18659) |
| 2026-06-29 · v1 | **Unmasking Web Agents** — [On the Internet, Nobody Knows You're an LLM Bot: Unmasking Web Agents with Multi-Layer Fingerprinting](https://arxiv.org/abs/2606.30119v1) | 部署受 robots.txt、验证码、工作量证明和 Cloudflare 保护的蜜罐网站，用网络、HTTP 和浏览器三层指纹表明，六个云端或本地运行的 LLM Web agent 都能与人类及彼此区分，数据中心 IP 仍是重要信号。 | [paper](https://arxiv.org/abs/2606.30119v1) · 代码未定位 · [evidence](docs/evidence.md#2606-30119) |
| 2026-05-02 · v1 | **FP-Agent** — [FP-Agent: Fingerprinting AI Browsing Agents](https://arxiv.org/abs/2605.01247v1) | 在受控蜜罐网站上测量七个 AI 浏览 agent 与人类用户：多个 agent 共用浏览器指纹时区分度有限，而打字、滚动和鼠标等行为指纹区分度高；分类器能识别全部七个 agent，Cloudflare 只识别出一个。 | [paper](https://arxiv.org/abs/2605.01247v1) · 代码未定位 · [evidence](docs/evidence.md#2605-01247) |
| 2026-03-19 · v1 | **Speculative Policy Orchestration** — [Speculative Policy Orchestration: A Latency-Resilient Framework for Cloud-Robotic Manipulation](https://arxiv.org/abs/2603.19418v1) | 云端世界模型预先计算未来路径点并流式发送到端侧缓冲区，使控制频率与往返时延解耦；端侧用 ε-tube 校验器限制运动误差，并自适应调整预取深度。 | [paper](https://arxiv.org/abs/2603.19418v1) · 代码未定位 · [evidence](docs/evidence.md#2603-19418) |
| 2026-03-17 · v1 | **POaaS** — [POaaS: Minimal-Edit Prompt Optimization as a Service to Lift Accuracy and Cut Hallucinations on On-Device sLLMs](https://arxiv.org/abs/2603.16045v1) | 在语义漂移与长度约束下，保守地纠错、改写和补充事实，优化 prompt。 | [paper](https://arxiv.org/abs/2603.16045v1) · 代码未定位 · [evidence](docs/evidence.md#2603-16045) |

## 相关资源

- [Awesome-Gradient-Free-LLMOpt](https://github.com/zz1358m/Awesome-Gradient-Free-LLMOpt) — ES/ZO 参数优化的配套阅读清单，也是本仓库组织形式的参考。

## 维护

修改 `data/papers.json` 后运行 `python scripts/render.py`；提交前运行 `python scripts/render.py --check`。欢迎通过 Issue/PR 补充论文、作者代码、版本更新和设备实测信息。文献元数据与来源按条记录，研究建议单独存放。

本仓库采用 [MIT License](LICENSE)；所链接论文、代码和数据集保留各自许可。
