#!/usr/bin/env bash
# Usage: ./reply.sh "message shown in the viewer chat"
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
python3 - "$1" "$here" <<'PY'
import datetime as dt
import json
import os
from pathlib import Path
import sys

message, directory = sys.argv[1:]
here = Path(directory)
timestamp = dt.datetime.now().isoformat(timespec="seconds")
with (here / "outbox.jsonl").open("a") as handle:
    handle.write(json.dumps({"t": timestamp, "who": "agent", "text": message}) + "\n")
status = here / "status.json"
temporary = status.with_suffix(".json.tmp")
temporary.write_text(json.dumps({"state": "idle", "note": "", "t": timestamp}) + "\n")
os.replace(temporary, status)
PY
