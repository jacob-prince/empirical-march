---
name: cannon-cluster
description: Use for Harvard FASRC/Cannon authentication, file transfer, SLURM submission, monitoring, result retrieval, or cluster recovery.
---

# Cannon cluster workflow

## Authenticate safely

Use the local TOTP helper to create one persistent SSH control connection:

```bash
start-ssh
ssh cannon 'hostname'
```

The helper is currently installed at `~/totp/scripts/start-ssh`; the `cannon` alias targets `login.rc.fas.harvard.edu`. SSH `ControlMaster`/`ControlPersist` lets later `ssh`, `scp`, and `rsync` operations reuse the authenticated socket. `stop-ssh` closes it. GPU-node aliases may use `ProxyJump cannon`.

Never read, copy, display, or commit the password, TOTP seed/code, private key, or helper credential store.

## Before submission

1. Read `docs/CLUSTER.md` and `cluster/AGENTS.md`.
2. Confirm the exact repository, environment, data, output, and log paths.
3. Audit the registry, `squeue`, `sacct`, and output directory for duplicate runs.
4. Run a local or short cluster smoke test.
5. Record the scientific criterion in the analysis plan.
6. Decide whether the job is restartable. Do not use a preemptible/requeue partition for a long job that cannot resume.

## Submission and monitoring

- Prefer the earliest suitable GPU across `kempner_konkle_lab` and `konkle_lab`; use `cluster/tools/submit_fast.sh` when appropriate.
- Keep heavy work off the login node.
- After submission, write the job ID, array mapping, config, seed, destination, and dependencies into `notes/STATE.md`.
- Monitor by job ID and durable summary/output file, not by repeatedly scraping noisy logs.
- Treat a full filesystem, truncated JSON, missing summary, or preemption without resume as a failed/untrusted run until verified.

## Retrieval and completion

- Copy back small results, manifests, and figure inputs; keep large arrays/checkpoints in documented cluster storage.
- Check file counts, sizes, and preferably checksums.
- Recompute the small summary locally when possible.
- Mark the job complete only after outputs are readable and the expected records exist.
- Record cleanup and recovery instructions before ending the session.
