# Agent rules

The files in this repository are the project's memory. Before changing anything, read this file, the nearest `AGENTS.md` in the folder you are working in, the relevant `SKILL.md`, and that folder's `notes/STATE.md` and `notes/plan.md`.

## Scope

- Only touch files the request needs.
- Don't undo the user's changes or unrelated work.
- Don't turn a diagnosis into a fix, a pilot into a full run, or an analysis result into a paper claim unless asked.
- Don't launch cluster jobs just because they might be useful. Follow the cluster rules and record every launch.

## Doing the science

- Write down the question and what counts as success before running the test.
- Keep what you observed, what you infer, and what you decided separate.
- Prefer the smallest comparison that answers the question.
- Record failures, null results, dropped directions, and changes to the plan.
- Never pick a seed, example, threshold, or checkpoint because it makes the figure look better, unless the selection rule was written down beforehand and is reported.
- Don't overwrite raw results. Write a new version or a new numbered analysis, and note what it replaces.

## What goes where

- `scripts/`: code and job files.
- `results/`: small output files, tables, and manifests.
- `figures/`: rendered figures. Every figure must come from a script and a result file.
- `notes/plan.md`: question, prediction, comparison, exclusions, and pass/fail rule, written before the run.
- `notes/STATE.md`: short current status, enough to pick the work back up.
- `notes/decisions.md`: why things were decided, and changes in direction.
- `report.html`: readable summary of the analysis. Rebuild it when a figure or conclusion changes.
- `z-old/`: old figure versions. Not a place for current alternatives.

## Keeping STATE.md current

Update `STATE.md` when a job is launched, a result comes in, the pass/fail rule changes, work stops, or someone else takes over. Include job IDs, hashes, seeds, dates, paths, and the next step. Nobody should have to piece the status together from chat or terminal output.

## Checking your work

- Run tests after code changes.
- Render and look at every figure or report you changed.
- Check that the paths you reference exist and that reports use the latest outputs.
- Say what you checked and what you couldn't check.

## Security

Never commit or print passwords, private keys, TOTP secrets or codes, AWS credentials, access tokens, signed URLs, or config files that contain credentials. Document how to log in, not the login details. Use `.example` files with placeholders.

## Skills

Use `.agents/skills/empirical-march/SKILL.md` for numbered analyses, `.agents/skills/scientific-figures/SKILL.md` for any figure, and `.agents/skills/cannon-cluster/SKILL.md` for cluster work. Skills describe how to do a task; folder `AGENTS.md` files add rules for that folder. If two rules conflict, the more specific one wins unless the user says otherwise.
