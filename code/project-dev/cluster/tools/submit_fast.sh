#!/usr/bin/env bash
# Submit to the candidate partition/account pair with the earliest estimated start.
# Run on Cannon: bash cluster/tools/submit_fast.sh path/to/job.sbatch [extra sbatch args]

set -euo pipefail
job_file="${1:?usage: submit_fast.sh JOB.sbatch [sbatch args...]}"
shift

kempner_account="${KEMPNER_ACCOUNT:-kempner_konkle_lab}"
lab_account="${LAB_ACCOUNT:-konkle_lab}"
candidates=(
  "kempner_h100:${kempner_account}:cc9.0"
  "kempner_requeue:${kempner_account}:cc9.0"
  "gpu_test:${kempner_account}:"
  "gpu_test:${lab_account}:"
  "gpu:${lab_account}:"
  "gpu_requeue:${lab_account}:"
)

if [[ -n "${NOREQUEUE:-}" ]]; then
  candidates=(
    "kempner_h100:${kempner_account}:cc9.0"
    "gpu:${lab_account}:"
    "gpu_h200:${lab_account}:"
    "gpu_test:${kempner_account}:"
    "gpu_test:${lab_account}:"
  )
fi

best=""
best_time=""
for candidate in "${candidates[@]}"; do
  IFS=: read -r partition account constraint <<< "$candidate"
  output="$(sbatch --test-only --partition="$partition" --account="$account" --constraint="$constraint" "$@" "$job_file" 2>&1 | tail -1 || true)"
  start="$(sed -n 's/.*to start at \([0-9T:-]*\).*/\1/p' <<< "$output")"
  if [[ -z "$start" ]]; then
    printf '  %s/%s: %s\n' "$partition" "$account" "$output" >&2
    continue
  fi
  printf '  %s/%s: start %s\n' "$partition" "$account" "$start" >&2
  if [[ -z "$best_time" || "$start" < "$best_time" ]]; then
    best="$candidate"
    best_time="$start"
  fi
done

[[ -n "$best" ]] || { echo "no candidate accepted the job" >&2; exit 1; }
IFS=: read -r partition account constraint <<< "$best"
printf 'submitting to %s/%s (estimated %s)\n' "$partition" "$account" "$best_time" >&2

if [[ -n "${DRYRUN:-}" ]]; then
  printf 'sbatch --partition=%q --account=%q --constraint=%q ' "$partition" "$account" "$constraint"
  printf '%q ' "$@" "$job_file"
  printf '\n'
  exit 0
fi

sbatch --partition="$partition" --account="$account" --constraint="$constraint" --requeue "$@" "$job_file"
