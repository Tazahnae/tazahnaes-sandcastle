#!/usr/bin/env bash
# 🐚 Bash – Level 4: Loops & Repetition
# 🎉 Automate like a real engineer!
#
# 📘 Scenario
# You’re writing a daily STEAM log for 5 days. Use a loop to make the files fast.
#
# 📝 Your task is to:
#   1) Create files in projects/: day1.txt … day5.txt
#   2) Put this inside each file:  STEAM Log Day X  (replace X with 1–5)
#
# 👉 Run:
#     bash bash/level4_loops_and_repetition.sh
#    Then Commit & Push, and check Actions for ✅/❌
#
# ℹ️ Why this line?
# set -e  → “Stop the script if something goes wrong.” (especially helpful in loops)

set -e

mkdir -p projects

for i in 1 2 3 4 5; do
  echo "STEAM Log Day $i" > "projects/day${i}.txt"
  echo "🗒️  Wrote projects/day${i}.txt"
done

echo "✅ Created day1.txt … day5.txt with your log text."
