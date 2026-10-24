# How agents read the repository

## Which rules apply

Agents read rules from general to specific:

1. the root `AGENTS.md`;
2. `code/project-dev/AGENTS.md` for code changes;
3. folder rules such as `analyses/AGENTS.md`, `cluster/AGENTS.md`, or `preprint_figures/AGENTS.md`;
4. the current folder's `notes/plan.md` and `notes/STATE.md`;
5. any skill under `.agents/skills/` that fits the task.

So the folder you work in decides the rules you follow. Work in the preprint folder has a higher bar for evidence and figure quality.

## Handoffs

A new agent should be able to pick up the work by reading only:

- the `AGENTS.md` files that apply;
- `notes/plan.md`;
- `notes/STATE.md`;
- the latest figure or report;
- the code file named in `STATE.md`.

If that isn't enough, fix the notes before doing more work.

## Status words

- **planned**: the pass/fail rule is written; nothing has run.
- **running**: the job or process and its output path are recorded.
- **done**: outputs exist, checks passed, report rebuilt.
- **stopped**: dropped on purpose; reason recorded.
- **blocked**: waiting on something outside the analysis; what would unblock it is recorded.
- **superseded**: a newer analysis replaces the interpretation. The old files stay.

## Staying in your lane

An agent working on a numbered analysis only changes that folder. Changes to shared code, model architecture, dataset choices, cluster tools, or the paper figures need to be asked for, or done as a separate task. This keeps one analysis from quietly changing the rest of the project.
