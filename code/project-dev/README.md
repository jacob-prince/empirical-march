# project-dev

Rename this directory and the `project_name` package for the new project. This inner project owns executable code, tests, model metadata, cluster infrastructure, and the full empirical march.

```bash
uv sync
uv run pytest
python3 scripts/new_analysis.py --take take1 --name first_question
python3 scripts/validate_structure.py
```

See the repository root README for the research workflow and the applicable `AGENTS.md` files before editing a subtree.
