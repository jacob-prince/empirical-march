#!/usr/bin/env bash
# Non-secret cluster environment template. Copy outside Git or to env.sh (ignored) and edit.

export PROJECT_NAME="project-name"
export PROJECT_USER="${USER}"
export PROJECT_HOME="/n/holylabs/LABS/konkle_lab/Lab/${PROJECT_USER}/${PROJECT_NAME}"
export PROJECT_SCRATCH="/n/netscratch/konkle_lab/Lab/${PROJECT_USER}/${PROJECT_NAME}"
export PROJECT_STORAGE="/n/lab_storage/konkle_lab/Lab/${PROJECT_USER}/${PROJECT_NAME}"
export UV_CACHE_DIR="${PROJECT_SCRATCH}/cache/uv"
export TORCH_HOME="${PROJECT_SCRATCH}/cache/torch"
export PYTHONUNBUFFERED=1

# Put account/partition policy in submit scripts, not credentials here.
