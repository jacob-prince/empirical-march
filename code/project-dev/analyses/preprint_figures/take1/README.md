# Preprint figures, take1

A local page for viewing and editing the paper figures.

```bash
python3 server.py 8767
# open http://127.0.0.1:8767
```

Edit text on the page and click Save. Chat messages and saves are added to `inbox.jsonl`. An agent watches that file, edits the code or `manuscript.json`, re-renders figures, and replies with `reply.sh` (`say.sh` also works). See `docs/FIGURE_VIEWER.md` in the repository root.
