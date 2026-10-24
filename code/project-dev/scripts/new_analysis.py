#!/usr/bin/env python3
"""Create the next numbered analysis by copying analyses/_template."""

from argparse import ArgumentParser
from pathlib import Path
import re
import shutil


PROJECT = Path(__file__).resolve().parent.parent
ANALYSES = PROJECT / "analyses"
TEMPLATE = ANALYSES / "_template"


def slug(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")
    if not value:
        raise ValueError("name must contain a letter or number")
    return value


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--take", default="take1", help="take directory, e.g. take1")
    parser.add_argument("--name", required=True, help="short question slug")
    args = parser.parse_args()

    if not re.fullmatch(r"take[1-9][0-9]*", args.take):
        parser.error("--take must look like take1")
    take = ANALYSES / args.take
    take.mkdir(exist_ok=True)
    numbers = [int(p.name[:2]) for p in take.iterdir() if p.is_dir() and re.match(r"^[0-9]{2}_", p.name)]
    number = max(numbers, default=-1) + 1
    destination = take / f"{number:02d}_{slug(args.name)}"
    if destination.exists():
        parser.error(f"already exists: {destination}")

    shutil.copytree(TEMPLATE, destination)
    readme = destination / "README.md"
    readme.write_text(readme.read_text().replace("NN_question_slug", destination.name))
    run_sbatch = destination / "scripts" / "run.sbatch"
    run_sbatch.write_text(run_sbatch.read_text().replace("NN_question_slug", destination.name).replace("take1", args.take))
    print(destination.relative_to(PROJECT))


if __name__ == "__main__":
    main()
