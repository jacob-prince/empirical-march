# Agent operating contract

This repository treats the filesystem as durable scientific memory. Before changing anything, read this file, the nearest nested `AGENTS.md`, the relevant `SKILL.md`, and the active folder's `notes/STATE.md` and `notes/plan.md`.

## Scope

- Touch only files required by the request.
- Preserve user changes and unrelated work.
- Do not turn a diagnosis into an implementation, a pilot into a scale-up, or an analysis result into a manuscript claim without authorization.
- Do not launch paid or scarce compute merely because it would be useful. Follow the cluster rules and record the launch.

## Scientific discipline

- State the question and success criterion before running the test.
- Separate observation, inference, and decision.
- Prefer the smallest decisive comparison.
- Record failures, nulls, stopped directions, and protocol deviations.
- Never choose a seed, example, threshold, or checkpoint because it makes the figure look better unless that selection rule was stated and is disclosed.
- Do not overwrite raw results. Write a new version or a new numbered analysis and document the supersession.

## Folder ownership

- `scripts/`: executable sources and launch files.
- `results/`: small machine-readable outputs, tables, and manifests.
- `figures/`: rendered evidence; every figure must trace to a script and result.
- `notes/plan.md`: question, prediction, comparison, exclusions, and pass/fail rule written before the run.
- `notes/STATE.md`: concise current truth for resumption.
- `notes/decisions.md`: durable rationale and changes in direction.
- `report.html`: human-readable analysis record; rebuild after a material figure or conclusion changes.
- `z-old/`: visibly retired renders, never a dumping ground for active alternatives.

## Progress documentation

Update `STATE.md` when a job is launched, a result lands, a criterion changes, work stops, or ownership is handed off. Include exact job IDs, hashes, seeds, dates, paths, and the next action. Do not make readers reconstruct state from chat or terminal scrollback.

## Verification

- Run proportionate tests after code changes.
- Render and inspect every changed figure or report.
- Check that referenced paths exist and that reports use current outputs.
- Report what was verified and what could not be verified.

## Security

Never commit or print passwords, private keys, TOTP seeds/codes, AWS credentials, access tokens, signed URLs, or credential-bearing config files. Document the authentication workflow, not the credential. Use `.example` files with placeholders.

## Skills

Use `.agents/skills/empirical-march/SKILL.md` for numbered analysis work, `.agents/skills/scientific-figures/SKILL.md` for any scientific figure, and `.agents/skills/cannon-cluster/SKILL.md` for Cannon/FASRC work. Skills add procedure; nested `AGENTS.md` files add location-specific constraints. When rules conflict, the more specific applicable instruction wins unless the user says otherwise.
