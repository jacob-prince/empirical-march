#!/usr/bin/env python3
"""Print new viewer requests. This does not launch or authenticate an agent."""

from pathlib import Path
import time


INBOX = Path(__file__).resolve().parent / "inbox.jsonl"


def main() -> None:
    position = INBOX.stat().st_size if INBOX.exists() else 0
    print(f"watching {INBOX} from byte {position}", flush=True)
    while True:
        if INBOX.exists() and INBOX.stat().st_size < position:
            position = 0
        if INBOX.exists():
            with INBOX.open() as handle:
                handle.seek(position)
                for line in handle:
                    print(line.rstrip(), flush=True)
                position = handle.tell()
        time.sleep(1)


if __name__ == "__main__":
    main()
