# Cluster rules

Read the root `AGENTS.md` and `.agents/skills/cannon-cluster/SKILL.md` before any cluster work.

- Never store credentials or TOTP secrets here.
- Every job file sets resources, wall time, log paths, and `set -euo pipefail`.
- Before every launch, check for duplicate runs and record where the output will go.
- Use job arrays for a fixed list of conditions, and commit the list.
- Only use requeue partitions for jobs whose checkpoint and resume have been tested.
- Don't run heavy CPU or GPU work on the login node.
- Don't trust outputs until you've checked the files and the expected record counts.
- Record job IDs and decisions in the analysis's `notes/STATE.md`, not only in a cluster log.
