#!/usr/bin/env bash
set -euo pipefail
out=$(bash bash/level1/01_echo.sh)
[[ "$out" == "Hello, STEAM!" ]]
echo "Bash tests passed ✅"
