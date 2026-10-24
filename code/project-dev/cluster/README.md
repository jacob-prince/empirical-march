# Cluster files

- `env.example.sh`: copy to `env.sh` somewhere private on the cluster and edit the paths. Don't commit secrets.
- `jobs/smoke_gpu.sbatch`: quick CUDA and package test.
- `tools/submit_fast.sh`: tries each partition/account pair and submits to whichever starts soonest.

Jobs for a specific analysis usually live in that analysis (`analyses/takeN/NN_name/scripts/*.sbatch`). Shared tools live here.
