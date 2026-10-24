# Cluster files

- `env.example.sh`: copy to a private cluster location as `env.sh` and edit paths; do not commit secrets.
- `jobs/smoke_gpu.sbatch`: minimal CUDA and package smoke test.
- `tools/submit_fast.sh`: test candidate partition/account pairs and submit to the earliest estimated start.

Scientific jobs normally live inside the analysis that owns them (`analyses/takeN/NN_name/scripts/*.sbatch`). Shared launch policy and reusable infrastructure live here.
