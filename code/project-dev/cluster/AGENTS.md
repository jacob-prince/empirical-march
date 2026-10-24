# Cluster subtree rules

Read the repository contract and `.agents/skills/cannon-cluster/SKILL.md` before cluster work.

- Never store credentials or TOTP material here.
- Every job file must set explicit resources, wall time, log paths, and strict shell mode.
- Every launch requires a duplicate-run audit and a recorded destination.
- Prefer job arrays for a declared condition roster. Commit the roster.
- Requeue/preemptible partitions require tested checkpoint/resume behavior.
- Do not run sustained CPU/GPU work on the login node.
- Do not trust outputs until file integrity and expected record counts are checked.
- Record job IDs and decisions in the owning analysis `notes/STATE.md`, not only in a cluster log.
