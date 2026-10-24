#!/usr/bin/env python3
"""Build one HTML index per take from numbered analysis folders."""

from html import escape
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent


def field(text: str, label: str, fallback: str) -> str:
    match = re.search(rf"^{re.escape(label)}:\s*(.+)$", text, re.M | re.I)
    return match.group(1).strip() if match else fallback


def main() -> None:
    for take in sorted(HERE.glob("take[0-9]*")):
        rows = []
        for analysis in sorted(take.iterdir()):
            if not analysis.is_dir() or not re.match(r"^[0-9]{2}_", analysis.name):
                continue
            state_path = analysis / "notes" / "STATE.md"
            state = state_path.read_text() if state_path.exists() else ""
            status = field(state, "Status", "not recorded")
            question_match = re.search(r"## Question and criterion\s+(.+?)(?=\n## |\Z)", state, re.S)
            summary = " ".join(question_match.group(1).split()) if question_match else "No question recorded."
            rows.append(
                f'<tr><td>{escape(analysis.name[:2])}</td><td><a href="{escape(analysis.name)}/report.html">{escape(analysis.name)}</a></td>'
                f'<td>{escape(status)}</td><td>{escape(summary)}</td></tr>'
            )
        body = "\n".join(rows) or '<tr><td colspan="4">No numbered analyses yet.</td></tr>'
        html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(take.name)} analysis reports</title><style>
body{{font:15px/1.5 Arial,Helvetica,sans-serif;max-width:1000px;margin:2rem auto;padding:0 1rem;color:#181818}}
table{{border-collapse:collapse;width:100%}}th,td{{text-align:left;padding:.55rem;border-bottom:1px solid #ddd;vertical-align:top}}th{{border-bottom:2px solid #333}}a{{color:#0645ad;text-decoration:none}}a:hover{{text-decoration:underline}}
</style></head><body><h1>{escape(take.name)} analysis reports</h1><p>Generated from each numbered folder's report and STATE.md.</p>
<table><tr><th>#</th><th>Folder</th><th>Status</th><th>Question/current criterion</th></tr>{body}</table></body></html>"""
        output = take / "report_index.html"
        output.write_text(html)
        print(output)


if __name__ == "__main__":
    main()
