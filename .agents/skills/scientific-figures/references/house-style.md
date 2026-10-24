# Scientific figure house style

Use this for analysis and paper figures. If the project has its own style module or accepted figures, those win over these defaults. Write down any deviation.

## Visual target

Figures should be sparse and readable by someone who doesn't know the project.

- Use a few large panels rather than many small plots.
- Show real stimuli when possible, not cartoons of what the model saw.
- Keep sentences out of data panels: short titles, short axis labels, small legends, and only the annotations you need.
- Put methods, interpretation, and headline numbers in the caption or report.
- Use the same colors, markers, and icons throughout the paper so the reader only has to learn them once.

## Physical geometry

Make the figure at its final print size. Don't make it big and shrink it later.

| element | default |
|---|---:|
| one-column width | 88 mm |
| two-column width | 180 mm |
| typical height | 60-130 mm, chosen by content |
| output | RGB PNG, white background, 300 dpi |

Use the smallest height that doesn't feel crowded. Fix empty space by changing panel sizes, axis limits, or layout, not by adding text.

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
- Bad title: `Model A is significantly better`
- Bad title: `Accuracy, targeting, and ablation results across seven models`

Use a centered panel title: a short noun phrase, with an optional smaller second line. Don't put methods, pass numbers, or results in titles.

## Axes and grids

- Show left and bottom spines only.
- Use outward ticks and a light gray y-grid (`alpha` about 0.35, line width about 0.5 pt).
- Add a faint zero line when meaningful.
- Use short noun-phrase labels with the metric or unit: `Pearson r`, `Accuracy`, `Distance (deg)`.
- Set axis limits from the meaningful range, not just the data range. Chance and negative values must stay visible.
- Avoid dual axes unless there is no clearer alternative.
- Use frameless legends or direct labels near line endpoints.

## Models, conditions, and baselines

Define labels, order, and colors once, in the shared style module.

- Labels say what is different about the model, not pilot numbers, run IDs, or hashes.
- Order models weakest to strongest: untrained/reference floors, feedforward/ablated baselines, then full models.
- Use gray for references and weak baselines; use a stable saturated progression such as purple → magenta → orange → green for ordered model families.
- Include weak baselines in every panel where the metric applies. If a metric doesn't apply to a model, leave it out using one shared rule, and say why.
- Draw chance, uniform, or reference lines as dashed gray lines with a small direct label.
- Color tick labels by the model or condition they name when that helps. Only rotate them if you have to.

Do not reorder conditions by observed performance unless the ordering itself is the declared analysis.

## Marks and uncertainty

- Show the summary statistic with the uncertainty interval defined by the analysis plan.
- When per-seed, per-subject, or per-item values exist and remain readable, show translucent jittered points behind the summary.
- Keep subjects, model seeds, and repeated trials distinct. Don't make trials look like independent subjects.
- State exactly what error bars represent.
- Do not print values on every bar. Put exact headline values in the caption or a table.

Points with error bars, or lines, are often better than bars for showing order, paired data, or distributions.

## Heatmaps and maps

- Every heatmap has a numeric colorbar with units or a clearly defined normalized scale.
- Panels compared by color share identical limits, colormap, and normalization.
- Use a perceptually ordered map for magnitude and a centered diverging map for signed change.
- Mark missing values explicitly; never map missingness to the same color as zero.
- For attention/spotlight overlays, use a transparent magnitude field over the real stimulus and a visible contour near half peak. Keep the stimulus readable beneath the overlay.

## Schematic panels

When the reader needs to understand the experiment or model first, make panel **a** a schematic.

- Walk left-to-right through stimulus → model/manipulation → measurement/readout.
- Use real stimuli and the same geometry used by the model.
- Use numbered black step circles or another restrained sequence cue only when the temporal order matters.
- Use bold flow arrows and stable architectural colors: give each component one color and keep it across every figure.
- Keep labels to a few words. Name the data panels the schematic feeds, such as `(b, c)`.
- Skip decorative brain icons and model details that don't matter for the test.

## Panel composition

- Order panels the way the reader should follow them, not the order the scripts were written.
- Align comparable axes and plot areas.
- Use lowercase bold panel letters at the upper left, outside the plotting area, one size larger than panel titles.
- Keep legends, colorbars, and labels from creating uneven panel widths.
- Use whitespace to separate conceptual groups, not to pad the page.

## Don't

- Result sentences or methods paragraphs inside panels.
- Value labels on every bar/point.
- 3D effects, shadows, gradients used as decoration, or unnecessary frames.
- Inconsistent fonts, local model nicknames, or colors that change meaning between figures.
- Cropped axes that hide a baseline or exaggerate a small effect.
- Separate heatmap scales for panels presented as direct comparisons.
- JPEG plot exports, screenshots of plots, or uninspected notebook renders.
- Agent or tool credits inside figures.
