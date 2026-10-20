"""Validate the catalog and render both READMEs, evidence notes, and BibTeX."""
import argparse
import datetime as dt
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = [
    ('skills', 'Skills, plans, and trajectory collaboration', 'Skill、计划与轨迹协同'),
    ('routing', 'Routing and help-seeking', '路由与求助决策'),
    ('context', 'Context and modality selection', '上下文与模态选择'),
    ('personalization', 'Personalization and knowledge transfer', '个性化与知识迁移'),
    ('training', 'Collaborative and federated training', '协同训练与联邦优化'),
    ('decoding', 'Token-level collaborative decoding', 'Token 级协同解码'),
    ('embodied', 'Embodied and robot control across edge and cloud', '具身与机器人端云协同'),
    ('adjacent', 'Adjacent ideas and transfer opportunities', '邻近工作与迁移机会'),
]

def validate(data):
    cutoff = dt.date.fromisoformat(data['cutoff'])
    ids = set()
    for p in data['papers']:
        assert re.fullmatch(r'\d{4}\.\d{4,5}', p['arxiv_id']), p['name']
        assert p['arxiv_id'] not in ids, 'Duplicate arXiv entry'
        ids.add(p['arxiv_id'])
        assert type(p['version']) is int and p['version'] > 0
        first = dt.date.fromisoformat(p['first_submitted'])
        version = dt.date.fromisoformat(p['version_date'])
        checked = dt.date.fromisoformat(p['checked_on'])
        assert first <= version <= cutoff and checked >= version
        assert p['category'] in {c[0] for c in CATEGORIES}
        assert p['scope'] in {'core', 'adjacent'}
        assert (p['category'] == 'adjacent') == (p['scope'] == 'adjacent')
        for field in ['title','authors','summary','summary_zh','exchange','exchange_zh','evidence','evidence_zh','status']:
            assert p[field], f'Missing {field}: {p["name"]}'
        expected = f'https://arxiv.org/abs/{p["arxiv_id"]}v{p["version"]}'
        assert p['paper_url'] == expected
        for url in p['source_urls'] + ([p['code_url']] if p['code_url'] else []):
            parsed = urlparse(url)
            assert parsed.scheme == 'https' and parsed.hostname and not parsed.username
        assert p['code_status'] == ('author-linked' if p['code_url'] else 'not located in checked paper pages')

