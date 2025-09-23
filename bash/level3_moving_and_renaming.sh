#!/usr/bin/env bash
# 🐚 Bash – Level 3: Moving & Renaming
# 🎉 Time to organize like a pro!
#
# 📘 Scenario
# You want a better file name and a safe place to keep it.
#
# 📝 Your task is to:
#   1) Rename ideas.txt → brainstorm.txt
#   2) Create a folder: archive
#   3) Move brainstorm.txt into archive/
#
# 👉 Run:
#     bash bash/level3_moving_and_renaming.sh
#    Then Commit & Push, and check Actions for ✅/❌
#
# ℹ️ Why this line?
# set -e  → “Stop the script if something goes wrong.”

set -e

mkdir -p projects

# If ideas.txt is missing, make one so rename makes sense
[ -f projects/ideas.txt ] || echo "My first STEAM idea" > projects/ideas.txt

# 1) Rename
if [ -f projects/ideas.txt ]; then
  mv projects/ideas.txt projects/brainstorm.txt
  echo "✏️  Renamed ideas.txt → brainstorm.txt"
else
  echo "⚠️  ideas.txt not found (maybe already renamed?)."
fi

# 2) Make archive
mkdir -p projects/archive

# 3) Move into archive
if [ -f projects/brainstorm.txt ]; then
  mv projects/brainstorm.txt projects/archive/
  echo "📦 Moved brainstorm.txt → projects/archive/"
else
  echo "⚠️  brainstorm.txt not found (maybe already moved?)."
fi

echo "✅ Organization complete!"
