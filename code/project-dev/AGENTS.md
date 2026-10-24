# Development-project rules

This directory is the executable scientific project. Read the repository `AGENTS.md` first.

- Keep importable logic in `src/project_name`; analysis scripts should call shared logic rather than duplicate it.
- Add or update tests when changing shared behavior.
- Notebooks demonstrate and inspect; they are not the only source of an algorithm or reported number.
- Keep model/run metadata in `registry/`, with immutable hashes and artifact provenance. Do not commit weights.
- Shared software changes and analysis-specific changes are separate concerns. An analysis task does not authorize a broad refactor.
- Run `python3 scripts/validate_structure.py` before handoff.
