#!/usr/bin/env bash
# Run every notebook in reading order. Each one checks its own claim with an
# assert, so the first failure stops the run. Run from anywhere; paths resolve
# from the repo root.
set -euo pipefail
cd "$(dirname "$0")/.."

PY="${PYTHON:-python}"

for nb in \
    part2-metaphor/a_the_loss_is_real.py \
    part2-metaphor/b_cost_sensitive_learning.py \
    part2-metaphor/c_the_two_model_ledger.py \
    part2-metaphor/d_calibration.py
do
    echo "== $nb"
    "$PY" "$nb"
done

echo "== part3-case-study/reproduce_the_impossibility.py"
if [ -f data/compas-scores-two-years.csv ]; then
    "$PY" part3-case-study/reproduce_the_impossibility.py
else
    echo "SKIP: data/compas-scores-two-years.csv not found. See data/README.md."
fi

echo "ALL PASS"
