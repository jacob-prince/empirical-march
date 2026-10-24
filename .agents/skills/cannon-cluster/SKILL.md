---
name: cannon-cluster
description: Use for anything on the FASRC Cannon cluster (including Kempner partitions): connecting over SSH, copying files, submitting SLURM jobs, monitoring, getting results back, or recovering a dropped connection.
---

# Cannon cluster

## Connect

The user's machine should have [caxon/totp](https://github.com/caxon/totp) set up (see `docs/CLUSTER.md`). It keeps one SSH connection open so you don't need a password or two-factor code:

```bash
start-ssh
ssh cannon hostname
```

`cannon` points to `login.rc.fas.harvard.edu`. Once `start-ssh` has run, `ssh`, `scp`, and `rsync` all reuse the open connection. `stop-ssh` closes it. Compute-node aliases can use `ProxyJump cannon`. If a command hangs or asks for a password, run `start-ssh` again. If `start-ssh` isn't found, ask the user to set up totp.

Never read, copy, print, or commit the password, TOTP secret or code, private keys, or the keychain entries totp uses.

## Before submitting

1. Read `docs/CLUSTER.md` and `cluster/AGENTS.md`.
2. Confirm the repository, environment, data, output, and log paths.
3. Check the registry, `squeue`, `sacct`, and the output folder for duplicate runs.
4. Run a quick local or short cluster smoke test.
5. Make sure the pass/fail rule is written in the analysis plan.
6. Decide whether the job can resume. Don't put a long job that can't resume on a requeue partition.

## Submitting and monitoring

- Use whichever GPU starts soonest across `kempner_konkle_lab` and `konkle_lab`. `cluster/tools/submit_fast.sh` does this.
- Keep heavy work off the login node.
- After submitting, write the job ID, array mapping, config, seed, output path, and dependencies in `notes/STATE.md`.
- Monitor by job ID and by a summary or output file the job writes, not by scrolling through logs.
- Treat a full disk, cut-off JSON, missing summary, or a preemption without resume as a failed run until checked.

## Getting results back

- Copy back small results, manifests, and figure inputs. Leave large arrays and checkpoints on cluster storage, at a recorded path.
- Check file counts and sizes, and checksums if possible.
- Recompute the summary locally when you can.
- Only mark the job done once the outputs open and the expected records are there.
- Before ending the session, write down what needs cleaning up and how to recover.
