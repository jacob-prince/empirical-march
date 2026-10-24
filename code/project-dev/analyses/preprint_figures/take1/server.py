#!/usr/bin/env python3
"""Local, file-backed server for the live manuscript page (standard library only)."""

from __future__ import annotations

import datetime as dt
import hashlib
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import sys
from urllib.parse import parse_qs, urlparse


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.resolve()
DOC = HERE / "manuscript.json"
INBOX = HERE / "inbox.jsonl"
OUTBOX = HERE / "outbox.jsonl"
STATUS = HERE / "status.json"


def now() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def atomic_json(path: Path, payload: object) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    os.replace(temporary, path)


def set_status(state: str, note: str = "") -> None:
    atomic_json(STATUS, {"state": state, "note": note, "t": now()})


def read_document() -> tuple[dict, str]:
    raw = DOC.read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()[:12]


def append_jsonl(path: Path, record: dict) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps({"t": now(), **record}, ensure_ascii=False) + "\n")


def flatten(document: dict) -> dict[str, object]:
    values: dict[str, object] = {"title": document.get("title", ""), "plan": document.get("plan", "")}
    for group in ("figures", "retired"):
        for figure in document.get(group, []):
            identifier = figure.get("id", "?")
            for key, value in figure.items():
                values[f"{group}.{identifier}.{key}"] = value
    return values


class Handler(SimpleHTTPRequestHandler):
    def log_message(self, *_: object) -> None:
        return

    def send_json(self, payload: object, code: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_local_file(self, path: Path, content_type: str | None = None) -> None:
        if not path.is_file():
            self.send_error(404)
            return
        body = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type or self.guess_type(str(path)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        request = urlparse(self.path)
        if request.path in ("/", "/index.html"):
            self.send_local_file(HERE / "index.html", "text/html; charset=utf-8")
            return
        if request.path == "/api/doc":
            document, version = read_document()
            self.send_json({"version": version, "doc": document})
            return
        if request.path == "/api/status":
            if not STATUS.exists():
                set_status("idle")
            self.send_json(json.loads(STATUS.read_text()))
            return
        if request.path == "/api/outbox":
            offset = int(parse_qs(request.query).get("n", ["0"])[0])
            records = []
            if OUTBOX.exists():
                records = [json.loads(line) for line in OUTBOX.read_text().splitlines() if line.strip()]
            self.send_json({"n": len(records), "messages": records[offset:]})
            return
        if request.path == "/file":
            relative = parse_qs(request.query).get("p", [""])[0]
            path = (HERE / relative).resolve()
            if path != ROOT and ROOT not in path.parents:
                self.send_error(403)
                return
            self.send_local_file(path)
            return
        self.send_error(404)

    def do_POST(self) -> None:  # noqa: N802
        length = int(self.headers.get("Content-Length", 0))
        payload = json.loads(self.rfile.read(length) or b"{}")
        if self.path == "/api/save":
            previous, _ = read_document()
            before, after = flatten(previous), flatten(payload)
            changed = sorted(key for key in set(before) | set(after) if before.get(key) != after.get(key))
            atomic_json(DOC, payload)
            _, version = read_document()
            append_jsonl(INBOX, {"kind": "save", "changed": changed, "new": {key: after.get(key) for key in changed}})
            self.send_json({"ok": True, "version": version, "changed": changed})
            return
        if self.path == "/api/chat":
            text = str(payload.get("text", "")).strip()
            if not text:
                self.send_json({"ok": False, "error": "empty message"}, 400)
                return
            append_jsonl(INBOX, {"kind": "chat", "text": text})
            set_status("working", "new request received")
            self.send_json({"ok": True})
            return
        self.send_error(404)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8767
    print(f"manuscript viewer: http://127.0.0.1:{port}", flush=True)
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
