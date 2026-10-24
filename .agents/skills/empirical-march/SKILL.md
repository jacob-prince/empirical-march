---
name: empirical-march
description: Use for creating, extending, checking, stopping, or handing off a numbered analysis under analyses/takeN.
---

# Empirical march

The numbered analyses are a chain of questions. New ones are added at the end; old ones are not rewritten. Each folder answers one main question.

## Before starting

1. Read the root and `analyses/` `AGENTS.md` files.
2. Read the analysis's `notes/plan.md`, `notes/STATE.md`, and latest report.
3. Restate the question, comparison, fixed inputs, exclusions, and pass/fail rule.
4. Check earlier analyses, the registry, the cluster queue and job history, and stored outputs for work that has already been done.
5. If you want to change the pass/fail rule after seeing data, stop and write down the proposed change before running anything.

## Folder layout

```text
NN_question_slug/
├── scripts/          code, SLURM files, condition lists, report builder
├── results/          small JSON/CSV/TSV/NPZ summaries
├── figures/          rendered figures
├── notes/
│   ├── plan.md       question and pass/fail rule, written first
│   ├── STATE.md      current status
│   └── decisions.md  why things were decided
├── report.md         report text
└── report.html       built from report.md
```

## While working

- Write outputs to named files. Don't leave a temporary scratch file as the only copy.
- Record the seed, dataset and split, checkpoint hash, code commit, command or config, date, and storage path.
- Record cluster job IDs as soon as you submit.
- Keep failed outputs if they explain a decision, and label them.
- Update `STATE.md` after each batch of work, not only at the end of a long session.

## Before calling it done

- The pass/fail rule was applied exactly as written, or any change is stated up front.
- Every number that matters is in a small result file or table.
- Every result that matters has a figure, or a reason it doesn't need one.
- Each figure comes from a script and named inputs.
- The report states the result, the main caveat, and the decision.
- `STATE.md` says done, stopped, or superseded, and names the next question.

## New analysis or new take

Make the next numbered folder when the question changes. Start a new `takeN` when the main question, the type of data, or the standard of evidence changes. Never renumber old work to make the history look tidier.
