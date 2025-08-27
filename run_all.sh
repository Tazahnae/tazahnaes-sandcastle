#!/usr/bin/env bash
set -e
source .venv/bin/activate
echo "=== Python ==="
pytest -q
echo "=== Web ==="
cd web/level1/tests && npm install >/dev/null && npm test -s && cd -
echo "=== Bash ==="
bash/bash_test_runner.sh
