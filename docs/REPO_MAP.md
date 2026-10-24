# Repository map

The outer workspace holds material that may be shared across codebases. The inner `code/project-dev` directory holds the project code.

| Path | What it holds | Kept long-term? |
|---|---|---|
| `literature/` | papers, manifests, and reading notes | yes |
| `meeting-notes/YYYY-MM-DD/` | dated decisions, reports, and slides | yes |
| `labbook/` | project-wide log and dashboard | yes |
| `stimuli/` | shared stimuli and where they came from | yes, if the license allows |
| `assets/` | shared artwork | yes |
| `outputs/` | exported deliverables | selected only |
| `code/project-dev/src/` | importable project code | yes |
| `code/project-dev/tests/` | tests | yes |
| `code/project-dev/registry/` | model/run metadata and pointers to weights | yes |
| `code/project-dev/cluster/` | SLURM jobs, environment, and submission tools | yes |
| `code/project-dev/analyses/takeN/` | analyses in the order they were done | yes |
| `code/project-dev/analyses/preprint_figures/takeN/` | the paper figures | yes |

An analysis folder is the smallest complete unit. It holds the question, the code, small result files, figures, current status, and a readable report. Paper figures can use data from analyses, but an analysis should never rely on a paper figure folder for the only copy of a result.
