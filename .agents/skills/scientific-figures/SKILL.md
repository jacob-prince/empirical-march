---
name: scientific-figures
description: Create or edit analysis and paper figures in the lab style, including panel layout, styling, captions, tracking where the data came from, rendering, and checking the output. Use for plots, schematics, figure assembly, figure reports, and moving figures into the paper. Not for slide layout or dashboard charts.
---

# Scientific figures

A figure should make one main point, be readable at final print size, and show only values that come from a result file. A reader should not need console output or inside knowledge of the project to understand it.

## Before editing a figure

1. Read the `AGENTS.md` files that apply, the analysis's `notes/plan.md` and `notes/STATE.md`, and the current report or caption.
2. Find the result files, the list of models or checkpoints, seeds, exclusions, how uncertainty is computed, and the pass/fail rule.
3. Find the project's shared `figstyle.py`, its model label and order table, and any schematic helpers. Add to those rather than making local styles or labels.
4. Open one or two accepted figures from the project at full resolution, and match their density and text size.

See [references/house-style.md](references/house-style.md) for sizes, fonts, axes, colors, model order, schematics, and file format. For any report or paper figure, also see [references/figure-lifecycle.md](references/figure-lifecycle.md) for captions, moving figures into the paper, the live figure page, and checking renders.

## Figure rules

- One figure, one main point. Each panel shows the design, the main result, or a needed control. Otherwise drop it.
- If the task is unfamiliar, panel **a** usually shows the real stimulus, trial, model path, or measurement before any summary plots.
- Titles name the analysis, not the finding. Findings and numbers go in the caption or report.
- Label panels with bold lowercase letters in reading order.
- Show weak baselines, chance or reference lines, and error bars whenever they exist. Don't crop axes or drop models in a way that hides a floor or a failure.
- Heatmaps being compared share one color scale, and each has a colorbar with numbers.
- Use the same color for a model or condition everywhere. Never change it to make one panel look better.
- Keep interpretation, methods text, and value labels out of the data panels.

## Data

- Read plotted values from `results/` files, or from a paper figure's `preproc_data/`. Don't type headline numbers into plotting code.
- Write down selection rules. Don't choose seeds, examples, checkpoints, thresholds, or units because they look better after seeing the result.
- Record the source analysis, result path, job ID, model hash, seed, sample count, exclusions, and how uncertainty was computed, in the caption or in `STATE.md`.
- Move clearly different old versions to `z-old/`. Keep one obvious current figure path.
- A paper figure must be rebuildable from its code plus its copied inputs or a fixed manifest. It must not depend on scratch files that might change.

## Captions

Keep captions out of the image. Start with a short bold sentence stating the result, then describe each panel in order with `(a)`, `(b)`, and so on. Define markers, error bars, sample size, chance or reference lines, abbreviations, and which models are shown. End with a cautious reading and the main caveat. Pull key numbers from the same result files the plot uses.

Don't claim causation from correlation, generality from one seed, or success when the pass/fail rule failed.

## Checking the render

1. Render at final size from a recorded command.
2. Open the actual output file, not just the notebook or plot window.
3. Look at the whole figure, and zoom into dense areas. Check for clipping, overlaps, empty space, alignment, text size, image quality, legends, tick labels, shared scales, and reading order.
4. Check the values, `n`, error bars, examples, and labels against the result files.
5. Compare once against an accepted figure. If the new one is denser, wordier, or has smaller text, simplify it.
6. Re-render until it's clean, then rebuild `report.html` or update `manuscript.json` and the live page.
7. Write what you checked, and anything still wrong, in `STATE.md`.

Never hand off a render you haven't looked at.

## Where figures go

Analysis figures live in the analysis folder. Paper figures live in `analyses/preprint_figures/takeN/figureN/`. Save plots as PNG at 300 dpi on a white background. Don't use JPEG for plots. Only make vector files when the project or journal asks for them.
