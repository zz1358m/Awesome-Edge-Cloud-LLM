# Evaluation evidence / 实验依据与边界

The notes below summarize checked paper pages; they are not independent reproductions. Missing measurements are not inferred. / 以下摘要来自核验的论文页面，不是独立复现；缺失的测量不作推断。

<a id="2609-16008"></a>

## Co-Skill

- **Version:** 2026-09-17, v2; first submitted 2026-08-01.
- **Status:** preprint.
- **Exchange:** Trajectory trie / skill tree. / 轨迹 trie / skill tree。
- **Evidence:** Server GPU emulation (A800); ALFWorld and WebShop; RL is optional and disabled by default.
- **实验边界：** A800 上模拟端侧；ALFWorld、WebShop；默认关闭 RL，可选做能力内化。
- **Sources:** [metadata](https://arxiv.org/abs/2609.16008v2), [full text](https://arxiv.org/html/2609.16008v2). Checked 2026-10-09.

<a id="2505-05440"></a>

## EcoAgent

- **Version:** 2025-11-17, v3; first submitted 2025-05-08.
- **Status:** AAAI 2026 (author-reported).
- **Exchange:** Plans / screen summaries / feedback. / 计划 / 屏幕摘要 / 反馈。
- **Evidence:** AndroidWorld evaluation; mobile automation benchmark evidence does not establish phone energy savings.
- **实验边界：** AndroidWorld 评估；移动自动化基准结果不等于手机能耗收益。
- **Sources:** [metadata](https://arxiv.org/abs/2505.05440v3), [full text](https://arxiv.org/html/2505.05440v3). Checked 2026-10-09.

<a id="2605-24598"></a>

## Hera

- **Version:** 2026-05-23, v1; first submitted 2026-05-23.
- **Status:** preprint.
- **Exchange:** Step state / selected agent action. / step 状态 / 被选 agent 的动作。
- **Evidence:** RTX 4090 deployment evaluation; ALFWorld, WebShop, AppWorld; relative cloud-only success is not absolute success.
- **实验边界：** RTX 4090 部署评估；ALFWorld、WebShop、AppWorld；相对 cloud-only 成功率不能当作绝对成功率。
- **Sources:** [metadata](https://arxiv.org/abs/2605.24598v1), [full text](https://arxiv.org/html/2605.24598v1). Checked 2026-10-09.

<a id="2509-24050"></a>

## GAPG

- **Version:** 2026-05-23, v4; first submitted 2025-09-28.
- **Status:** preprint.
- **Exchange:** Reasoning / call-for-help. / 推理 / 求助请求。
- **Evidence:** Reasoning benchmarks with on-device-scale models; model size alone does not establish real-device feasibility.
- **实验边界：** 使用端侧规模模型做推理基准评估；模型大小本身不能证明真实设备可行性。
- **Sources:** [metadata](https://arxiv.org/abs/2509.24050v4), [full text](https://arxiv.org/html/2509.24050v4). Checked 2026-10-09.

<a id="2502-11007"></a>

## TMO

- **Version:** 2026-07-10, v5; first submitted 2025-02-16.
- **Status:** MobiHoc 2025; extended journal version (arXiv comments).
- **Exchange:** Selected multimodal context / responses. / 筛选后的多模态上下文 / 响应。
- **Evidence:** Offline archived responses, LLM-as-judge quality, and nearest-neighbor estimation of uncertain state-action quality.
- **实验边界：** 依赖离线响应档案、LLM-as-judge 和 nearest-neighbor 质量估计，迁移时需验证真实 outcome。
- **Sources:** [metadata](https://arxiv.org/abs/2502.11007v5), [full text](https://arxiv.org/html/2502.11007v5). Checked 2026-10-09.

<a id="2609-15664"></a>

## CIDERS

- **Version:** 2026-09-14, v1; first submitted 2026-09-14.
- **Status:** preprint.
- **Exchange:** Messenger / consensus state / backbone updates. / messenger / 共识状态 / backbone 更新。
- **Evidence:** No common-hardware end-to-end runtime, peak memory, or full traffic measurements; counted recurring payload is about twice one-messenger baselines.
- **实验边界：** 未在共同硬件测量完整 runtime、峰值内存和全流量；已计周期载荷约为单 messenger 基线两倍。
- **Sources:** [metadata](https://arxiv.org/abs/2609.15664v1), [full text](https://arxiv.org/html/2609.15664v1). Checked 2026-10-09.

<a id="2508-21313"></a>

## CDCDA-PLM

- **Version:** 2026-01-27, v2; first submitted 2025-08-29.
- **Status:** preprint.
- **Exchange:** User history / synthetic training examples. / 用户历史 / 合成训练样本。
- **Evidence:** Personalization benchmarks; local inference does not imply that user data stayed local during augmentation.
- **实验边界：** 个性化基准；后续本地推理不代表数据增强阶段用户数据始终留在本地。
- **Sources:** [metadata](https://arxiv.org/abs/2508.21313v2), [full text](https://arxiv.org/html/2508.21313v2). Checked 2026-10-09.

<a id="2502-20421"></a>

## MobiLLM

- **Version:** 2025-02-27, v1; first submitted 2025-02-27.
- **Status:** preprint.
- **Exchange:** Quantized activations. / 量化 activation。
- **Evidence:** Jetson Xavier NX and CPU-only Huawei Matebook with an A100 server over Wi-Fi; these are not smartphone measurements.
- **实验边界：** Jetson Xavier NX、纯 CPU 华为 Matebook 与 A100 云端，经 Wi-Fi 协作；不是智能手机实测。
- **Sources:** [metadata](https://arxiv.org/abs/2502.20421v1), [full text](https://arxiv.org/html/2502.20421v1). Checked 2026-10-09.

<a id="2602-03019"></a>

## FedKRSO

- **Version:** 2026-02-03, v1; first submitted 2026-02-03.
- **Status:** INFOCOM 2026 (author-reported).
- **Exchange:** Seeds / subspace update accumulators. / seed / 子空间更新累积量。
- **Evidence:** GLUE federated experiments; seed-based communication should not be labeled forward-only optimization.
- **实验边界：** GLUE 联邦实验；基于 seed 的通信不能归类为 forward-only 优化。
- **Sources:** [metadata](https://arxiv.org/abs/2602.03019v1), [full text](https://arxiv.org/html/2602.03019v1). Checked 2026-10-09.

<a id="2604-12401"></a>

## pAirZero

- **Version:** 2026-04-14, v1; first submitted 2026-04-14.
- **Status:** preprint.
- **Exchange:** ZO scalar / sign signals over wireless aggregation. / 无线聚合的 ZO scalar / sign 信号。
- **Evidence:** A100-based simulation with OPT-125M and five clients on SST-2/SQuAD; no demonstrated phone agent adaptation.
- **实验边界：** A100 仿真；OPT-125M、5 个客户端、SST-2/SQuAD；尚未验证手机 agent 适配。
- **Sources:** [metadata](https://arxiv.org/abs/2604.12401v1), [full text](https://arxiv.org/html/2604.12401v1). Checked 2026-10-09.

<a id="2312-06353"></a>

## FedKSeed

- **Version:** 2024-05-27, v5; first submitted 2023-12-11.
- **Status:** ICML 2024 (author-reported).
- **Exchange:** Finite random seeds / scalar gradients. / 有限随机 seed / 标量梯度。
- **Evidence:** Foundational communication baseline; compact payload alone does not measure total evaluation compute or device energy.
- **实验边界：** 低通信量基础基线；紧凑载荷本身不能衡量总评估计算量或端侧能耗。
- **Sources:** [metadata](https://arxiv.org/abs/2312.06353v5), [full text](https://arxiv.org/html/2312.06353v5). Checked 2026-10-09.

<a id="2609-02514"></a>

## AceSpec

- **Version:** 2026-09-02, v1; first submitted 2026-09-02.
- **Status:** preprint.
- **Exchange:** Draft indices / sparse verification distributions. / draft 索引 / 稀疏验证分布。
- **Evidence:** Jetson AGX Orin 32GB + 4 x A100 40GB, with tc-shaped WAN; embedded hardware is real, network conditions are emulated.
- **实验边界：** Jetson AGX Orin 32GB + 4 x A100 40GB，tc 注入 WAN 条件；硬件真实，网络条件模拟。
- **Sources:** [metadata](https://arxiv.org/abs/2609.02514v1), [full text](https://arxiv.org/html/2609.02514v1). Checked 2026-10-09.

<a id="2606-25091"></a>

## Speculation at a Distance

- **Version:** 2026-09-05, v2; first submitted 2026-06-23.
- **Status:** preprint.
- **Exchange:** Draft / verification protocol. / draft / 验证协议。
- **Evidence:** Systems analysis; compare against co-located speculation and separate single-request latency from server throughput.
- **实验边界：** 系统分析；应对照共置 speculation，并区分单请求延迟与服务器吞吐。
- **Sources:** [metadata](https://arxiv.org/abs/2606.25091v2), [full text](https://arxiv.org/html/2606.25091v2). Checked 2026-10-09.

<a id="2603-16045"></a>

## POaaS

- **Version:** 2026-03-17, v1; first submitted 2026-03-17.
- **Status:** FEVER 2026 (author-reported).
- **Exchange:** Rewritten prompt. / 改写 prompt。
- **Evidence:** Same 3B/8B model acts as optimizer and solver; adjacent on-device work, not a validated strong-cloud collaboration method.
- **实验边界：** 同一 3B/8B 模型担任 optimizer 与 solver；属于端侧邻近工作，未验证强云端协同。
- **Sources:** [metadata](https://arxiv.org/abs/2603.16045v1), [full text](https://arxiv.org/html/2603.16045v1). Checked 2026-10-09.

<a id="2610-08412"></a>

## HintKD

- **Version:** 2026-10-06, v1; first submitted 2026-10-06.
- **Status:** preprint.
- **Exchange:** Discrete hint index. / 离散 hint 索引。
- **Evidence:** DeepSense 6G beam prediction and MNIST; transferring the idea to LLMs or agents remains a research hypothesis.
- **实验边界：** DeepSense 6G 波束预测、MNIST；迁移至 LLM/agent 仍是研究假设。
- **Sources:** [metadata](https://arxiv.org/abs/2610.08412v1), [full text](https://arxiv.org/html/2610.08412v1). Checked 2026-10-09.

<a id="2510-22009"></a>

## OpenPhone

- **Version:** 2026-10-05, v3; first submitted 2025-10-24.
- **Status:** preprint.
- **Exchange:** GUI state and execution history / cloud agent actions after the switch. / GUI 状态与执行历史 / 切换后云端 agent 的动作。
- **Evidence:** AndroidLab online evaluation plus 25 custom tasks on four apps; model latency is measured with vLLM on one or two RTX 3090 GPUs, not on phones; in the collaboration analysis the cloud still performs about 65% of steps.
- **实验边界：** AndroidLab 在线评测，另加四个 app 的 25 个自建任务；模型延迟用 vLLM 在一张或两张 RTX 3090 上测量，不是手机实测；协同分析中云端仍执行约 65% 的步骤。
- **Sources:** [metadata](https://arxiv.org/abs/2510.22009v3), [full text](https://arxiv.org/html/2510.22009v3). Checked 2026-10-12.

<a id="2610-08268"></a>

## DySCo

- **Version:** 2026-10-06, v1; first submitted 2026-10-06.
- **Status:** preprint.
- **Exchange:** Cut-layer hidden states / next-token IDs. / 切分层的 hidden state / 下一个 token ID。
- **Evidence:** Single-edge runs pair a Jetson Orin (8 GB, over WAN) or datacenter GPUs with an RTX A6000 cloud; the multi-edge batching study runs all edge and cloud processes on one multi-GPU server, so it isolates scheduling from wide-area network variation.
- **实验边界：** 单端实验用 Jetson Orin（8 GB，经 WAN）或数据中心 GPU 搭配 RTX A6000 云端；多端批处理实验的端侧和云端进程都跑在同一台多 GPU 服务器上，只隔离出调度行为，不含广域网波动。
- **Sources:** [metadata](https://arxiv.org/abs/2610.08268v1), [full text](https://arxiv.org/html/2610.08268v1). Checked 2026-10-12.

