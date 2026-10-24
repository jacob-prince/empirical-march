# Repository map

The outer workspace holds context that may span more than one codebase. The inner `code/project-dev` directory holds the executable scientific project.

| Path | Role | Durable? |
|---|---|---|
| `literature/` | papers, manifests, extracted facts, and reading notes | yes |
| `meeting-notes/YYYY-MM-DD/` | dated decisions, reports, and presentation artifacts | yes |
| `labbook/` | cross-analysis log and dashboard | yes |
| `stimuli/` | shared stimulus assets and provenance | yes, if licensing permits |
| `assets/` | shared visual/source assets | yes |
| `outputs/` | exported deliverables | selected only |
| `code/project-dev/src/` | importable project logic | yes |
| `code/project-dev/tests/` | invariants, parity checks, regression tests | yes |
| `code/project-dev/registry/` | model/run metadata and public artifact pointers | yes |
| `code/project-dev/cluster/` | SLURM, environment, and submission policy | yes |
| `code/project-dev/analyses/takeN/` | chronological empirical record | yes |
| `code/project-dev/analyses/preprint_figures/takeN/` | curated paper argument | yes |

An analysis folder is the smallest complete scientific unit. It owns the question, executable sources, raw-enough result summaries, rendered evidence, current state, and human-readable report. The preprint layer may consume analyses, but analyses must never depend on a preprint figure for their only copy of a result.
