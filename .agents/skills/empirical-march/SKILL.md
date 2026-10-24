---
name: empirical-march
description: Use for creating, extending, auditing, stopping, or handing off a numbered scientific analysis under analyses/takeN.
---

# Empirical march

The numbered analysis tree is an append-only chain of questions. One folder should answer one main question with one main evidentiary point.

## Before work

1. Read the root and analysis `AGENTS.md` files.
2. Read the analysis `notes/plan.md`, `notes/STATE.md`, and latest report.
3. Restate the question, comparison, fixed inputs, exclusions, and pass/fail criterion.
4. Search prior analyses, the registry, cluster queue/accounting, and stored outputs for duplicate work.
5. If the result would require changing the criterion after seeing data, stop and record the proposed change before running it.

## Folder contract

```text
NN_question_slug/
├── scripts/          local programs, SLURM files, rosters, report builder
├── results/          JSON/CSV/TSV/NPZ summaries small enough to track
├── figures/          rendered evidence
├── notes/
│   ├── plan.md       pre-stated question and decision rule
│   ├── STATE.md      current resumable truth
│   └── decisions.md  durable rationale
├── report.md         narrative source
└── report.html       rebuilt human-readable record
```

## During work

- Write deterministic outputs to named destinations; do not use an anonymous scratch file as the only copy.
- Record seed, dataset/split, checkpoint hash, code commit, command/config, date, and storage location.
- Log cluster job IDs immediately after submission.
- Preserve failed outputs when they explain a decision; label them clearly.
- Update `STATE.md` at batch boundaries, not after a long chat has already become the only record.

## Evidence gate

Before calling an analysis done:

- the stated criterion is evaluated exactly as written, or the deviation is prominent;
- every consequential number is in a small result file or table;
- every consequential result has a figure or explicit reason it does not need one;
- the figure traces to a script and inputs;
- the report states the result, caveat, and decision;
- `STATE.md` says done/stopped/superseded and names the next question.

## Escalation into a new analysis or take

Create the next numbered folder when the scientific question changes. Start a new `takeN` when the organizing thesis, dataset regime, or evidentiary standard changes. Never renumber old work to manufacture a cleaner history.
