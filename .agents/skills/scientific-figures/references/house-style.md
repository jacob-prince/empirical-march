# Jacob scientific figure house style

Use this reference for analysis and manuscript figures. Project-specific style helpers and accepted reference figures override generic defaults, but deviations should be deliberate and recorded.

## Visual target

The target is the AccentuateVVS/VisCogNet manuscript look: sparse, figure-first, and readable without knowing the project.

- Prefer a few large, coherent panels over a mosaic of small plots.
- Use real example stimuli when possible. Avoid cartoon substitutes for inputs the model actually saw.
- Keep data panels nearly sentence-free: short titles, short axis labels, compact legends, and necessary annotations only.
- Put methods, interpretation, and headline numbers in the caption/report.
- Use a stable visual grammar across the paper so the reader learns the colors, marks, and architectural icons once.

## Physical geometry

Author at final print size rather than shrinking an oversized canvas later.

| element | default |
|---|---:|
| one-column width | 88 mm |
| two-column width | 180 mm |
| typical height | 60-130 mm, chosen by content |
| output | RGB PNG, white background, 300 dpi |

Use the smallest height that avoids crowding. Fix dead space with panel ratios, axis limits, or layout—not by filling it with extra text.

## Type and line scale

Use Helvetica Neue Regular with Arial fallback. Avoid light weights. At final size:

| element | size/style |
|---|---|
| panel title | 8.5 pt |
| optional title qualifier | 6.5 pt |
| axis label | 7 pt |
| tick/legend text | 6 pt |
| panel letter | 10 pt, bold lowercase |
| figure/group title | 9 pt |
| schematic annotation | 5.5 pt minimum |
| axis spines/ticks | 0.8 pt |
| primary line | 1.5 pt |
| marker | about 4 pt |
| error-bar cap | about 2 pt |

Use regular math text for symbols. Do not allow text below 5 pt at final size.

## Title grammar

Figure and panel titles name the analysis, not the outcome.

- Good figure title: `Inset targeting by training task`
- Good panel title: `Encoding score` with qualifier `Natural test images`
- Bad title: `The dorsal model is significantly better`
- Bad title: `Accuracy, targeting, and ablation results across seven models`

Prefer a centered two-line panel title: a short noun phrase plus an optional smaller qualifier. Do not put methods, pass numbers, or results in titles.

## Axes and grids

- Show left and bottom spines only.
- Use outward ticks and a light gray y-grid (`alpha` about 0.35, line width about 0.5 pt).
- Add a faint zero line when meaningful.
- Use short noun-phrase labels with the metric or unit: `Pearson r`, `Accuracy`, `Distance (deg)`.
- Set limits from the scientific scale, not only the observed values. Chance-level and negative results must remain visible.
- Avoid dual axes unless there is no clearer alternative.
- Use frameless legends or direct labels near line endpoints.

## Models, conditions, and baselines

Define labels, order, and colors once in the shared style module.

- Labels state what scientifically differs, not pilot numbers, run IDs, or hashes.
- Order models weakest to strongest: untrained/reference floors, feedforward/ablated baselines, then full models.
- Use gray for references and weak baselines; use a stable saturated progression such as purple → magenta → orange → green for ordered model families.
- Include weak baselines in every panel where the metric is defined. If a metric is undefined for a model, filter it through one shared availability rule and state why.
- Draw chance, uniform, or reference lines as dashed gray lines with a small direct label.
- Color categorical tick labels by the condition/model they name when that improves reading; rotate only when necessary.

Do not reorder conditions by observed performance unless the ordering itself is the declared analysis.

## Marks and uncertainty

- Show the summary statistic with the uncertainty interval defined by the analysis plan.
- When per-seed, per-subject, or per-item values exist and remain readable, show translucent jittered points behind the summary.
- Distinguish biological subjects, model seeds, and repeated trials; do not visually imply that trials are independent subjects.
- State exactly what error bars represent.
- Do not print values on every bar. Put exact headline values in the caption or a table.

Prefer points/intervals or lines to bars when they show ordering, paired structure, or distributions more honestly.

## Heatmaps and maps

- Every heatmap has a numeric colorbar with units or a clearly defined normalized scale.
- Panels compared by color share identical limits, colormap, and normalization.
- Use a perceptually ordered map for magnitude and a centered diverging map for signed change.
- Mark missing values explicitly; never map missingness to the same color as zero.
- For attention/spotlight overlays, use a transparent magnitude field over the real stimulus and a visible contour near half peak. Keep the stimulus readable beneath the overlay.

## Schematic panels

When the reader needs the experimental or model logic, use panel **a** as the schematic.

- Walk left-to-right through stimulus → model/manipulation → measurement/readout.
- Use real stimuli and the same geometry used by the model.
- Use numbered black step circles or another restrained sequence cue only when the temporal order matters.
- Use bold flow arrows and stable architectural colors. In the VisCogNet grammar: ventral blue, dorsal orange/purple, feedback red, feature taps dashed blue, readout/selected output teal.
- Keep labels to a few words. Name the data panels the schematic feeds, such as `(b, c)`.
- Avoid decorative brain icons or architectural detail that does not affect the test.

## Panel composition

- Put panels in the reader's causal or processing order, not the order scripts were written.
- Align comparable axes and plot areas.
- Use lowercase bold panel letters at the upper left, outside the plotting area, one size larger than panel titles.
- Keep legends, colorbars, and labels from creating uneven panel widths.
- Use whitespace to separate conceptual groups, not to pad the page.

## Forbidden patterns

- Result sentences or methods paragraphs inside panels.
- Value labels on every bar/point.
- 3D effects, shadows, gradients used as decoration, or unnecessary frames.
- Inconsistent fonts, local model nicknames, or colors that change meaning between figures.
- Cropped axes that hide a baseline or exaggerate a small effect.
- Separate heatmap scales for panels presented as direct comparisons.
- JPEG plot exports, screenshots of plots, or uninspected notebook renders.
- Agent/vendor attribution inside scientific figures.
