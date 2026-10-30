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

<a id="2610-17560"></a>

## EdgeWise

- **Version:** 2026-10-13, v1; first submitted 2026-10-13.
- **Status:** preprint; ICLR 2027 submission under review ([OpenReview](https://openreview.net/forum?id=w1bB3nAhvd)).
- **Exchange:** Trajectory history (full or trimmed) for a delegated step / the cloud LLM's analysis and action for that step. / 被委托步骤所需的轨迹历史（完整或裁剪）/ 云端 LLM 为该步生成的分析与动作。
- **Evidence:** Terminal-Bench 2.1 and SWE-ReBench with Qwen3.5-9B as the SLM and API-served frontier models as the cloud LLM; the main runs serve the SLM on A100 GPUs, and a separate deployment runs the self-delegation model on one NVIDIA DGX Spark calling a cloud API; reported cost is API cost, not device energy.
- **实验边界：** 在 Terminal-Bench 2.1 和 SWE-ReBench 上评测，SLM 为 Qwen3.5-9B，云端 LLM 为 API 调用的前沿模型；主实验的 SLM 跑在 A100 上，另有一组部署实验把自委托模型放在单台 NVIDIA DGX Spark 上调用云端 API；报告的成本是 API 费用，不含设备能耗。
- **Sources:** [metadata](https://arxiv.org/abs/2610.17560v1), [full text](https://arxiv.org/html/2610.17560v1). Checked 2026-10-15.

<a id="2610-17816"></a>

## EC2-Bench

- **Version:** 2026-10-13, v1; first submitted 2026-10-13.
- **Status:** preprint; ICLR 2027 submission under review ([OpenReview](https://openreview.net/forum?id=xUfOKMx2hz)).
- **Exchange:** Task instruction and execution history visible to the cloud / cloud-generated actions (delegation) or plans and suggestions (advisory). / 云端可见的任务指令与执行历史 / 云端生成的动作（委托）或计划与建议（咨询）。
- **Evidence:** All configurations run in the OpenClaw runtime with Qwen3.5-2B/9B as current edge models, Qwen3.5-27B and Qwen3.7-Plus as proxies for stronger future edge models, and GLM-5.3 as the main cloud model; edge cost is estimated in FLOPs rather than measured on devices, and privacy exposure is judged by an LLM checked against 200 human labels.
- **实验边界：** 全部配置在 OpenClaw 运行时中执行，端侧用 Qwen3.5-2B/9B 代表当前模型、Qwen3.5-27B 与 Qwen3.7-Plus 作为未来更强端侧模型的代理，云端主要用 GLM-5.3；端侧开销以 FLOPs 估算而非设备实测，隐私暴露由 LLM 判定，并用 200 条人工标注做了核对。
- **Sources:** [metadata](https://arxiv.org/abs/2610.17816v1), [full text](https://arxiv.org/html/2610.17816v1). Checked 2026-10-15.

<a id="2604-17827"></a>

## Local-First Intelligence

- **Version:** 2026-10-10, v2; first submitted 2026-04-20.
- **Status:** preprint; ICLR 2027 submission under review ([OpenReview](https://openreview.net/forum?id=mo3S2ihVAe)).
- **Exchange:** SLM-formulated information requests meant to omit private user details / LLM answers or clarification requests. / SLM 构造的、力求不含用户隐私的信息请求 / LLM 的回答或澄清请求。
- **Evidence:** PrivQA built from six QA datasets plus zero-shot PUPA, AESLC, and SAMSum; SLMs are Qwen3-4B/8B and Llama 3B/8B, cloud LLMs include DeepSeek-R1-Distill-Llama-70B, Qwen3-235B-A22B, and Qwen3-Max; training uses 8×H20 GPUs, and latency is measured with Qwen3-8B on one RTX 4090 against a cloud API, not on a phone.
- **实验边界：** PrivQA 由六个 QA 数据集构造，另在 PUPA、AESLC、SAMSum 上零样本评测；SLM 为 Qwen3-4B/8B 和 Llama 3B/8B，云端 LLM 包括 DeepSeek-R1-Distill-Llama-70B、Qwen3-235B-A22B 和 Qwen3-Max；训练用 8 张 H20，延迟用单张 RTX 4090 上的 Qwen3-8B 对接云端 API 测得，不是手机实测。
- **Sources:** [metadata](https://arxiv.org/abs/2604.17827v2), [full text](https://arxiv.org/html/2604.17827v2). Checked 2026-10-19.

<a id="2610-14209"></a>

## SLM Interpreter

- **Version:** 2026-10-09, v1; first submitted 2026-10-09.
- **Status:** preprint.
- **Exchange:** User request and, on failure, stack traces that can contain user content / the generated program. / 用户请求，以及失败时可能含有用户内容的 stack trace / 生成的程序。
- **Evidence:** AppWorld Test Normal and Test Challenge with Qwen3.6-27B, Qwen3.5-122B-A10B, and Qwen3-Coder-Next as planners and Qwen3.5 SLMs up to 9B; all models are served with llama.cpp on A100 or V100 GPUs, so device cost is reported as token and context counts rather than latency or energy.
- **实验边界：** 在 AppWorld 的 Test Normal 和 Test Challenge 上评测，规划模型为 Qwen3.6-27B、Qwen3.5-122B-A10B 和 Qwen3-Coder-Next，SLM 为不超过 9B 的 Qwen3.5；所有模型都用 llama.cpp 跑在 A100 或 V100 上，端侧开销以 token 与上下文长度报告，没有延迟或能耗实测。
- **Sources:** [metadata](https://arxiv.org/abs/2610.14209v1), [full text](https://arxiv.org/html/2610.14209v1). Checked 2026-10-15.

<a id="2609-32130"></a>

## REBASE

- **Version:** 2026-09-26, v1; first submitted 2026-09-26.
- **Status:** preprint.
- **Exchange:** Escalating repair evidence (fingerprint and failing step, accessibility-subtree diff, low-resolution crop, screenshot) / version-keyed path patches. / 逐级升级的修复证据（指纹与失败步骤、无障碍子树 diff、低分辨率局部截图、整屏截图） / 按版本索引的路径补丁。
- **Evidence:** Two Jetson AGX Orin 64 GB boards run Qwen3-VL-8B (INT4, AWQ) as the device agent and control AndroidWorld Android 13 environments hosted on a Jetson AGX Thor gateway; the cloud agent is Gemini 3.1 Pro; nine app version pairs from the F-Droid archive (three hidden from the cloud); tc/netem shapes three bandwidth and three RTT tiers, and device energy is reported in joules.
- **实验边界：** 两块 Jetson AGX Orin 64 GB 运行 Qwen3-VL-8B（INT4、AWQ）作为端侧 agent，控制部署在 Jetson AGX Thor 网关上的 AndroidWorld Android 13 环境；云端 agent 为 Gemini 3.1 Pro；使用 F-Droid 归档中的九组应用版本（其中三组对云端不可见）；用 tc/netem 设置三档带宽和三档 RTT，端侧能耗以焦耳报告。
- **Sources:** [metadata](https://arxiv.org/abs/2609.32130v1), [full text](https://arxiv.org/html/2609.32130v1). Checked 2026-10-20.

<a id="2605-28646"></a>

## MaskClaw

- **Version:** 2026-05-29, v2; first submitted 2026-05-27.
- **Status:** preprint.
- **Exchange:** Allowed screen content, a masked SafeScreenshot, or a confirmation request in place of the raw screenshot / downstream agent behavior is outside the paper's scoring. / 放行的屏幕内容、遮挡后的 SafeScreenshot，或代替原始截图的确认请求 / 下游 agent 的行为不在论文评分范围内。
- **Evidence:** Offline evaluation on the 832-sample P-GUI-Evo benchmark built from real UI patterns and reconstructed HTML screens, using a static single-step protocol that scores Allow/Mask/Ask decisions, leakage, and raw-upload rate, plus five designed skill-evolution scenarios; the authors state that they do not claim end-to-end device latency or deployment readiness.
- **实验边界：** 在由真实界面模式和重建 HTML 屏幕构成的 832 条 P-GUI-Evo 基准上离线评估，采用静态单步协议，对放行/遮挡/询问决策、泄露和原图上传率评分，另有五个设计好的 skill 演化场景；作者明确不声称端到端设备延迟或可部署性。
- **Sources:** [metadata](https://arxiv.org/abs/2605.28646v2), [full text](https://arxiv.org/html/2605.28646v2). Checked 2026-10-20.

<a id="2510-15455"></a>

## CORE

- **Version:** 2025-10-17, v1; first submitted 2025-10-17.
- **Status:** preprint.
- **Exchange:** Per-block sub-task candidates, the task and history, and only the top-ranked UI blocks / the selected sub-task and target element. / 各块的候选子任务、任务描述与历史，以及排名靠前的 UI 块 / 选定的子任务与目标元素。
- **Evidence:** DroidTask (143 tasks, 12 apps) on a real Honor Play3 phone with Android 9 and AndroidLab (98 tasks, 9 apps) on the Pixel 7 Pro emulator; GPT-4o via API is the cloud LLM, while local LLMs such as Gemma 2-9B and Qwen2.5-7B run on an RTX 4090D GPU rather than on the phone; UI exposure reduction and cloud and local latency are reported separately.
- **实验边界：** DroidTask（143 个任务、12 个应用）在搭载 Android 9 的真实 Honor Play3 手机上运行，AndroidLab（98 个任务、9 个应用）在 Pixel 7 Pro 模拟器上运行；云端 LLM 为通过 API 调用的 GPT-4o，Gemma 2-9B、Qwen2.5-7B 等本地 LLM 跑在 RTX 4090D GPU 上而非手机上；UI 暴露减少量以及云端、本地延迟分别报告。
- **Sources:** [metadata](https://arxiv.org/abs/2510.15455v1), [full text](https://arxiv.org/html/2510.15455v1). Checked 2026-10-20.

<a id="2602-10139"></a>

## Available but Invisible

- **Version:** 2026-04-26, v3; first submitted 2026-02-08.
- **Status:** preprint.
- **Exchange:** Anonymized instructions, XML hierarchies, and screenshots with typed placeholders / actions over the virtual UI, resolved locally against real values. / 带类型占位符的匿名化指令、XML 层级和截图 / 针对虚拟界面的动作，由本地对照真实值解析。
- **Evidence:** AndroidLab (138 tasks, XML and SoM modes) on the default Pixel 7 Pro emulator with GPT-4o and Gemini-3-flash-preview as cloud agents, and PrivScreen QA with Qwen2.5-VL-7B, GPT-5, and UI-TARS-7B; PrivScreen baseline numbers are cited from the DualTAP paper; no on-phone latency or energy measurement.
- **实验边界：** AndroidLab（138 个任务，XML 与 SoM 两种模式）在默认 Pixel 7 Pro 模拟器上运行，云端 agent 为 GPT-4o 和 Gemini-3-flash-preview；PrivScreen 问答使用 Qwen2.5-VL-7B、GPT-5 和 UI-TARS-7B，其基线数字引自 DualTAP 论文；没有手机上的延迟或能耗测量。
- **Sources:** [metadata](https://arxiv.org/abs/2602.10139v3), [full text](https://arxiv.org/html/2602.10139v3). Checked 2026-10-20.

<a id="2604-23941"></a>

## GoClick

- **Version:** 2026-04-27, v1; first submitted 2026-04-27.
- **Status:** preprint.
- **Exchange:** Screenshot and task for planning / action intent or functional description of the target element. / 用于规划的截图与任务 / 动作意图或目标元素的功能描述。
- **Evidence:** Grounding benchmarks plus step-level agent evaluation on recorded screenshot trajectories with ground-truth actions; TTFT and TPOT are measured on one L20 GPU at batch size 1 with a 780×360 input to approximate mobile use, not on a phone.
- **实验边界：** 在 GUI 定位基准上评测，并在带标准动作的录制截图轨迹上做逐步 agent 评测；TTFT 与 TPOT 在单张 L20 GPU 上以批大小 1、780×360 输入近似手机场景测得，并非手机实测。
- **Sources:** [metadata](https://arxiv.org/abs/2604.23941v1), [full text](https://arxiv.org/html/2604.23941v1). Checked 2026-10-20.

<a id="2512-22047"></a>

## MAI-UI

- **Version:** 2025-12-26, v1; first submitted 2025-12-26.
- **Status:** preprint.
- **Exchange:** Error summary plus trajectory history (instruction, screenshots, past thoughts and actions) at the switch / the cloud agent executes the remaining steps. / 切换时的错误摘要与轨迹历史（指令、截图、此前的思考与动作） / 由云端 agent 执行剩余步骤。
- **Evidence:** AndroidWorld online evaluation of the device–cloud system against device-only, random-switch, no-error-summary, and cloud-only baselines, reporting success rate, cloud-call reduction, and the share of tasks finished on device; models are Qwen3-VL-based MAI-UI variants from 2B to 235B-A22B; privacy blocking is shown only as a pilot case study, and the checked sections report no phone latency or energy.
- **实验边界：** 在 AndroidWorld 上在线评估端云系统，对比纯端侧、随机切换、无错误摘要和纯云端基线，报告成功率、云端调用减少量和完全在端侧完成的任务比例；模型为基于 Qwen3-VL 的 MAI-UI 系列（2B 至 235B-A22B）；隐私拦截只以试点案例展示，所查章节未报告手机延迟或能耗。
- **Sources:** [metadata](https://arxiv.org/abs/2512.22047v1), [full text](https://arxiv.org/html/2512.22047v1). Checked 2026-10-20.

<a id="2605-08646"></a>

## PAAC

- **Version:** 2026-10-18, v2; first submitted 2026-05-09.
- **Status:** NeurIPS 2026 (author-reported).
- **Exchange:** Sanitized task and per-step key findings with typed placeholders / sanitized reasoning and actions that the device de-references before execution. / 带类型占位符的脱敏任务与每步要点 / 脱敏的推理与动作，端侧执行前还原。
- **Evidence:** τ²-Bench Airline (50) and Retail (115) plus 20 sampled GAIA tasks under privacy levels P0–P3, and 17 further benchmarks with 100 sampled instances each; the on-device agent Qwen3-4B-Instruct is served by vLLM on an NVIDIA A100 and the cloud agent is Gemini 3 Flash; leakage is computed with three LLM evaluators plus regex matching; no phone deployment.
- **实验边界：** 在 τ²-Bench Airline（50 例）、Retail（115 例）和抽样的 20 个 GAIA 任务上按 P0–P3 隐私等级评测，另有 17 个基准各抽样 100 例；端侧 agent Qwen3-4B-Instruct 通过 vLLM 跑在 NVIDIA A100 上，云端 agent 为 Gemini 3 Flash；泄露率由三个 LLM 评估器加正则匹配计算；没有手机部署。
- **Sources:** [metadata](https://arxiv.org/abs/2605.08646v2), [full text](https://arxiv.org/html/2605.08646v2). Checked 2026-10-20.

<a id="2604-07767"></a>

## AdecPilot

- **Version:** 2026-04-09, v1; first submitted 2026-04-09.
- **Status:** preprint.
- **Exchange:** Task instruction with far fewer UI elements than a cloud-only agent uploads / abstract milestones, with at most one replanning round. / 任务指令，上传的 UI 元素远少于纯云端 agent / 抽象里程碑，至多一轮重规划。
- **Evidence:** AndroidWorld (116 tasks, 20 apps) on a Pixel 6 emulator (API 33) over three seeds, plus AndroidLab; GPT-4o is the cloud designer and a quantized Qwen3-VL-2B runs on a local server with an RTX 4070 TiS GPU; reports success rate, cloud calls and tokens, relative cloud energy, latency, and reduction in uploaded UI elements.
- **实验边界：** AndroidWorld（116 个任务、20 个应用）在 Pixel 6 模拟器（API 33）上跑三个随机种子，另有 AndroidLab；云端设计者为 GPT-4o，量化的 Qwen3-VL-2B 跑在配有 RTX 4070 TiS 的本地服务器上；报告成功率、云端调用与 token、相对云端能耗、延迟和上传 UI 元素的减少量。
- **Sources:** [metadata](https://arxiv.org/abs/2604.07767v1), [full text](https://arxiv.org/html/2604.07767v1). Checked 2026-10-20.

<a id="2609-35775"></a>

## SPECTRA

- **Version:** 2026-07-31, v1; first submitted 2026-07-31.
- **Status:** ACM MM 2026 (author-reported).
- **Exchange:** Screenshot and instruction for requested cases / cloud grounding coordinates. / 被判定需要请求的截图与指令 / 云端给出的定位坐标。
- **Evidence:** MMBench-GUI, ScreenSpot-Pro, and UI-I2E-Bench with InfiGUI-G1-3B or Holo1.5-3B on the edge and GTA1-32B in the cloud; request quality is reported as AUC, SRCC, and the area under a normalized collaborative-gain curve over request rates, and an on-device cost table is given for InfiGUI-G1-3B on ScreenSpot-Pro.
- **实验边界：** 在 MMBench-GUI、ScreenSpot-Pro 和 UI-I2E-Bench 上评测，端侧为 InfiGUI-G1-3B 或 Holo1.5-3B，云端为 GTA1-32B；请求质量以 AUC、SRCC 和归一化协同增益曲线下面积报告，并给出 InfiGUI-G1-3B 在 ScreenSpot-Pro 上的端侧开销表。
- **Sources:** [metadata](https://arxiv.org/abs/2609.35775v1), [full text](https://arxiv.org/html/2609.35775v1). Checked 2026-10-20.

<a id="2610-16778"></a>

## PrivacyGuard

- **Version:** 2026-10-12, v1; first submitted 2026-10-12.
- **Status:** preprint.
- **Exchange:** Sanitized instructions and screenshots carrying structured entity references / actions whose references are resolved locally. / 带结构化实体引用的脱敏指令与截图 / 含引用的动作，在本地解析。
- **Evidence:** Five-turn CrossTurnPII sessions, reference-required Android tasks, AndroidLab (138 tasks, four planners), and PrivScreen; all compared protection pipelines run on the same RTX 4090 server, which the authors describe as experimental apparatus rather than the remote planner, and a Xiaomi 12S workload checks single-device prototype feasibility.
- **实验边界：** 在五轮 CrossTurnPII 会话、需要引用的 Android 任务、AndroidLab（138 个任务、四个规划器）和 PrivScreen 上评测；所有对比的保护流程都跑在同一台 RTX 4090 服务器上，作者说明它是实验设备而非远端规划器；另用 Xiaomi 12S 上的负载验证单机原型的可行性。
- **Sources:** [metadata](https://arxiv.org/abs/2610.16778v1), [full text](https://arxiv.org/html/2610.16778v1). Checked 2026-10-20.

<a id="2609-33141"></a>

## On-Device Operation Caches

- **Version:** 2026-09-27, v1; first submitted 2026-09-27.
- **Status:** preprint.
- **Exchange:** Low-confidence queries with their table context / generated formula. / 低置信度的查询及其表格上下文 / 生成的公式。
- **Evidence:** NL2Formula (70,799 query–formula pairs over 21,670 tables) with a target 60% hit rate and at least 95% precision; Gemma 3 1B serves as the cache model and GPT-5 with model routing is the cloud-only baseline; the device hardware behind the latency figures is not described in the checked sections.
- **实验边界：** 在 NL2Formula（21,670 张表上的 70,799 对查询与公式）上评测，目标命中率 60%、精度不低于 95%；缓存模型为 Gemma 3 1B，纯云端基线为带模型路由的 GPT-5；所查章节未说明延迟数字对应的设备硬件。
- **Sources:** [metadata](https://arxiv.org/abs/2609.33141v1), [full text](https://arxiv.org/html/2609.33141v1). Checked 2026-10-20.

<a id="2609-32642"></a>

## PriCon

- **Version:** 2026-09-26, v1; first submitted 2026-09-26.
- **Status:** preprint; ICLR 2027 submission under review ([OpenReview](https://openreview.net/forum?id=1rBcnLE8ft)).
- **Exchange:** Mathematical reformulation or cross-domain semantic surrogate of the task / guidance or code for the surrogate, mapped back locally. / 任务的数学改写或跨领域语义替身 / 针对替身任务的指导或代码，由本地映射回原任务。
- **Evidence:** Read from the PDF because the HTML rendering is truncated; the local-SLM role is played by GPT-4o-mini, DeepSeek-V4-Flash, and a Qwen3 model, with task-intent inference and utility reported per task family against direct consultation, sensitive-value removal, and decoy baselines; no device hardware or latency is measured.
- **实验边界：** 因 HTML 版本不完整而阅读 PDF；本地 SLM 的角色由 GPT-4o-mini、DeepSeek-V4-Flash 和一个 Qwen3 模型扮演，按任务族报告任务意图推断与效用，对比直接咨询、去除敏感值和诱饵基线；没有设备硬件或延迟测量。
- **Sources:** [metadata](https://arxiv.org/abs/2609.32642v1), [full text](https://arxiv.org/pdf/2609.32642v1). Checked 2026-10-25.

<a id="2605-30102"></a>

## Hybrid MAS

- **Version:** 2026-05-28, v1; first submitted 2026-05-28.
- **Status:** AIWILD Workshop at ICML 2026 (author-reported).
- **Exchange:** User query and execution state for verification / plans, verification verdicts, reset-safe summaries, and advice. / 用户查询与供验证的执行状态 / 计划、验证结论、可安全重置的摘要与建议。
- **Evidence:** HotpotQA (500 validation questions), FanOutQA, and AppWorld with Qwen3 4B–32B as edge models and GPT-4o via Azure OpenAI as the cloud model; edge energy comes from an analytical model that the authors present as a lower bound for order-of-magnitude comparison, not a device measurement.
- **实验边界：** 在 HotpotQA（500 个验证集问题）、FanOutQA 和 AppWorld 上评测，端侧模型为 Qwen3 4B–32B，云端模型为通过 Azure OpenAI 调用的 GPT-4o；端侧能耗来自解析模型，作者说明它是用于数量级比较的下界，并非设备实测。
- **Sources:** [metadata](https://arxiv.org/abs/2605.30102v1), [full text](https://arxiv.org/html/2605.30102v1). Checked 2026-10-20.

<a id="2502-04392"></a>

## Division-of-Thoughts

- **Version:** 2025-02-06, v1; first submitted 2025-02-06.
- **Status:** preprint.
- **Exchange:** Sub-tasks assigned to the cloud, with their dependencies / sub-task answers. / 分配给云端的子任务及其依赖 / 子任务答案。
- **Evidence:** 200 test questions from each of seven benchmarks (P3, SCAN, MATH, CHAMP, DROP, CSQA, WebShop); GPT-4o is the cloud LLM and Llama 3-8B the on-device model, deployed on a local A100 GPU; reports accuracy, time cost, and API cost.
- **实验边界：** 在七个基准（P3、SCAN、MATH、CHAMP、DROP、CSQA、WebShop）上各取 200 道测试题；云端 LLM 为 GPT-4o，端侧模型为部署在本地 A100 GPU 上的 Llama 3-8B；报告准确率、时间成本与 API 成本。
- **Sources:** [metadata](https://arxiv.org/abs/2502.04392v1), [full text](https://arxiv.org/html/2502.04392v1). Checked 2026-10-20.

<a id="2606-00756"></a>

## CoMIC

- **Version:** 2026-10-13, v2; first submitted 2026-05-30.
- **Status:** preprint.
- **Exchange:** Subgoal trajectories with contextual features / admitted experience and cross-agent guidance keyed by subgoal identifiers. / 带上下文特征的子目标轨迹 / 筛选后的经验与按子目标标识索引的跨 agent 指导。
- **Evidence:** Five AgentBoard tasks (Jericho, Blocksworld, Gripper, Tyreworld, Barman); edge agents run on a Linux workstation with one RTX 4090 and reach the cloud over HTTP/WebSocket; deepseek-chat is the cloud critic, with Mistral-7B edge agents alone or mixed with a gpt-4-turbo agent; here the edge is a Web edge server rather than a user device.
- **实验边界：** 在五个 AgentBoard 任务（Jericho、Blocksworld、Gripper、Tyreworld、Barman）上评测；端侧 agent 跑在配一张 RTX 4090 的 Linux 工作站上，通过 HTTP/WebSocket 与云端通信；云端评审为 deepseek-chat，端侧为单独的 Mistral-7B agent 或与一个 gpt-4-turbo agent 混合；这里的端侧是 Web 边缘服务器而非用户设备。
- **Sources:** [metadata](https://arxiv.org/abs/2606.00756v2), [full text](https://arxiv.org/html/2606.00756v2). Checked 2026-10-20.

<a id="2603-05974"></a>

## MCCom

- **Version:** 2026-03-09, v2; first submitted 2026-03-06.
- **Status:** FSE 2026 (author-reported).
- **Exchange:** Code context and re-ranked retrieved snippets after a rejected local suggestion / cloud completion. / 本地建议被拒后的代码上下文与重排后的检索片段 / 云端补全结果。
- **Evidence:** RepoEval line- and API-level subsets plus a new StmtEval benchmark, with 7B code LLMs such as Qwen2.5-Coder-7B as the cloud model and a trained 121M local model; offline experiments on A800 GPUs that account for retrieval, model inference, and an assumed 200 ms cloud query latency.
- **实验边界：** 在 RepoEval 的行级、API 级子集和新的 StmtEval 基准上评测，云端模型为 Qwen2.5-Coder-7B 等 7B 代码模型，本地为训练的 1.21 亿参数模型；离线实验在 A800 GPU 上进行，计入检索、模型推理和假定的 200 ms 云端查询延迟。
- **Sources:** [metadata](https://arxiv.org/abs/2603.05974v2), [full text](https://arxiv.org/html/2603.05974v2). Checked 2026-10-20.

<a id="2410-15285"></a>

## CAMP

- **Version:** 2025-04-05, v2; first submitted 2024-10-20.
- **Status:** IEEE CAI 2025 (author-reported).
- **Exchange:** Prompts enriched with locally retrieved code context / completions, documentation, error warnings, and chat answers. / 附带本地检索代码上下文的提示 / 补全、文档、错误提示与对话回答。
- **Evidence:** CoderEval class-, file-, and project-runnable tasks measured by Pass@K, plus a user study of the Xcode plugin; the local component is retrieval and indexing rather than a local generative model, and no device latency measurement is reported in the checked sections.
- **实验边界：** 在 CoderEval 的类级、文件级和项目级可运行任务上以 Pass@K 评测，另有 Xcode 插件的用户研究；本地组件是检索与索引而不是本地生成模型，所查章节未报告设备延迟测量。
- **Sources:** [metadata](https://arxiv.org/abs/2410.15285v2), [full text](https://arxiv.org/html/2410.15285v2). Checked 2026-10-20.

<a id="2608-00569"></a>

## CloudEdgeVLA

- **Version:** 2026-09-16, v3; first submitted 2026-08-01.
- **Status:** preprint; ICLR 2027 submission under review ([OpenReview](https://openreview.net/forum?id=vh50wiftCa)).
- **Exchange:** Observations sent asynchronously / cloud task features rather than actions. / 异步上传的观测 / 云端返回的任务特征而非动作。
- **Evidence:** Built on OpenVLA-OFT (7B) and evaluated on the four LIBERO simulation suites under simulated uniform delays of up to 40 control steps, with 50 trials per task and three seeds; no physical robot or real network in the checked sections.
- **实验边界：** 基于 OpenVLA-OFT（7B），在 LIBERO 的四个仿真任务集上、在最长 40 个控制步的模拟均匀延迟下评测，每个任务 50 次、三个随机种子；所查章节没有实体机器人或真实网络。
- **Sources:** [metadata](https://arxiv.org/abs/2608.00569v3), [full text](https://arxiv.org/html/2608.00569v3). Checked 2026-10-20.

<a id="2603-20711"></a>

## RoboECC

- **Version:** 2026-04-27, v2; first submitted 2026-03-21.
- **Status:** IJCNN 2026 (author-reported).
- **Exchange:** Intermediate activations at the chosen split point / outputs of the remaining stages for action generation. / 切分点处的中间激活 / 剩余阶段用于生成动作的输出。
- **Evidence:** Cloud side is an NVIDIA A100 and the edge side a Jetson AGX Orin or Thor in MAX_N mode; evaluated VLAs include OpenVLA and CogACT on LIBERO and SimplerEnv simulation, with a real-world deployment example; the framework's own overhead is reported separately.
- **实验边界：** 云端为 NVIDIA A100，端侧为工作在 MAX_N 模式的 Jetson AGX Orin 或 Thor；评测的 VLA 包括 OpenVLA 与 CogACT，在 LIBERO 和 SimplerEnv 仿真中测试，并有真实场景部署示例；框架自身开销单独报告。
- **Sources:** [metadata](https://arxiv.org/abs/2603.20711v2), [full text](https://arxiv.org/html/2603.20711v2). Checked 2026-10-20.

<a id="2603-07949"></a>

## RAPID

- **Version:** 2026-03-12, v2; first submitted 2026-03-09.
- **Status:** preprint.
- **Exchange:** Partitioned intermediate features when a high-importance phase is flagged / fresh action chunks. / 被标记为高重要性阶段时的切分中间特征 / 新的动作块。
- **Evidence:** OpenVLA on LIBERO pick-and-place, drawer-opening, and peg-insertion tasks under standard, visual-noise, and distraction conditions, plus real-world tasks; system-level numbers are measured on an NVIDIA A100 with an Intel Xeon Silver 4410T, and the checked setup does not name a separate embedded edge board.
- **实验边界：** 以 OpenVLA 在 LIBERO 的抓放、开抽屉和插销任务上评测，包含标准、视觉噪声和干扰三种条件，另有真实场景任务；系统级数字在 NVIDIA A100 与 Intel Xeon Silver 4410T 上测得，所查设置没有说明独立的嵌入式端侧板卡。
- **Sources:** [metadata](https://arxiv.org/abs/2603.07949v2), [full text](https://arxiv.org/html/2603.07949v2). Checked 2026-10-20.

<a id="2609-25415"></a>

## Cloud, Edge, or Split?

- **Version:** 2026-09-21, v1; first submitted 2026-09-21.
- **Status:** iEdge 2026 (author-reported).
- **Exchange:** Image–query pair (cloud) or projected visual tokens (split) / generated text. / 图像与查询（全云端）或投影后的视觉 token（拆分） / 生成的文本。
- **Evidence:** An NVIDIA Jetson (8-core Cortex-A78AE CPU, 1024-core Ampere GPU) represents the UAV's onboard computer, with tegrastats sampling power at 100 ms; workloads come from a UAV power-line inspection dataset and CODEBRIM bridge defects under selected bandwidth intervals.
- **实验边界：** 以一块 NVIDIA Jetson（8 核 Cortex-A78AE CPU、1024 核 Ampere GPU）代表无人机机载计算，tegrastats 每 100 ms 采样功耗；负载来自无人机电力线巡检数据集和 CODEBRIM 桥梁缺陷数据集，在若干带宽区间下测试。
- **Sources:** [metadata](https://arxiv.org/abs/2609.25415v1), [full text](https://arxiv.org/html/2609.25415v1). Checked 2026-10-20.

<a id="2408-09972"></a>

## EC-Drive

- **Version:** 2024-08-19, v1; first submitted 2024-08-19.
- **Status:** preprint.
- **Exchange:** Drift-flagged driving data and scene descriptions / cloud perception, prediction, and planning outputs. / 被漂移检测标记的驾驶数据与场景描述 / 云端的感知、预测与规划结果。
- **Evidence:** Qualitative scenario comparisons on images collected by autonomous vehicles on a university campus, plus a table scoring smaller and larger models on gaze, scene understanding, and logic; the checked sections give no edge hardware or end-to-end latency figures.
- **实验边界：** 在校园内自动驾驶车辆采集的图像上做定性场景对比，另有一张表按注视区域、场景理解和推理逻辑为大小模型打分；所查章节没有给出端侧硬件或端到端延迟数字。
- **Sources:** [metadata](https://arxiv.org/abs/2408.09972v1), [full text](https://arxiv.org/html/2408.09972v1). Checked 2026-10-20.

<a id="2606-31497"></a>

## Communication-Aware Robot Execution

- **Version:** 2026-10-02, v2; first submitted 2026-06-30.
- **Status:** preprint.
- **Exchange:** Next cloud request submitted from a selected location / the next task primitive. / 在选定位置发出的下一次云端请求 / 下一个任务原语。
- **Evidence:** ROS/Gazebo simulation of a TurtleBot3 Burger with a floor-level communication map built from measured Wi-Fi fingerprints (SODIndoorLoc) and a shared cloud delay model; no physical robot or live network.
- **实验边界：** 在 ROS/Gazebo 中仿真 TurtleBot3 Burger，通信地图由实测 Wi-Fi 指纹（SODIndoorLoc）构建，并使用统一的云端时延模型；没有实体机器人或真实网络。
- **Sources:** [metadata](https://arxiv.org/abs/2606.31497v2), [full text](https://arxiv.org/html/2606.31497v2). Checked 2026-10-20.

<a id="2609-07838"></a>

## ComVLA

- **Version:** 2026-09-07, v1; first submitted 2026-09-07.
- **Status:** IEEE GLOBECOM 2026 (author-reported).
- **Exchange:** Top-K visual tokens sized to channel capacity / predicted actions. / 按信道容量确定数量的 Top-K 视觉 token / 预测的动作。
- **Evidence:** Four LIBERO suites with OpenVLA-OFT fine-tuned on LIBERO and SigLIP and DINOv2 encoders on the edge side; all experiments run on an H100 GPU, with transmitted bytes computed analytically and Rayleigh and Rician fading simulated.
- **实验边界：** 在 LIBERO 四个任务集上评测，使用在 LIBERO 上微调的 OpenVLA-OFT，端侧为 SigLIP 与 DINOv2 编码器；所有实验在 H100 GPU 上运行，传输字节按公式计算，Rayleigh 与 Rician 衰落为仿真。
- **Sources:** [metadata](https://arxiv.org/abs/2609.07838v1), [full text](https://arxiv.org/html/2609.07838v1). Checked 2026-10-20.

<a id="2603-05831"></a>

## Knowledge-Driven Mobile Agentic AI

- **Version:** 2026-03-06, v1; first submitted 2026-03-06.
- **Status:** preprint.
- **Exchange:** Accumulated mission logs, promoted offline at the home side / a cacheable knowledge pack. / 积累的任务日志，在后方离线提炼 / 可缓存的知识包。
- **Evidence:** A UAV aerial-base-station case study under intermittent backhaul and runtime disruptions, with Qwen2.5-3B for onboard macro-level replanning and a Gemini-based home replanning baseline, averaged over 50 inference episodes; reasoning is mission-level replanning rather than low-level control.
- **实验边界：** 以间歇回传和运行时中断下的无人机空中基站任务为案例，机载宏观重规划使用 Qwen2.5-3B，后方重规划基线基于 Gemini，结果为 50 个推理回合的平均；推理对象是任务级重规划而非底层控制。
- **Sources:** [metadata](https://arxiv.org/abs/2603.05831v1), [full text](https://arxiv.org/html/2603.05831v1). Checked 2026-10-20.

<a id="2608-15502"></a>

## EcoVLA

- **Version:** 2026-08-16, v1; first submitted 2026-08-16.
- **Status:** APPT 2026 (author-reported).
- **Exchange:** Intermediate tensors at stage boundaries / outputs of the remaining stages and actions. / 阶段边界处的中间张量 / 剩余阶段的输出与动作。
- **Evidence:** Real testbed with a Jetson AGX Orin 32 GB as the robot device and an RTX 4090 edge server, power from tegrastats and NVML, and tc-injected bandwidth changes; OpenVLA, π0, π0.5, SmolVLA, and RDT-1b are driven by standardized online requests because the focus is deployment efficiency rather than task success.
- **实验边界：** 真实测试平台：机器人端为 Jetson AGX Orin 32 GB，边缘服务器为 RTX 4090，功耗来自 tegrastats 与 NVML，用 tc 注入带宽变化；OpenVLA、π0、π0.5、SmolVLA 和 RDT-1b 以标准化的在线请求驱动，因为关注点是部署效率而非任务成功率。
- **Sources:** [metadata](https://arxiv.org/abs/2608.15502v1), [full text](https://arxiv.org/html/2608.15502v1). Checked 2026-10-20.

<a id="2610-10812"></a>

## Skill-SLM

- **Version:** 2026-10-07, v1; first submitted 2026-10-07.
- **Status:** preprint.
- **Exchange:** No run-time exchange; offline, a cloud LLM produces the skill library and training data / LoRA-tuned SLM weights deployed on the robot. / 运行时无交换；离线阶段由云端 LLM 生成 skill 库与训练数据 / 部署到机器人上的 LoRA 微调 SLM 权重。
- **Evidence:** Llama-3.2-3B, Llama-3.1-8B, Qwen3-4B, and Qwen3-8B are trained with LoRA on four H200 GPUs, quantized to Q4_K_M, and run with Ollama on a Jetson Orin NX 16 GB aboard a Holybro X500 V2 UAV and a ROSMASTER X3 ground vehicle.
- **实验边界：** Llama-3.2-3B、Llama-3.1-8B、Qwen3-4B 与 Qwen3-8B 在四张 H200 上用 LoRA 训练，量化为 Q4_K_M，用 Ollama 跑在 Holybro X500 V2 无人机和 ROSMASTER X3 地面车搭载的 Jetson Orin NX 16 GB 上。
- **Sources:** [metadata](https://arxiv.org/abs/2610.10812v1), [full text](https://arxiv.org/html/2610.10812v1). Checked 2026-10-20.

<a id="2607-18659"></a>

## Broken Gates

- **Version:** 2026-07-21, v1; first submitted 2026-07-21.
- **Status:** preprint.
- **Exchange:** Not an edge–cloud method; varies where the agent's browser runs / bot-defense verdicts and trust scores. / 不是端云方法；比较 agent 的浏览器运行在哪里 / 反爬判定与信任分。
- **Evidence:** Seven solver services and six agents tested against four deployed bot-management systems, with fine-grained interaction-trace analysis; a security measurement study that does not propose or evaluate edge–cloud collaboration.
- **实验边界：** 七个破解服务与六个 agent 对抗四种已部署的机器人管理系统，并做细粒度交互轨迹分析；这是安全测量研究，没有提出或评估端云协同方法。
- **Sources:** [metadata](https://arxiv.org/abs/2607.18659v1), [full text](https://arxiv.org/html/2607.18659v1). Checked 2026-10-20.

<a id="2606-30119"></a>

## Unmasking Web Agents

- **Version:** 2026-06-29, v1; first submitted 2026-06-29.
- **Status:** preprint.
- **Exchange:** Not an edge–cloud method; contrasts cloud-hosted and locally run agents / anti-bot outcomes and fingerprints. / 不是端云方法；对比云端托管与本地运行的 agent / 反爬结果与指纹。
- **Evidence:** Six web agents plus scrapers and browser-automation frameworks visit the honeysites, with human baselines from two local Intel Core i7 machines; cloud-hosted agents were monitored manually; the study also finds that stealth techniques often raise detectability, and it does not evaluate edge–cloud collaboration.
- **实验边界：** 六个 Web agent 以及爬虫和浏览器自动化框架访问蜜罐网站，人类基线来自两台本地 Intel Core i7 机器，云端托管的 agent 由人工监控；研究还发现隐身技术常常反而提高可检测性；没有评估端云协同。
- **Sources:** [metadata](https://arxiv.org/abs/2606.30119v1), [full text](https://arxiv.org/html/2606.30119v1). Checked 2026-10-20.

<a id="2605-01247"></a>

## FP-Agent

- **Version:** 2026-05-02, v1; first submitted 2026-05-02.
- **Status:** preprint.
- **Exchange:** Not an edge–cloud method / browser and behavioral fingerprints collected by the site. / 不是端云方法 / 网站采集的浏览器与行为指纹。
- **Evidence:** Flight-booking, online-shopping, and forum tasks on an instrumented honey website, a multi-class classifier over the collected features, and a case study against Cloudflare's bot detection; it does not evaluate edge–cloud collaboration.
- **实验边界：** 在带监测的蜜罐网站上执行订机票、网购和论坛互动任务，基于采集特征训练多分类器，并与 Cloudflare 的机器人检测做案例对比；没有评估端云协同。
- **Sources:** [metadata](https://arxiv.org/abs/2605.01247v1), [full text](https://arxiv.org/html/2605.01247v1). Checked 2026-10-20.

<a id="2603-19418"></a>

## Speculative Policy Orchestration

- **Version:** 2026-03-19, v1; first submitted 2026-03-19.
- **Status:** preprint.
- **Exchange:** Robot state / speculative future kinematic waypoints. / 机器人状态 / 推测的未来运动路径点。
- **Evidence:** RLBench manipulation on a physically distributed edge–cloud setup with an emulated 150 ms round-trip delay and ±30 ms jitter; the cloud model is a world model, including a three-layer MLP trained on demonstrations, not a language or VLA model, so transfer to LLM or VLA policies is not shown.
- **实验边界：** 在物理分布的端云环境中做 RLBench 操作任务，模拟 150 ms 往返时延和 ±30 ms 抖动；云端模型是世界模型（包括在示教数据上训练的三层 MLP），不是语言或 VLA 模型，因此没有展示向 LLM/VLA 策略的迁移。
- **Sources:** [metadata](https://arxiv.org/abs/2603.19418v1), [full text](https://arxiv.org/html/2603.19418v1). Checked 2026-10-20.

<a id="2610-21436"></a>

## HyCo

- **Version:** 2026-10-19, v2; first submitted 2026-10-15.
- **Status:** preprint.
- **Exchange:** Draft token tree (token IDs and parent indices) / accepted tokens, bonus token, and the hidden state, input embedding, and KV entries the device-side MTP head needs. / draft token 树（token ID 与父节点索引）/ 接受的 token、bonus token，以及端侧 MTP 头所需的 hidden state、输入 embedding 和 KV 条目。
- **Evidence:** Gemma 4 26B-A4B verifier on one RTX PRO 6000 cloud GPU, drafters on a Galaxy S26 Ultra NPU over commercial LTE/5G; single-client runs on Spec-Bench and 32K-token summarization; server GPU time per output token is the main cost metric, not loaded-service capacity or energy; the default ε rule is lossy and is evaluated separately from exact verification.
- **实验边界：** 验证模型 Gemma 4 26B-A4B 跑在一张 RTX PRO 6000 云端 GPU 上，两个 drafter 跑在 Galaxy S26 Ultra 的 NPU 上，经商用 LTE/5G 连接；Spec-Bench 与 32K token 摘要上的单客户端实验；主要成本指标是每个输出 token 的服务器 GPU 时间，不是满载服务容量或能耗；默认的 ε 规则有损，与严格验证分开报告。
- **Sources:** [metadata](https://arxiv.org/abs/2610.21436v2), [full text](https://arxiv.org/html/2610.21436v2). Checked 2026-10-25.

<a id="2610-26171"></a>

## CEMA-Router

- **Version:** 2026-10-19, v1; first submitted 2026-10-19.
- **Status:** preprint.
- **Exchange:** Whole requests dispatched to one cloud or edge endpoint / responses; the router consumes node profiles, backlog estimates, and profiled quality scores. / 整条请求派发到某个云端或边缘端点 / 返回结果；路由器使用节点画像、积压估计和离线测得的质量分数。
- **Evidence:** RouterBench traces mapped to a simulated five-tier cloud–edge profile, plus a six-node testbed of server GPUs labelled cloud (A100, V100) and edge (A40, A30) running 1.7B–14B models on GSM8K and MMLU; no phones or embedded boards; API price is zero in the testbed, so the deployed comparison covers quality, energy, and completion time; energy is estimated from power profiles.
- **实验边界：** 一部分是把 RouterBench 轨迹映射到模拟的五档云边配置上；另一部分是六节点测试床，节点均为服务器 GPU，分别标为云端（A100、V100）和边缘（A40、A30），运行 1.7B–14B 模型，评测 GSM8K 与 MMLU；没有手机或嵌入式板卡；测试床中 API 价格为零，因此部署对比只涉及质量、能耗和完成时间；能耗由功率画像估算。
- **Sources:** [metadata](https://arxiv.org/abs/2610.26171v1), [full text](https://arxiv.org/html/2610.26171v1). Checked 2026-10-25.

<a id="2610-21463"></a>

## SpecAgent

- **Version:** 2026-10-15, v1; first submitted 2026-10-15.
- **Status:** preprint; ICLR 2027 submission under review ([OpenReview](https://openreview.net/forum?id=FgDfnkBEzf)).
- **Exchange:** Drafted trajectory segment with real read-only tool observations and a held state-changing action / verdict (accepted prefix length, reason, optional replacement step) or a repair turn. / 带真实只读工具观测、末尾挂起一个状态修改动作的轨迹草稿片段 / 判定（接受的前缀长度、理由、可选的替换步骤）或一轮修复。
- **Evidence:** Main experiments (τ²-Bench, AutomationBench, VitaBench) run both Qwen3.5-4B and Qwen3.5-397B-A17B on H20 servers, with memory traffic and FLOPs estimated from token counts; the edge–cloud setting is a separate MCP-Atlas run with the weak model on one local RTX 5090 and three cloud API strong models, where API cost and strong output tokens fall but wall time does not.
- **实验边界：** 主实验（τ²-Bench、AutomationBench、VitaBench）中 Qwen3.5-4B 与 Qwen3.5-397B-A17B 都部署在 H20 服务器上，显存流量和 FLOPs 由 token 数估算；端云设置是单独的 MCP-Atlas 实验，弱模型跑在一张本地 RTX 5090 上，强模型为三个云端 API 模型，API 费用和强模型输出 token 下降，但端到端时间没有下降。
- **Sources:** [metadata](https://arxiv.org/abs/2610.21463v1), [full text](https://arxiv.org/html/2610.21463v1). Checked 2026-10-25.

<a id="2610-35489"></a>

## TP-JSCC

- **Version:** 2026-10-26, v1; first submitted 2026-10-26.
- **Status:** preprint.
- **Exchange:** Question text over a reliable channel plus JSCC-encoded pruned visual tokens over a noisy channel / answer. / 经可靠信道传输的问题文本，加上经噪声信道传输、JSCC 编码后的剪枝视觉 token / 答案。
- **Evidence:** ScanQA and SQA3D with cdViews view selection and LLaVA-OneVision as the cloud LVLM; the wireless link is a simulated AWGN channel at 0–25 dB SNR, and edge-side cost is reported as GFLOPs (stated to fit a Jetson TX2-class GPU) rather than measured on a device.
- **实验边界：** 在 ScanQA 与 SQA3D 上评测，使用 cdViews 选视角、LLaVA-OneVision 作为云端 LVLM；无线链路为 0–25 dB SNR 的仿真 AWGN 信道，端侧开销以 GFLOPs 报告（文中称可由 Jetson TX2 级 GPU 承担），未在真实设备上测量。
- **Sources:** [metadata](https://arxiv.org/abs/2610.35489v1), [full text](https://arxiv.org/html/2610.35489v1). Checked 2026-10-30.

<a id="2610-32079"></a>

## Label-Budgeted Attribute Inference

- **Version:** 2026-10-23, v1; first submitted 2026-10-23.
- **Status:** preprint.
- **Exchange:** Hidden-state sequence after the split layer (generation) or a 512-dimensional embedding (face verification) / server-side output. / 拆分层之后的隐状态序列（生成任务）或 512 维嵌入（人脸验证） / 服务器端输出。
- **Evidence:** LLaVA-1.5-7B and Qwen2.5-VL-3B on FairFace and UTKFace, with an RTX 2080 Ti (11 GiB) emulating the device and a V100 as the server; device latency, memory, and energy are measured per split layer, while transmission time is computed for an assumed link rate.
- **实验边界：** 在 FairFace 与 UTKFace 上评测 LLaVA-1.5-7B 和 Qwen2.5-VL-3B，以 RTX 2080 Ti（11 GiB）模拟设备、V100 作为服务器；按拆分层测量设备端延迟、显存和能耗，传输时间按假定链路速率计算。
- **Sources:** [metadata](https://arxiv.org/abs/2610.32079v1), [full text](https://arxiv.org/html/2610.32079v1). Checked 2026-10-30.

