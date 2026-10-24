# Code rules

This folder is the project code. Read the root `AGENTS.md` first.

- Put reusable code in `src/project_name`. Analysis scripts should call it rather than copy it.
- Add or update tests when you change shared code.
- Notebooks are for demos and poking around. They should never be the only copy of a method or a reported number.
- Keep model/run metadata in `registry/`, with fixed hashes and where the weights are stored. Don't commit weights.
- Changes to shared code and changes for one analysis are separate tasks. Working on an analysis is not a reason for a big refactor.
- Run `python3 scripts/validate_structure.py` before handing off.
