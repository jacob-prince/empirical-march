# Cannon / Harvard FASRC setup

This documents the non-secret parts of Jacob's current cluster workflow. Paths and account availability can change; verify them before launching a new project.

## Authentication and TOTP

The workstation has a `cannon` SSH host alias for `login.rc.fas.harvard.edu`. FASRC requires its own TOTP flow. A local helper cloned under `~/totp` provides:

```bash
start-ssh             # ~/totp/scripts/start-ssh; opens the shared authenticated connection
ssh cannon            # reuses it
stop-ssh              # ssh -O stop cannon
```

The installed SSH configuration uses:

```sshconfig
Host cannon
    HostName login.rc.fas.harvard.edu
    User <FASRC_USERNAME>
    ServerAliveInterval 60
    TCPKeepAlive no
    ControlMaster auto
    ControlPath ~/.ssh/controlmasters/%r@%h:%p
    ControlPersist yes
```

GPU host patterns can add `ProxyJump cannon`, so only the login-node connection performs the TOTP authentication. Because `ssh`, `rsync`, and `scp` share the control socket, agents should call `start-ssh` once rather than trigger concurrent authentication prompts.

If the connection becomes stale, close and recreate it. Do not automate around the helper by extracting its stored password or TOTP material. The repository may document aliases and commands, but must never contain credentials, TOTP seeds, one-time codes, private keys, or the helper's credential files.

## Storage roles

Use explicit project variables from `cluster/env.example.sh` rather than scattering paths through scripts.

- `/n/holylabs/LABS/konkle_lab/Lab/<user>/<project>`: durable project checkout and environments.
- `/n/netscratch/konkle_lab/Lab/<user>/<project>`: SLURM logs, caches, temporary outputs, and resumable training state; subject to cleanup policies.
- `/n/lab_storage/konkle_lab/Lab/<user>/<project>`: durable lab results and shared data when capacity permits.
- Shared datasets may live under another lab-managed path; use the official loader/default cache rather than building a private copy unless required.

Check capacity before a large run. A job that exits successfully after writing a truncated or zero-byte result to a full filesystem is not a valid result.

## Environments

Keep a reproducible lock file in Git and the environment on the cluster project filesystem. Source a non-secret cluster environment file from jobs. On shared filesystems, invoking the environment's interpreter directly can be more reliable than a package manager command that takes a lock:

```bash
/n/holylabs/LABS/konkle_lab/Lab/<user>/<project>/code/project-dev/.venv/bin/python -m project_name...
```

## SLURM policy

Jacob can use both `kempner_konkle_lab` and `konkle_lab` accounts. The included `submit_fast.sh` performs `sbatch --test-only` across configured candidate partitions and submits to the earliest estimated start. Its defaults mirror the VisCogNet policy: prefer Kempner H100, consider standard/requeue GPUs, and use test partitions for short work.

Use requeue partitions only when the program writes periodic checkpoints and resumes the same run ID correctly. Otherwise set `NOREQUEUE=1`. Record partition, account, resources, dependency, array-to-condition mapping, and job ID in the analysis `STATE.md`.

## Safe lifecycle

1. Authenticate and verify `ssh cannon`.
2. Synchronize code; do not synchronize local secrets or raw untracked caches.
3. Run duplicate audit and smoke test.
4. Submit from the project root with explicit output/log paths.
5. Record the job immediately.
6. Monitor `squeue`/`sacct` plus a durable summary file.
7. Retrieve and verify result counts/checksums.
8. Rebuild figures/reports locally.
9. Clean only explicitly resolved scratch paths.

## Ports and interactive tools

For a Streamlit or other cluster-hosted viewer, bind it to a compute node and forward a local port through Cannon. The preprint HTML viewer in this template is intentionally local and needs no cluster tunnel.
