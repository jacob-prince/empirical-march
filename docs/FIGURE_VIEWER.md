# Live figure page

The figure page lives in `code/project-dev/analyses/preprint_figures/take1`. It is a local web page that reads and writes ordinary files.

## Files

- `manuscript.json`: title, plan, figure order, captions, notes, and retired figures.
- `index.html`: the editable page and chat pane.
- `server.py`: local server. Reads and writes `manuscript.json` and handles the inbox, outbox, and status files.
- `inbox.jsonl`: saved edits and chat messages from the page (ignored by Git).
- `outbox.jsonl`: agent replies (ignored by Git).
- `status.json`: idle or working (ignored by Git).
- `working.sh`: the agent calls this to say what it is working on.
- `reply.sh`: the agent calls this to reply and set the status back to idle. `say.sh` does the same thing.
- `watch_inbox.py`: optional terminal watcher that prints new requests.

## Start

```bash
cd code/project-dev/analyses/preprint_figures/take1
python3 server.py 8767
# open http://127.0.0.1:8767
```

The server only listens on `127.0.0.1`. Don't expose it publicly, since it can edit `manuscript.json` and serve files from the preprint folder.

## Working with an agent

In your Claude Code or Codex session, say something like:

> Watch `analyses/preprint_figures/take1/inbox.jsonl`. For each new request, call `working.sh`, edit the figure code or manuscript, render and look at the output, update `manuscript.json`, then call `reply.sh` with what you did.

To see incoming requests in a terminal:

```bash
python3 watch_inbox.py
```

The page doesn't call a model API. It passes messages between the browser and the agent session you already have open, so no API keys are stored in the repository.

## Edit loop

1. You edit a heading, caption, or note and click **Save**, or send a chat message.
2. The server writes `manuscript.json` and adds a short record to `inbox.jsonl`.
3. The agent reads the request and calls `./working.sh "rebuilding Figure 2"`.
4. The agent edits the code or data, runs the figure script, looks at the render, and updates the figure path or caption in `manuscript.json`.
5. The agent calls `./reply.sh "Figure 2 rebuilt; shortened the caption and fixed the shared color scale."`.
6. The page sees the change, reloads the figure, shows the reply, and sets the status back to idle.

If you have unsaved edits in the browser when the file changes on disk, the page warns you instead of overwriting them.

## Figure folders

Each `figureN/` holds:

- the plotting code;
- `preproc_data/` with the small input files and a manifest saying where each one came from;
- `cluster/` for jobs needed only by this figure;
- `notes/STATE.md` for status and checks;
- `z-old/` for old versions;
- the current PNG.

The analysis folders remain the full record. The preprint folder only holds the data and code needed to rebuild the paper figure, with links back to the analyses it came from.
