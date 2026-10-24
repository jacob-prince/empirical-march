---
name: scientific-figures
description: Create or edit house-style scientific analysis and manuscript figures, including panel design, house styling, captions, provenance, rendering, and visual verification. Use for plots, schematics, figure assembly, figure reports, and preprint-figure promotion. Do not use for slide-deck layout or generic product/dashboard charts.
---

# Scientific figures

A figure is a compact evidentiary argument. It must remain understandable at final print size, trace every displayed value to a result, and make one main point without requiring console output or project folklore.

## Required context

Before editing a figure:

1. Read the applicable `AGENTS.md`, the owning analysis `notes/plan.md` and `notes/STATE.md`, and the current report or manuscript caption.
2. Identify the exact result files, model/checkpoint roster, seeds, exclusions, uncertainty definition, and pre-stated decision rule.
3. Find the project's central `figstyle.py`, model-label/order table, and schematic helpers. Extend those shared definitions rather than inventing local styles or labels.
4. Open one or two accepted house-style figures at full resolution. Match their density, hierarchy, and final-size legibility.

Read [references/house-style.md](references/house-style.md) for the exact geometry, typography, axes, colors, model ordering, schematics, and output conventions. For any analysis-report or preprint figure, also read [references/figure-lifecycle.md](references/figure-lifecycle.md) for provenance, promotion, caption, viewer, and verification requirements.

## Figure contract

- One figure makes one main point. Every panel either establishes the design, provides the primary evidence, supplies a necessary control, or is removed.
- When the task is unfamiliar, panel **a** should usually ground the reader with the real stimulus, trial, model path, or measurement schematic before summary statistics.
- Titles name the analysis, not the finding. Findings and numbers belong in the caption/report.
- Multi-panel figures use bold lowercase panel letters in reading order.
- Weak baselines, chance/reference lines, and uncertainty appear whenever defined. Do not crop axes or filter models in a way that hides a floor or failure.
- Compared heatmaps share one scale and each heatmap has a numeric colorbar.
- Use semantic colors consistently across the project. Never change a model/condition color to improve a single panel.
- Keep interpretation, methods paragraphs, and value labels out of data panels. The plot should contain only what is needed to read the comparison.

## Data and provenance

- Read plotted values from machine-readable `results/` files or a preprint figure's documented `preproc_data/`. Do not transcribe headline values into plotting code.
- Make selection rules explicit. Do not choose seeds, examples, checkpoints, thresholds, or units because they improve the appearance after looking at the result.
- Record source analysis, result path, run/job ID, model hash, seed, sample count, exclusions, and uncertainty calculation in the caption or verification record.
- Preserve materially different prior renders in `z-old/`. Keep one unambiguous current figure path.
- A preprint figure must be rebuildable from its source plus promoted inputs or a stable manifest; it must not depend silently on mutable scratch state.

## Caption contract

Keep captions outside the image. Start with a short bold declarative lead stating the result, then describe each panel in order using `(a)`, `(b)`, and so on. Define marks, error bars, sample size, chance/reference lines, abbreviations, and the model roster. End with the restrained reading and its main caveat. Pull key numbers programmatically from the same result files used by the plot.

Do not claim causality from association, generality from one seed, or success when the pre-stated criterion failed.

## Required verification loop

1. Render from a clean, recorded command at final physical dimensions.
2. Open the actual output, not only a notebook or plotting window.
3. Inspect the whole figure and dense regions at full resolution. Check clipping, overlaps, whitespace, panel alignment, type size, raster quality, legends, tick labels, shared scales, and reading order.
4. Cross-check displayed values, `n`, uncertainty, examples, and labels against source results.
5. Compare once against an accepted house reference. If the new figure is denser, wordier, or smaller-typed, simplify it.
6. Re-render until clean, then rebuild the owning `report.html` or update `manuscript.json` and the live viewer.
7. Record the verification and any unresolved limitation in the figure or analysis `STATE.md`.

Never present or hand off a render that has not been visually inspected.

## Output boundary

Analysis figures live with the analysis; manuscript figures live in `analyses/preprint_figures/takeN/figureN/`. Generated plots are PNG at 300 dpi by default, on a white RGB background. Do not use JPEG for plots. Create vector output only when the project or submission workflow explicitly requires it.