def readme(data, zh=False):
    papers=data['papers']
    core=sum(p['scope']=='core' for p in papers)
    intro = (
        '# Awesome Edge–Cloud LLM & Agent Collaboration\n\n'
        '[English](README.md) | **简体中文**\n\n'
        '收集 **LLM/Agent 端云协同**（含机器人与具身 agent）的论文、代码与数据集，按“优化什么”分类，重点关注端云之间交换什么，以及这些内容如何转化为端侧可复用能力。\n\n'
        if zh else
        '# Awesome Edge–Cloud LLM & Agent Collaboration\n\n'
        '**English** | [简体中文](README.zh-CN.md)\n\n'
        'A curated collection of **edge–cloud collaboration for LLMs and agents**, including robots and other embodied agents, organized by what is optimized: execution, guidance, context, personalization, training, decoding, and embodied control. A central question is what to exchange and how that exchange becomes reusable edge capability.\n\n'
    )
    intro += (f'**范围截至 {data["cutoff"]} · {len(papers)} 篇 · {core} 篇核心工作 + {len(papers)-core} 篇邻近工作。** 日期为所链接 arXiv 版本日期，首次提交日期另存于数据文件。本文献清单不是穷尽性综述，也不是统一性能排行榜。\n\n' if zh else f'**Coverage cutoff: {data["cutoff"]} · {len(papers)} papers · {core} core + {len(papers)-core} adjacent.** Dates refer to linked arXiv versions; initial submission dates are retained in the catalog. This is a focused reading list, not an exhaustive survey or a unified performance leaderboard.\n\n')
    intro += ('多数近期工作为 preprint；录用信息采用作者在 arXiv/项目页的报告。代码仅收录论文关联的作者链接；“未定位”不等于不存在。收益以作者实验为准，真实设备、服务器模拟和无线仿真应分别理解。\n\n' if zh else 'Many recent entries are preprints. Venue labels reflect author reports in arXiv/project pages. Code links are author-linked; “not located” does not mean unavailable. Reported results remain specific to the authors’ evaluation; real devices, server emulation, and wireless simulations must be distinguished.\n\n')
    intro += ('## 导航\n\n' if zh else '## Contents\n\n')
    for key,en,cn in CATEGORIES:
        intro += f'- [{cn if zh else en}](#{key})\n'
    intro += ('- [实验依据与边界](docs/evidence.md)\n- [研究问题与评估口径](docs/research-agenda.md)\n- [文献数据](data/papers.json) · [BibTeX](references.bib) · [贡献指南](CONTRIBUTING.md)\n\n' if zh else '- [Evaluation evidence and limits](docs/evidence.md)\n- [Research questions and evaluation](docs/research-agenda.md)\n- [Machine-readable catalog](data/papers.json) · [BibTeX](references.bib) · [Contributing](CONTRIBUTING.md)\n\n')
    intro += ('## 分类视角\n\n| 优化对象 | 典型决策 | 代表工作 |\n| --- | --- | --- |\n' if zh else '## Taxonomy\n\n| Optimization target | Typical decision | Examples |\n| --- | --- | --- |\n')
    taxonomy=[
        ('Guidance','指导内容','What structure and detail should the cloud return?','云端返回什么结构、多细的指导？','Co-Skill, EcoAgent'),
        ('Execution','执行位置','When should a query or agent step use the cloud?','哪个 query 或 agent step 需要云端？','Hera, GAPG'),
        ('Context','上传内容','Which modalities and observations are worth sending?','哪些模态与 observation 值得上传？','TMO, Co-Skill'),
        ('Capability','端侧能力','Which data and parameter components should adapt?','生成什么训练数据，适配哪些参数组件？','CDCDA-PLM, CIDERS'),
        ('Updates','训练协议','Where does learning run, and which updates travel?','训练放在哪里，传 activation、低维更新还是 scalar？','MobiLLM, FedKRSO, FedKSeed, pAirZero'),
        ('Tokens','协同解码','How should drafting, verification, and recovery interact?','draft、验证与 rejection 恢复如何协作？','AceSpec, Speculation at a Distance'),
        ('Embodied','具身控制','How should perception, policy inference, and control be split between a robot and remote compute under delay and bandwidth limits?','机器人与远端算力之间如何划分感知、策略推理与控制，以应对时延与带宽限制？','CloudEdgeVLA, RoboECC, EcoVLA'),
    ]
    for en,cn,q,qcn,ex in taxonomy:
        intro += f'| {cn if zh else en} | {qcn if zh else q} | {ex} |\n'
    intro += ('\n分类是主入口，论文可以跨多个优化对象；例如 Co-Skill 同时涉及上传轨迹和下发指导。\n\n' if zh else '\nCategories are primary entry points, not mutually exclusive mechanisms: Co-Skill, for example, addresses both uploaded trajectories and downloaded guidance.\n\n')
    intro += ('## 建议阅读顺序\n\n- 内容与 skill：**Co-Skill → EcoAgent → TMO**。\n- 长程 agent 路由：**Hera → GAPG**。\n- 个性化：**CIDERS → CDCDA-PLM**。\n- Forward-only 训练：**FedKSeed → pAirZero**，以 **FedKRSO** 作一阶子空间对照。\n- 解码系统：**AceSpec → Speculation at a Distance**，同时检查延迟与吞吐。\n- GUI agent 的上传内容：**CORE → PAAC → PrivacyGuard**。\n- 机器人：**CloudEdgeVLA → RoboECC → EcoVLA**，区分模拟时延与真实测试平台。\n\n' if zh else '## Suggested reading paths\n\n- Content and skills: **Co-Skill → EcoAgent → TMO**.\n- Long-horizon routing: **Hera → GAPG**.\n- Personalization: **CIDERS → CDCDA-PLM**.\n- Forward-only learning: **FedKSeed → pAirZero**, with **FedKRSO** as a first-order subspace comparison.\n- Decoding systems: **AceSpec → Speculation at a Distance**, checking both latency and throughput.\n- What GUI agents upload: **CORE → PAAC → PrivacyGuard**.\n- Robots: **CloudEdgeVLA → RoboECC → EcoVLA**, separating simulated delays from real testbeds.\n\n')
    for key,en,cn in CATEGORIES:
        intro += f'<a id="{key}"></a>\n\n## {cn if zh else en}\n\n'
        if key=='adjacent':
            intro += ('以下工作提供可迁移思路，但不能当作已验证的 LLM/Agent 端云协同方法。\n\n' if zh else 'These works offer related ideas; they do not establish the corresponding LLM/agent edge–cloud transfer.\n\n')
        intro += ('| 版本日期 | 工作 | 贡献 | 资源 |\n| --- | --- | --- | --- |\n' if zh else '| Version date | Work | Contribution | Resources |\n| --- | --- | --- | --- |\n')
        for p in sorted((p for p in papers if p['category']==key),key=lambda p:p['version_date'],reverse=True):
            resources=f'[paper]({p["paper_url"]})'
            resources+=f' · [code]({p["code_url"]})' if p['code_url'] else (' · 代码未定位' if zh else ' · code not located')
            resources+=f' · [evidence](docs/evidence.md#{p["arxiv_id"].replace(".","-")})'
            summary=p['summary_zh' if zh else 'summary']
            intro+=f'| {p["version_date"]} · v{p["version"]} | **{p["name"]}** — [{p["title"]}]({p["paper_url"]}) | {summary} | {resources} |\n'
        intro+='\n'
    intro += ('## 相关资源\n\n' if zh else '## Related resources\n\n')
    intro += '- [Awesome-Gradient-Free-LLMOpt](https://github.com/zz1358m/Awesome-Gradient-Free-LLMOpt) — '+('ES/ZO 参数优化的配套阅读清单，也是本仓库组织形式的参考。\n\n' if zh else 'a complementary ES/ZO reading list and inspiration for the collection format.\n\n')
    intro += ('## 维护\n\n修改 `data/papers.json` 后运行 `python scripts/render.py`；提交前运行 `python scripts/render.py --check`。欢迎通过 Issue/PR 补充论文、作者代码、版本更新和设备实测信息。文献元数据与来源按条记录，研究建议单独存放。\n\n本仓库采用 [MIT License](LICENSE)；所链接论文、代码和数据集保留各自许可。\n' if zh else '## Maintenance\n\nEdit `data/papers.json`, then run `python scripts/render.py`; validate with `python scripts/render.py --check`. Issues and PRs for papers, author code, version updates, and real-device measurements are welcome. Source records accompany each entry; research proposals are kept separate.\n\nThis collection uses the [MIT License](LICENSE). Linked papers, code, and datasets retain their own licenses.\n')
    return intro

