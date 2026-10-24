# Preprint figures, take1

This is a generic version of the VisCogNet live-editable manuscript page.

```bash
python3 server.py 8767
# open http://127.0.0.1:8767
```

Edit text in place and save. Chat messages and save records enter `inbox.jsonl`. An active agent watches that file, edits sources or `manuscript.json`, rebuilds figures, and responds with `reply.sh` (`say.sh` also works). See the repository `docs/FIGURE_VIEWER.md`.
