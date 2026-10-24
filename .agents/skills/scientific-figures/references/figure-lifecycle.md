# Making a figure, start to finish

Use this for any figure that goes into an analysis report, a meeting, or the paper.

## 1. Decide what the figure is for

Before plotting, write one sentence for each:

- the question the figure answers;
- the main comparison and metric;
- the pass/fail rule;
- the one conclusion the figure can support;
- the biggest caveat or alternative explanation.

If the panels answer several unrelated questions, split the figure or explain why they belong together.

## 2. Fix the inputs and selection rules

Before choosing examples or running a big render, write down:

- dataset, split, preprocessing, and sample count;
- model or checkpoint hashes and their labels;
- seeds or subjects, and what counts as a replicate;
- exclusions and how missing data are handled;
- how examples are chosen;
- how uncertainty is computed;
- what chance or the reference level is.

Use typical examples or examples picked by a rule. If you hand-pick an example to explain something, say so, and check that it isn't unusual.

## 3. Know where the data come from

An analysis figure reads its own `results/` files. A paper figure reads small copied inputs in `preproc_data/`, or a manifest that points to files that won't change.

For each copied input, record:

| field | what to write |
|---|---|
| source analysis | numbered folder and result file |
| how it was made | job ID, checkpoint/model hash, seed, code commit |
| processing | filtering, averaging, or other steps applied |
| check | checksum, row count, array shape, or similar |
| used in | which panel(s) |

Never use a number typed into the plot script without a record of where it came from. Never use a `latest` link, a scratch folder, or notebook state as the only source.

## 4. Plan the panels

A common order is:

1. **What was shown or changed?** A real example or a schematic.
2. **What was measured?** A picture of the measure, if it isn't obvious.
3. **What is the main result?** All models, with error bars and a reference.
4. **Does it hold up under the key control?** Only the controls the claim needs.

Don't add a panel just because the result exists. A supplementary figure is often better than a crowded main figure.

## 5. Build from shared code

- Import fonts, sizes, colors, model order, panel letters, grids, and save settings from the shared style module.
- Keep data loading and averaging separate from plotting when the computation isn't trivial.
- Make the render command repeatable and runnable from the project root.
- Save the current render to one fixed path. Move clearly different old versions to `z-old/`, with a date or description in the name.

## 6. Write the caption from the same data

Structure:

1. **Bold first sentence:** the specific result the figure shows.
2. `(a) ...` through `(n) ...`: what each panel shows. Define markers, error bars, sample size, reference lines, abbreviations, and how anything was selected.
3. **Reading:** one or two sentences linking the panels to the pass/fail rule.
4. **Caveat:** the main limit or failure that affects the reading.

Pull counts and key numbers from the result files when you can. A caption that matches what the plot shows still needs to be checked against the stored data.

## 7. Render and look

Render at 88 or 180 mm wide and the intended final height. Then look at:

- the whole image at normal size;
- the image at full resolution;
- zoomed crops of dense areas, small legends, and the edges of titles and panel letters;
- stimulus detail and map overlays;
- the caption next to the figure in the actual report or page.

Check that:

- nothing overlaps or is clipped;
- there are no large empty areas;
- all text is readable at final size;
- panel letters and reading order are right;
- legends and labels match the shared definitions;
- axes and color scales that should match do match;
- error bars and `n` match the results;
- the weakest baseline and chance or reference are visible;
- the conclusion still holds without relying on the chosen example.

Re-render after every layout change. Checking an earlier version doesn't count for the new one.

## 8. Put it in the report or paper

For an analysis figure:

- put the PNG in `figures/` and the code in `scripts/`;
- update the caption or report text;
- rebuild and look at `report.html`;
- update `notes/STATE.md` with the result and decision.

For a paper figure:

- keep the code, `preproc_data/`, `notes/STATE.md`, `cluster/`, and `z-old/` inside `figureN/`;
- update the PNG path, heading, caption, source, and notes in `manuscript.json`;
- start the local figure page and check that it refreshes;
- if working through the page's chat, call `working.sh` before editing and `reply.sh` only after you have checked the render and the page.

A chat request doesn't replace the notes. Any scientific decision made while editing goes in the figure's or analysis's `STATE.md`.

## 9. Handoff notes

Before calling the figure done, `notes/STATE.md` should list:

- the claim and the analyses it comes from;
- the current render and code paths;
- the copied inputs and how they were checked;
- the render command;
- the number checks you did;
- the visual checks you did, and at what resolution;
- known caveats and failed versions;
- the next editing or scientific step.

"Looks good" is not enough.
