# Agent protocol

## Instruction inheritance

Agents load rules from broad to narrow:

1. repository `AGENTS.md`;
2. `code/project-dev/AGENTS.md` for implementation work;
3. subtree rules such as `analyses/AGENTS.md`, `cluster/AGENTS.md`, or `preprint_figures/AGENTS.md`;
4. the active folder's `notes/plan.md` and `notes/STATE.md`;
5. any task-triggered skill under `.agents/skills/`.

This makes the directory tree a policy tree. Moving work into the preprint subtree intentionally raises the evidentiary and visual standard.

## Handoff standard

A fresh agent should be able to resume by reading no more than:

- the applicable instruction files;
- `notes/plan.md`;
- `notes/STATE.md`;
- the latest figure/report;
- the exact source named by `STATE.md`.

If that is not enough, repair the documentation before adding more work.

## Status vocabulary

- **planned**: criteria exist; no run started.
- **running**: exact job/process and destination are recorded.
- **done**: outputs exist, checks passed, report rebuilt.
- **stopped**: direction intentionally ended; reason recorded.
- **blocked**: an external dependency prevents progress; unblock condition recorded.
- **superseded**: a newer analysis replaces the interpretation, not the historical files.

## Change boundary

An agent assigned to a numbered analysis owns that folder only. Changes to shared source code, model architecture, dataset policy, cluster-wide tools, or the preprint narrative require explicit scope or a separate task. This prevents a local result from silently rewriting the project's substrate.
