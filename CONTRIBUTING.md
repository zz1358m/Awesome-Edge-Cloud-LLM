# Contributing

Add papers about LLM/agent edge–cloud collaboration with an explicit collaboration mechanism. Useful adjacent ideas may be included only when their scope and transfer limits are clear.

1. Edit `data/papers.json`; do not edit generated READMEs, evidence notes, or BibTeX directly.
2. Use the exact title and author metadata from a primary source. Pin the arXiv version and record its date separately from initial submission.
3. Choose a primary category: `skills`, `routing`, `context`, `personalization`, `training`, `decoding`, or `adjacent`.
4. Write concise English and Chinese summaries, exchanged-content descriptions, and evaluation boundaries.
5. Link author-associated code from the paper or official project page. If none is located, set `code_url` to `null` and `code_status` to `not located in checked paper pages`. Do not imply that code does not exist.
6. Record primary `source_urls`, `checked_on`, and publication status. Mark author-reported venue claims explicitly.
7. Run `python scripts/render.py` and `python scripts/render.py --check` using Python 3.10+; no dependencies are required.

The initial collection has a fixed coverage cutoff of 2026-10-09. A PR adding later work must also advance `cutoff` and explain the scope update. Old pinned versions can remain for reproducibility; update an entry deliberately when adopting a new version.

For evaluation notes, distinguish phone measurements, embedded boards, desktop/server model emulation, and simulated network conditions. Avoid ranking methods whose datasets, hardware, budgets, or quality metrics differ.

Research hypotheses belong in `docs/research-agenda.md`, with clear links to the closest prior work.
