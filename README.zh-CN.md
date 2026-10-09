# Awesome Edge–Cloud LLM & Agent Collaboration

[English](README.md) | **简体中文**

收集 **LLM/Agent 端云协同** 的论文、代码与数据集，按“优化什么”分类，重点关注端云之间交换什么，以及这些内容如何转化为端侧可复用能力。

**范围截至 2026-10-09 · 15 篇 · 13 篇核心工作 + 2 篇邻近工作。** 日期为所链接 arXiv 版本日期，首次提交日期另存于数据文件。本文献清单不是穷尽性综述，也不是统一性能排行榜。

多数近期工作为 preprint；录用信息采用作者在 arXiv/项目页的报告。代码仅收录论文关联的作者链接；“未定位”不等于不存在。收益以作者实验为准，真实设备、服务器模拟和无线仿真应分别理解。

## 导航

- [Skill、计划与轨迹协同](#skills)
- [路由与求助决策](#routing)
- [上下文与模态选择](#context)
- [个性化与知识迁移](#personalization)
- [协同训练与联邦优化](#training)
- [Token 级协同解码](#decoding)
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

分类是主入口，论文可以跨多个优化对象；例如 Co-Skill 同时涉及上传轨迹和下发指导。

## 建议阅读顺序

- 内容与 skill：**Co-Skill → EcoAgent → TMO**。
- 长程 agent 路由：**Hera → GAPG**。
- 个性化：**CIDERS → CDCDA-PLM**。
- Forward-only 训练：**FedKSeed → pAirZero**，以 **FedKRSO** 作一阶子空间对照。
- 解码系统：**AceSpec → Speculation at a Distance**，同时检查延迟与吞吐。

<a id="skills"></a>

## Skill、计划与轨迹协同

| 版本日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-09-17 · v2 | **Co-Skill** — [Co-Skill: A Collaborative Communication Framework for Skill Evolution](https://arxiv.org/abs/2609.16008v2) | 合并上传轨迹的公共前缀，并按端侧执行失败逐步细化下发的 skill tree。 | [paper](https://arxiv.org/abs/2609.16008v2) · 代码未定位 · [evidence](docs/evidence.md#2609-16008) |
| 2025-11-17 · v3 | **EcoAgent** — [EcoAgent: An Efficient Device-Cloud Collaborative Multi-Agent Framework for Mobile Automation](https://arxiv.org/abs/2505.05440v3) | 云端规划，端侧观察与验证，上传简洁屏幕摘要，用反馈闭环触发调整。 | [paper](https://arxiv.org/abs/2505.05440v3) · [code](https://github.com/Yi-Biao/EcoAgent) · [evidence](docs/evidence.md#2505-05440) |

<a id="routing"></a>

## 路由与求助决策

| 版本日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-05-23 · v1 | **Hera** — [Hera: Learning Long-Horizon Coordination for Device-Cloud Collaborative LLM Agents](https://arxiv.org/abs/2605.24598v1) | 外部协调器先模仿学习，再以长程任务结果与云调用成本做 RL，逐步选择端或云。 | [paper](https://arxiv.org/abs/2605.24598v1) · 代码未定位 · [evidence](docs/evidence.md#2605-24598) |
| 2026-05-23 · v4 | **GAPG** — [Bridging On-Device and Cloud LLMs for Collaborative Reasoning: A Unified Methodology for Local Routing and Post-Training](https://arxiv.org/abs/2509.24050v4) | 通过自适应策略梯度联合训练端侧推理与内部求助决策。 | [paper](https://arxiv.org/abs/2509.24050v4) · 代码未定位 · [evidence](docs/evidence.md#2509-24050) |

<a id="context"></a>

## 上下文与模态选择

| 版本日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-07-10 · v5 | **TMO** — [Device-Cloud Collaborative LLM Inference with Multi-Modal, Multi-Task, Multi-Turn Conversations](https://arxiv.org/abs/2502.11007v5) | 以资源约束 RL 联合选择推理位置与模态来源，提供 M4A1 数据集。 | [paper](https://arxiv.org/abs/2502.11007v5) · [code](https://github.com/liangqiyuan/TMO) · [evidence](docs/evidence.md#2502-11007) |

<a id="personalization"></a>

## 个性化与知识迁移

| 版本日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
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
| 2026-09-05 · v2 | **Speculation at a Distance** — [Speculation at a Distance: Where Edge-Cloud Speculative Decoding Actually Pays Off](https://arxiv.org/abs/2606.25091v2) | 分析 RTT 约束下分布式 speculative decoding 的适用区间，强调多租户云端容量。 | [paper](https://arxiv.org/abs/2606.25091v2) · 代码未定位 · [evidence](docs/evidence.md#2606-25091) |
| 2026-09-02 · v1 | **AceSpec** — [AceSpec: An Asymmetric Edge-Cloud Collaborative Framework for Communication-Efficient LLM Inference](https://arxiv.org/abs/2609.02514v1) | 预先构造本地恢复分支，用上行索引与下行稀疏分布优化 speculative decoding 通信。 | [paper](https://arxiv.org/abs/2609.02514v1) · 代码未定位 · [evidence](docs/evidence.md#2609-02514) |

<a id="adjacent"></a>

## 邻近工作与迁移机会

以下工作提供可迁移思路，但不能当作已验证的 LLM/Agent 端云协同方法。

| 版本日期 | 工作 | 贡献 | 资源 |
| --- | --- | --- | --- |
| 2026-10-06 · v1 | **HintKD** — [HintKD: Hint Knowledge Distillation for Bandwidth-Constrained Cloud-Edge Inference](https://arxiv.org/abs/2610.08412v1) | 将 teacher 指导编码为 codebook 索引，由 student 的 FiLM adapter 解释。 | [paper](https://arxiv.org/abs/2610.08412v1) · 代码未定位 · [evidence](docs/evidence.md#2610-08412) |
| 2026-03-17 · v1 | **POaaS** — [POaaS: Minimal-Edit Prompt Optimization as a Service to Lift Accuracy and Cut Hallucinations on On-Device sLLMs](https://arxiv.org/abs/2603.16045v1) | 在语义漂移与长度约束下，保守地纠错、改写和补充事实，优化 prompt。 | [paper](https://arxiv.org/abs/2603.16045v1) · 代码未定位 · [evidence](docs/evidence.md#2603-16045) |

## 相关资源

- [Awesome-Gradient-Free-LLMOpt](https://github.com/zz1358m/Awesome-Gradient-Free-LLMOpt) — ES/ZO 参数优化的配套阅读清单，也是本仓库组织形式的参考。

## 维护

修改 `data/papers.json` 后运行 `python scripts/render.py`；提交前运行 `python scripts/render.py --check`。欢迎通过 Issue/PR 补充论文、作者代码、版本更新和设备实测信息。文献元数据与来源按条记录，研究建议单独存放。

本仓库采用 [MIT License](LICENSE)；所链接论文、代码和数据集保留各自许可。