def evidence(data):
    out='# Evaluation evidence / 实验依据与边界\n\nThe notes below summarize checked paper pages; they are not independent reproductions. Missing measurements are not inferred. / 以下摘要来自核验的论文页面，不是独立复现；缺失的测量不作推断。\n\n'
    for p in data['papers']:
        anchor=p['arxiv_id'].replace('.','-')
        out+=f'<a id="{anchor}"></a>\n\n## {p["name"]}\n\n'
        out+=f'- **Version:** {p["version_date"]}, v{p["version"]}; first submitted {p["first_submitted"]}.\n'
        out+=f'- **Status:** {p["status"]}.\n'
        out+=f'- **Exchange:** {p["exchange"]}. / {p["exchange_zh"]}。\n'
        out+=f'- **Evidence:** {p["evidence"]}\n'
        out+=f'- **实验边界：** {p["evidence_zh"]}\n'
        out+=f'- **Sources:** [metadata]({p["source_urls"][0]}), [full text]({p["source_urls"][1]}). Checked {p["checked_on"]}.\n\n'
    return out

def bibtex(data):
    out='% Version-pinned arXiv records; year follows initial submission.\n\n'
    for p in data['papers']:
        key='arxiv'+p['arxiv_id'].replace('.','')
        title=p['title'].replace('&',r'\&')
        out+=f'@misc{{{key},\n  title = {{{{{title}}}}},\n  author = {{{" and ".join(p["authors"])}}},\n  year = {{{p["first_submitted"][:4]}}},\n  eprint = {{{p["arxiv_id"]}}},\n  archivePrefix = {{arXiv}},\n  note = {{Version {p["version"]}, {p["version_date"]}}},\n  url = {{{p["paper_url"]}}}\n}}\n\n'
    return out

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    data=json.loads((ROOT/'data/papers.json').read_text(encoding='utf-8'))
    validate(data)
    outputs={'README.md':readme(data),'README.zh-CN.md':readme(data,True),'docs/evidence.md':evidence(data),'references.bib':bibtex(data)}
    for relative,body in outputs.items():
        path=ROOT/relative
        if args.check:
            assert path.exists() and path.read_text(encoding='utf-8')==body, f'Stale generated file: {relative}'
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(body,encoding='utf-8')
    # Local Markdown file targets and explicit cross-file anchors.
    for path in ROOT.rglob('*.md'):
        text=path.read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)]+)\)',text):
            if target.startswith(('https://','http://','#','mailto:')):
                continue
            relative,_,anchor=target.partition('#')
            dest=path.parent/relative
            assert dest.is_file(), f'Broken local link: {path}: {target}'
            if anchor:
                assert f'id="{anchor}"' in dest.read_text(encoding='utf-8'), f'Broken explicit anchor: {target}'
    print(f'Validated {len(data["papers"])} papers, generated-file consistency, and local Markdown links.')

if __name__=='__main__':
    main()
