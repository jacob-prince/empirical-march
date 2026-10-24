# Figure lifecycle, provenance, and manuscript promotion

Use this reference for any figure that enters an analysis report, meeting decision, or preprint take.

## 1. Define the evidentiary job

Before plotting, write one sentence for each:

- the question the figure answers;
- the primary comparison and metric;
- the pre-stated decision criterion;
- the one conclusion the complete figure may support;
- the strongest caveat or alternative explanation.

If the proposed panels answer multiple independent questions, split the figure or justify the grouping.

## 2. Freeze the roster and selection rules

Record before choosing examples or running a large render:

- dataset, split, preprocessing, and sample count;
- model/checkpoint hashes and human-readable labels;
- seeds/subjects and the unit of replication;
- exclusions and missing-data handling;
- example-selection rule;
- uncertainty/statistical method;
- chance/reference definition.

Use representative or rule-selected examples. If an example is hand-chosen for pedagogy, say so and verify that it does not contradict the distribution.

## 3. Establish the data boundary

An analysis figure reads its owning `results/` files. A preprint figure reads compact promoted inputs under `preproc_data/` or a manifest that points to immutable external artifacts.

For each promoted input, record:

| field | requirement |
|---|---|
| source analysis | numbered folder and result file |
| production identity | job ID, checkpoint/model hash, seed, code commit |
| selection/transformation | exact filtering, aggregation, or preprocessing |
| integrity | checksum, record count, dimensions, or another stable check |
| role | panel(s) that consume it |

Never use an undocumented value typed into the plot script. Never rely on a mutable `latest`, scratch glob, or private notebook state as the only source.

## 4. Design the panel argument

A common sequence is:

1. **What was shown or manipulated?** Real example or schematic.
2. **What was measured?** Visual definition of the response/metric if it is not obvious.
3. **What is the primary result?** Full roster, uncertainty, and reference.
4. **Does the interpretation survive the decisive control?** Only controls needed for the claim.

Do not add panels because the result already exists. A useful supplementary figure may be better than a crowded main figure.

## 5. Implement from shared primitives

- Import typography, dimensions, semantic colors, model order, panel letters, grids, and save behavior from the shared style module.
- Keep data loading/aggregation separate from drawing when the computation is non-trivial.
- Make the render command deterministic and runnable from the project root.
- Save the current render to one stable, documented path. Timestamp or move materially different retired versions into `z-old/`.

## 6. Caption from the same data

Use this structure:

1. **Bold declarative lead:** the narrow result the figure establishes.
2. `(a) ...` through `(n) ...`: what each panel shows; define marks, error bars, sample size, reference lines, abbreviations, and any selection.
3. **Reading:** one or two sentences connecting the panels to the criterion.
4. **Caveat:** the main boundary or failure that changes interpretation.

Generate key counts and numbers from result files when possible. A caption is not verified merely because it describes the visible marks; cross-check it against the stored data.

## 7. Render and inspect

Render at 88 or 180 mm width and the intended final height. Then inspect:

- the full image at normal reading scale;
- the full-resolution image;
- crops of dense regions, small legends, and title/panel-letter boundaries;
- stimulus detail and map overlays;
- the caption beside the figure in its actual report/viewer.

Check these invariants:

- no overlaps or clipping;
- no large accidental dead space;
- all text legible at final size;
- panel letters and reading order correct;
- legends and labels agree with central definitions;
- compared axes/scales actually match;
- uncertainty and `n` agree with results;
- the weakest baseline and chance/reference are visible;
- the conclusion remains true without relying on the chosen example.

Re-render after every layout-affecting change. Inspection of an earlier version does not validate the new render.

## 8. Integrate with reports and the live manuscript viewer

For an analysis figure:

- place the PNG in `figures/` and source in `scripts/`;
- update the caption/report source;
- rebuild and inspect `report.html`;
- update `notes/STATE.md` with the result and decision.

For a preprint figure:

- keep source, `preproc_data/`, `notes/STATE.md`, figure-specific `cluster/`, and `z-old/` under `figureN/`;
- update the current relative PNG path, heading, caption, source, and notes in `manuscript.json`;
- start the localhost viewer and verify the page refreshes;
- if working through the viewer chat, call `working.sh` before the edit and `reply.sh`/`say.sh` only after the render and page are verified.

The chat request does not replace documentation. Any scientific decision made during the edit belongs in the figure or analysis state file.

## 9. Handoff record

Before declaring the figure done, `notes/STATE.md` should include:

- the claim and originating analyses;
- current render and source paths;
- promoted inputs and provenance checks;
- the render command;
- numerical cross-checks performed;
- visual inspection performed and at what resolution;
- known caveats or failed variants;
- the next editorial/scientific action.

“Looks good” is not a sufficient verification record.
