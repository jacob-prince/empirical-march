#!/usr/bin/env python3
"""Validate the template's durable project contracts using only the standard library."""

from pathlib import Path
import json
import re
import sys


PROJECT = Path(__file__).resolve().parent.parent
REPO = PROJECT.parent.parent
REQUIRED_ROOT = ["AGENTS.md", "README.md", ".agents/skills", "literature", "meeting-notes", "labbook"]
ANALYSIS_PARTS = [
    "scripts",
    "results",
    "figures",
    "notes/plan.md",
    "notes/STATE.md",
    "notes/decisions.md",
    "report.md",
    "report.html",
]


def main() -> None:
    errors: list[str] = []
    for rel in REQUIRED_ROOT:
        if not (REPO / rel).exists():
            errors.append(f"missing repository path: {rel}")

    for take in sorted((PROJECT / "analyses").glob("take[0-9]*")):
        for analysis in sorted(take.iterdir()):
            if not analysis.is_dir() or not re.match(r"^[0-9]{2}_", analysis.name):
                continue
            for rel in ANALYSIS_PARTS:
                if not (analysis / rel).exists():
                    errors.append(f"{analysis.relative_to(PROJECT)} missing {rel}")

    viewer = PROJECT / "analyses" / "preprint_figures" / "take1"
    for rel in ["server.py", "index.html", "manuscript.json", "reply.sh", "say.sh", "working.sh"]:
        if not (viewer / rel).exists():
            errors.append(f"viewer missing {rel}")
    try:
        document = json.loads((viewer / "manuscript.json").read_text())
        if not isinstance(document.get("figures"), list):
            errors.append("manuscript.json figures must be a list")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid manuscript.json: {exc}")

    secret_names = re.compile(r"(totp|password|private[_-]?key|credentials)(\.|$)", re.I)
    for path in REPO.rglob("*"):
        if path.is_file() and secret_names.search(path.name) and not path.name.endswith(".example"):
            errors.append(f"secret-like filename must not be tracked: {path.relative_to(REPO)}")

    if errors:
        print("structure validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)
    print("structure validation passed")


if __name__ == "__main__":
    main()
