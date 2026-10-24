#!/usr/bin/env bash
#SBATCH --job-name=project-smoke
#SBATCH --partition=gpu_test
#SBATCH --account=konkle_lab
#SBATCH --nodes=1
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=00:10:00
#SBATCH --output=/n/netscratch/konkle_lab/Lab/%u/project-name/logs/slurm/%x_%j.out
#SBATCH --error=/n/netscratch/konkle_lab/Lab/%u/project-name/logs/slurm/%x_%j.err

set -euo pipefail
source /n/holylabs/LABS/konkle_lab/Lab/"$USER"/project-name/env.sh
cd "$PROJECT_HOME/code/project-dev"
"$PROJECT_HOME/code/project-dev/.venv/bin/python" - <<'PY'
import platform
import torch

print({"host": platform.node(), "torch": torch.__version__, "cuda": torch.cuda.is_available()})
if not torch.cuda.is_available():
    raise SystemExit("CUDA unavailable")
print({"device": torch.cuda.get_device_name(0)})
PY
