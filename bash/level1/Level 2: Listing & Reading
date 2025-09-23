#!/usr/bin/env bash
# 🐚 Bash Track – Level 2: Listing & Reading
#
# 🎉 Welcome back, STEAM Coder!
#
# 📘 Scenario
# Imagine you are keeping a STEAM Idea Journal.
# Yesterday, you made your first folder and file.
# Today, you want to:
#   1) Check what files are inside your "projects" folder
#   2) Peek inside your ideas.txt journal to see your first idea
#   3) Add a NEW idea without erasing the old one
#
# 👉 Run this file in Codespaces:
#     bash bash/level2.sh
#
# After you run it:
# - Look carefully at the output in the Terminal
# - It will SHOW you the folder contents
# - It will PRINT your ideas
# - Then it will ADD a second idea to the file
#
# Don’t forget to Commit & Push when finished ✅

# ℹ️ This line tells Bash:
# "Stop running the script if there’s an error."
# That way your program doesn’t keep going if something breaks.
set -e

# 1) List files
echo "📁 Looking inside your STEAM projects folder..."
ls -la projects

# 2) Show current contents
echo
echo "📖 Opening your STEAM idea journal (ideas.txt)..."
cat projects/ideas.txt || true

# 3) Append (>> adds to the end; it does NOT erase)
echo
echo "✍️ Adding a NEW idea to your journal..."
echo "My second STEAM idea" >> projects/ideas.txt

# Show final result
echo
echo "📝 Now your STEAM journal says:"
cat projects/ideas.txt

echo
echo "✅ Great job! You listed your folder, read your journal, and added a new idea."
