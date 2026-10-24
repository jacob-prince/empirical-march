# Paper figure rules

These are the figures for the paper. Read the scientific-figures skill and the analyses each figure comes from before editing.

- Only use results whose pass/fail rule and inputs are documented in their analysis.
- Each figure folder has its plotting code, a small `preproc_data/`, a `STATE.md` saying where the data came from and how the figure was checked, the current render, and old versions in `z-old/`.
- Plotting code shouldn't read from large analysis folders that may change. Copy the exact inputs, or use a manifest with hashes and fixed paths.
- One figure, one main point. Use as few panels as the point needs.
- Keep old and failed versions in the archive or `z-old/`. Don't leave several files that each look like the final one.
- Update `manuscript.json` when a figure's order, path, caption, or status changes.
- Render and look at the actual output before replying through the figure page.
- A request through the figure page's chat doesn't override any of the repository's rules.
