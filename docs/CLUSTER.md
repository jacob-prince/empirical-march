# Cluster setup (FASRC Cannon)

This page covers how we connect to and use the FASRC Cannon cluster, including the Kempner partitions. Paths and account access can change, so check them before starting a new project.

## Persistent SSH connection (totp)

FASRC asks for your password and a two-factor (TOTP) code every time you log in over SSH. That is fine for a person, but it means a coding agent can't run commands on the cluster for you. [caxon/totp](https://github.com/caxon/totp) solves this. It logs in once with your stored password and TOTP secret, then keeps that SSH connection open in the background. Every later `ssh`, `scp`, or `rsync` to the cluster reuses the open connection, so no password or code is needed. Once it is set up, an agent can submit jobs, check on them, debug on the cluster, and sync files back and forth.

> [!WARNING]
> totp has only been tested on macOS. It may work on Linux with some changes.

### Setup (once, on your own machine)

1. Clone the repo into your home directory:

    ```bash
    cd ~
    git clone https://github.com/caxon/totp.git
    cd totp
    ```

2. Install `conda` if you don't have it (for example [miniforge](https://github.com/conda-forge/miniforge)). Then create and activate the environment:

    ```bash
    conda env create -f environment.yml
    conda activate totp
    ```

3. Get your FASRC username, FASRC password, and FASRC TOTP secret. See the totp repo's guide: [OBTAIN_FASRC_TOKEN.md](https://github.com/caxon/totp/blob/main/docs/OBTAIN_FASRC_TOKEN.md). This is the FASRC two-factor setup, not the Harvard-wide one.

4. Run the installer and follow the prompts. Say yes to storing the passwords (they go in the macOS keychain), adding the shell aliases, and adding the SSH config:

    ```bash
    ./scripts/install
    ```

    The installer adds aliases to `~/.zshrc`. If you use bash, change `RC_FILE` in `src/constants.py` before installing.

5. Open a new terminal and test it:

    ```bash
    start-ssh
    ssh cannon hostname
    ```

    macOS may ask whether Python can use the keychain. Clicking "Always Allow" stops the prompt from coming back. Note that this lets any Python program read those specific secrets.

### Daily use

```bash
start-ssh        # open the shared connection (prints nothing if it worked; -v for logs)
ssh cannon       # reuses it, no password or code
stop-ssh         # close it
```

- The connection stays open even if you close the terminal. It can drop if your laptop sleeps or loses network for a while; just run `start-ssh` again.
- It only works for the main login node (`login.rc.fas.harvard.edu`). Logging into a specific node like `holylogin02` directly still asks for a password and code. Compute-node aliases can use `ProxyJump cannon` to go through the shared connection.
- If SSH stops working after the config changes, restart the SSH service: `sudo launchctl stop com.openssh.sshd`.
- To change your password or TOTP secret, run `python -m src.cleanup_all -t password` from the totp folder, then rerun `./scripts/install` and answer yes only to the password question.

The installer writes this block to `~/.ssh/config`:

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

### Notes for agents

- Run `start-ssh` once, then check with `ssh cannon hostname`. Don't run several `start-ssh` calls at the same time.
- If the connection has gone stale, run `start-ssh` again.
- Never read, copy, or print the stored password or TOTP secret, and never commit the keychain entries or anything from the totp folder.

## Storage

Set project paths once in `cluster/env.example.sh` instead of writing them into every script.

- `/n/holylabs/LABS/konkle_lab/Lab/<user>/<project>`: code checkout and Python environments.
- `/n/netscratch/konkle_lab/Lab/<user>/<project>`: SLURM logs, caches, temporary outputs, and checkpoints for resuming. Files here can be deleted by FASRC cleanup.
- `/n/lab_storage/konkle_lab/Lab/<user>/<project>`: long-term lab results and shared data, when there is space.
- Shared datasets may live elsewhere on lab storage. Use the standard loader or cache rather than making a private copy.

Check free space before a big run. A job that finishes "successfully" after writing an empty or cut-off file to a full disk has not produced a result.

## Environments

Keep a lock file in Git and the environment itself on the cluster project folder. Jobs should source a cluster environment file (without secrets). On shared filesystems it is often more reliable to call the environment's Python directly than to go through a package manager that takes a lock:

```bash
/n/holylabs/LABS/konkle_lab/Lab/<user>/<project>/code/project-dev/.venv/bin/python -m project_name...
```

## Submitting jobs

Lab members can usually submit under both `kempner_konkle_lab` and `konkle_lab`. `submit_fast.sh` runs `sbatch --test-only` on each candidate partition and submits to whichever would start soonest. By default it prefers Kempner H100s, also considers the standard and requeue GPU partitions, and uses the test partitions for short jobs.

Only use requeue partitions if the job saves checkpoints and can resume the same run. Otherwise set `NOREQUEUE=1`. Write the partition, account, resources, dependencies, array-index-to-condition mapping, and job ID in the analysis's `STATE.md`.

## Job checklist

1. Run `start-ssh` and check `ssh cannon`.
2. Sync code. Don't sync local secrets or large untracked caches.
3. Check for duplicate runs and run a quick smoke test.
4. Submit from the project root with explicit output and log paths.
5. Record the job in `STATE.md` right away.
6. Monitor with `squeue`/`sacct` and a summary file the job writes.
7. Copy results back and check file counts or checksums.
8. Rebuild figures and reports locally.
9. Delete only scratch paths you have checked.

## Ports and interactive tools

For Streamlit or another viewer running on the cluster, start it on a compute node and forward a local port through `cannon`. The paper-figure page in this template runs locally and doesn't need the cluster.
