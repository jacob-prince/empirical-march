---
name: scientific-figures
description: Use for creating or editing analysis, meeting, or preprint figures and their captions.
---

# Scientific figures

The figure is evidence, not decoration. One figure should make one point, and a reader should understand the comparison from the title, axes, legend, examples, and caption without reading console output.

## Source and provenance

- Every figure has a committed source file.
- Read data from `results/` or a preprint figure's `preproc_data/`; never type reported values into plotting code without a cited source.
- Record model hashes, seeds, sample counts, uncertainty definition, exclusions, and data paths in the caption or verification note.
- Use `z-old/` for retired renders. Do not overwrite the only evidence of a materially different version.

## Visual grammar

- Prefer an example stimulus or schematic before an abstract summary when it improves intuition.
- Use bold lowercase panel letters for multi-panel manuscript figures.
- Keep typography legible at final size and use a consistent house font.
- Keep colors semantic and stable across figures; do not use color merely to decorate.
- Every heatmap has a numeric colorbar. Compared heatmaps share limits.
- Avoid result sentences inside the plotting area. Interpretation belongs in the caption/report.
- Avoid dense subpanel grids when separate figures would make the reasoning clearer.

## Caption

Write a declarative lead, then one paragraph or line per panel. State what was measured and enough method to interpret it. End with the restrained conclusion and caveat. Do not claim causality from association or generality from one seed.

## Verification loop

1. Render the figure from a clean command.
2. Open the actual output at full resolution.
3. Check overlap, clipping, empty space, font size, color scale, panel order, raster quality, and whether labels match the data.
4. Cross-check key plotted values against result files.
5. Re-render until clean.
6. Rebuild the owning analysis report or preprint viewer document.

Do not present a figure that has not been visually inspected.
