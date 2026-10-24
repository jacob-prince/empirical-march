#!/usr/bin/env bash
# Usage: ./working.sh "short description of current work"
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
python3 - "$1" "$here" <<'PY'
import datetime as dt
import json
import os
from pathlib import Path
import sys

note, directory = sys.argv[1:]
status = Path(directory) / "status.json"
temporary = status.with_suffix(".json.tmp")
temporary.write_text(json.dumps({"state": "working", "note": note, "t": dt.datetime.now().isoformat(timespec="seconds")}) + "\n")
os.replace(temporary, status)
PY
