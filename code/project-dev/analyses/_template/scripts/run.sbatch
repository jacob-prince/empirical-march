#!/usr/bin/env bash
#SBATCH --job-name=project-analysis
#SBATCH --partition=gpu_test
#SBATCH --account=konkle_lab
#SBATCH --nodes=1
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=24G
#SBATCH --time=00:20:00
#SBATCH --output=/n/netscratch/konkle_lab/Lab/%u/project-name/logs/slurm/%x_%j.out

set -euo pipefail
source /n/holylabs/LABS/konkle_lab/Lab/"$USER"/project-name/env.sh
cd "$PROJECT_HOME/code/project-dev"
"$PROJECT_HOME/code/project-dev/.venv/bin/python" analyses/take1/NN_question_slug/scripts/run.py
