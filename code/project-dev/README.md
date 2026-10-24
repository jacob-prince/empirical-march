# project-dev

Rename this folder and the `project_name` package for your project. This folder holds the code, tests, model metadata, cluster files, and all the analyses.

```bash
uv sync
uv run pytest
python3 scripts/new_analysis.py --take take1 --name first_question
python3 scripts/validate_structure.py
```

See the root README for the workflow, and read the `AGENTS.md` files before editing a folder.
