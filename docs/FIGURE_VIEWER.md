# Live figure viewer and agent-edit loop

The viewer lives in `code/project-dev/analyses/preprint_figures/take1`. It is a local manuscript surface backed entirely by ordinary files.

## Files

- `manuscript.json`: source of truth for title, plan, ordered figures, captions, notes, and archive.
- `index.html`: editable manuscript page plus chat pane.
- `server.py`: localhost-only HTTP server; reads/writes the document atomically and exposes inbox/outbox/status endpoints.
- `inbox.jsonl`: saved edits and chat messages sent from the page; ignored by Git.
- `outbox.jsonl`: agent replies; ignored by Git.
- `status.json`: idle/working state; ignored by Git.
- `working.sh`: agent announces the task in progress.
- `reply.sh`: agent posts a response and returns status to idle; `say.sh` is a compatibility alias.
- `watch_inbox.py`: optional terminal watcher for new requests.

## Start

```bash
cd code/project-dev/analyses/preprint_figures/take1
python3 server.py 8767
# open http://127.0.0.1:8767
```

The server binds only to `127.0.0.1`. Do not bind it publicly: it can edit `manuscript.json` and serve figure files from the preprint subtree.

## Work with an agent

In the active Codex or Claude task, say:

> Watch `analyses/preprint_figures/take1/inbox.jsonl`. For each new request, call `working.sh`, edit the figure source or manuscript, render and inspect the output, update `manuscript.json`, then call `reply.sh` with the result.

The optional watcher shows incoming records:

```bash
python3 watch_inbox.py
```

The page does not invoke a model API. It is a transparent communication queue between a browser and an already-authorized agent session. That is intentional: no API key or agent credential is stored in the repository.

## Edit loop

1. Jacob edits a heading, caption, or note and clicks **Save**, or sends a chat message.
2. The server atomically writes `manuscript.json` and appends a compact record to `inbox.jsonl`.
3. The agent reads the request and calls `./working.sh "rebuilding Figure 2"`.
4. The agent edits source/data, runs the figure script, visually inspects the render, and updates the figure path/caption in `manuscript.json`.
5. The agent calls `./reply.sh "Figure 2 rebuilt; shortened the caption and corrected the shared color scale."`.
6. Browser polling sees the document version change, refreshes the figure, displays the reply, and returns the status dot to idle.

If Jacob has unsaved browser edits while the document changes on disk, the page warns instead of silently replacing them.

## Figure-folder contract

Each `figureN/` owns:

- the assembly/plotting source;
- `preproc_data/` with compact promoted inputs and a provenance manifest;
- `cluster/` for figure-specific remote extraction/evaluation;
- `notes/STATE.md` for current status and verification;
- `z-old/` for retired visual versions;
- the current rendered PNG(s).

The analysis tree remains the scientific record. The preprint folder contains only the data and code needed to reproduce the curated figure, with links back to the originating analyses.
