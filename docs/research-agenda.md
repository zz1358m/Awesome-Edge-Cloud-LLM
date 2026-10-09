# Research agenda / 研究问题

These are curator proposals, not established results or claims of novelty. / 以下是研究设想，不是已验证结论，也不构成新颖性声明。

## A. Budget-aware skill compilation / 面向预算的 skill 编译

Given an edge model, a few capability probes, and a device budget, choose the structure, detail, examples, and loading policy of cloud-generated guidance. Measure whether the compilation cost is recovered across subsequent tasks.

输入端侧模型、少量能力 probing 和设备预算，决定保留哪些规则、展开哪些步骤、增加哪些例子、按需加载哪个子结构。核心对照是 [Co-Skill](https://arxiv.org/abs/2609.16008v2)，进一步需要验证跨模型、量化配置与真实设备收益。

An illustrative objective / 示例目标：

$$
S^* = \arg\max_S \left[\mathbb{E}[R\mid M_{edge},S]-\lambda C_{local}(S)-\mu C_{compile}(S)\right].
$$

Count local prefill, execution, energy, cloud generation, verification, and delivery. A graph or tree representation needs measurable benefits in execution or resource use.

## B. Jointly choosing intervention time and content / 联合选择求助时机与内容

Extend the decision beyond local/cloud to local execution, hint, subplan, reusable skill patch, or cloud takeover. Optimize final outcome and cumulative collaboration cost, including reuse across future tasks.

将决策扩展为本地执行、hint、subplan、skill patch、云端接管。关注帮助内容对后续轨迹和后续任务的价值。相关基础包括 [Hera](https://arxiv.org/abs/2605.24598v1)、[EcoAgent](https://arxiv.org/abs/2505.05440v3) 与 [Co-Skill](https://arxiv.org/abs/2609.16008v2)。

## C. Local outcome-driven forward-only adaptation / 本地 outcome 驱动的 forward-only 适配

Let the cloud organize proposals and aggregation while devices evaluate candidates on local tasks. Study reliable feedback under heterogeneous hardware, quantization, local distributions, and limited evaluation budgets.

云端维护搜索状态，端侧用本地任务评估候选并上传紧凑反馈。需要明确候选间如何使用可比评估 batch、如何分层聚合不同用户，以及如何控制 rollout 成本。

Use [FedKSeed](https://arxiv.org/abs/2312.06353v5) and [pAirZero](https://arxiv.org/abs/2604.12401v1) as seed/scalar and ZO references; [FedKRSO](https://arxiv.org/abs/2602.03019v1) supplies a first-order subspace comparison. Seed communication alone is already established and should not be presented as the new contribution.

## Evaluation / 评估口径

| Question / 问题 | Measurement / 测量 |
| --- | --- |
| Outcome at equal budget / 同预算效果 | End-task success, accuracy, or reward; matched total budget |
| Cost at equal outcome / 同效果成本 | Full forward count, latency, peak memory, bytes, energy, cloud bill |
| Amortization / 成本摊销 | Number of future tasks needed to recover compilation or adaptation cost |
| Device realism / 设备真实性 | Hardware, quantization, model placement, power measurement, network RTT/bandwidth |
| Decoding trade-off / 解码取舍 | Per-request latency and multi-tenant throughput measured separately |

Include cloud analysis, edge prefill, extra rollouts, network transfer, and model update costs. Report raw outcomes and denominators alongside relative improvements. LLM-as-judge scores and task success are different quantities. Simulation and hardware measurements should carry separate labels.
