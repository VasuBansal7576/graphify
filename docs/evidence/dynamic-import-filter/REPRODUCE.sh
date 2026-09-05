#!/bin/sh
set -eu

# Set BASE_CHECKOUT to a checkout at 33362d9 and CANDIDATE_CHECKOUT to 2236f54.
PYTHON=${PYTHON:-python}
BASE_CHECKOUT=${BASE_CHECKOUT:?set BASE_CHECKOUT to the 33362d9 checkout}
CANDIDATE_CHECKOUT=${CANDIDATE_CHECKOUT:?set CANDIDATE_CHECKOUT to the 2236f54 checkout}
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
FIXTURE=$SCRIPT_DIR/fixture
WORK=$(mktemp -d "${TMPDIR:-/tmp}/graphify-dynamic-import-filter.XXXXXX")

run_case() {
    label=$1
    checkout=$2
    out=$WORK/$label
    echo "=== $label ($checkout) ==="
    (cd "$checkout" && "$PYTHON" -m graphify extract "$FIXTURE" --code-only --no-cluster --max-workers 1 --out "$out")
    "$PYTHON" -c 'import json, sys; from pathlib import Path; graph=json.loads((Path(sys.argv[1]) / "graphify-out" / "graph.json").read_text()); print("dynamic edges:", [(e["source"], e["target"], e["relation"]) for e in graph["edges"] if e.get("relation") == "dynamic_import"])' "$out"
}

run_case before "$BASE_CHECKOUT"
run_case after "$CANDIDATE_CHECKOUT"
