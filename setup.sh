#!/usr/bin/env bash
set -e
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r python/level1/requirements.txt
echo "✅ Setup complete. Run: source .venv/bin/activate"
