#!/usr/bin/env python3
"""Build a dependency-free analysis report from report.md and figures/."""

from html import escape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent


def inline(text: str) -> str:
    text = escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def markdown(text: str) -> str:
    out: list[str] = []
    in_list = False
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            if in_list:
                out.append("</ul>")
                in_list = False
            continue
        heading = re.match(r"^(#{1,4})\s+(.*)$", line)
        if heading:
            if in_list:
                out.append("</ul>")
                in_list = False
            level = len(heading.group(1))
            out.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
        elif line.startswith("- "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(line[2:])}</li>")
        else:
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<p>{inline(line)}</p>")
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def main() -> None:
    narrative = markdown((ROOT / "report.md").read_text())
    images = sorted((ROOT / "figures").glob("*.png"))
    gallery = "\n".join(
        f'<figure><img src="figures/{escape(path.name)}" alt="{escape(path.stem)}"><figcaption>{escape(path.stem)}</figcaption></figure>'
        for path in images
    ) or '<p class="muted">No PNG figures yet.</p>'
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(ROOT.name)} report</title><style>
body{{font:16px/1.55 Arial,Helvetica,sans-serif;color:#181818;max-width:980px;margin:2rem auto;padding:0 1rem}}
h1,h2,h3{{line-height:1.2}} img{{width:100%;border:1px solid #ddd}} figure{{margin:2rem 0}} figcaption,.muted{{color:#666}}
code{{background:#f3f3f3;padding:.1rem .3rem;border-radius:3px}}
</style></head><body>{narrative}<h2>Rendered figures</h2>{gallery}</body></html>"""
    out = ROOT / "report.html"
    out.write_text(html)
    print(out)


if __name__ == "__main__":
    main()
