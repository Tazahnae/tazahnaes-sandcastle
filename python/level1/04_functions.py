# 🔢 Exercise 4: Is Even?
# You got this, STEAM Coder! 🙌
#
# ────────────────────────────────────────────────
# 📘 BEFORE YOU BEGIN
# All coding is done in **GitHub Codespaces**.
# Open this file in Codespaces: python/level1/is_even_04.py
# Complete the TODO, then follow SAVE + CHECK steps.
#
# 📖 DEFINITIONS
# • Conditional (if/else) → choose different actions based on a test.
# • Boolean → a value that is either True or False.
# • Even number → divisible by 2 (remainder 0).
# • Modulo operator (%) → gives the remainder of division.
# ────────────────────────────────────────────────
#
# 📝 TASK
# Write a function `is_even(n)` that returns True if n is even, else False.
#
# 📚 Example Scenario:
# Imagine you’re designing a game where only players with even-numbered IDs
# get a bonus. Your function checks:
#   is_even(24) → True
#   is_even(37) → False
#
# EXAMPLES
#   is_even(2)   → True
#   is_even(3)   → False
#   is_even(0)   → True
#
# 💡 HINT
# Use the modulo operator: n % 2 == 0
#
# 🧪 HOW TO TEST IN CODESPACES
# 1) Open the Terminal.
# 2) Type: python
# 3) Import function:
#       from python.level1.is_even_04 import is_even
# 4) Try it:
#       is_even(10)   → True
#       is_even(11)   → False
# 5) Exit Python:  exit()  or press Ctrl + D
# ────────────────────────────────────────────────
# 💾 SAVE + CHECK YOUR WORK
# 1) Source Control → write a message (example: finish is_even)
# 2) Click **Commit & Push** (or **Sync Changes**)
# 3) On GitHub → **Actions** tab → open *Python tests*
# 4) Look for:
#       ✅ Green check → You passed!
#       ❌ Red X → Fix in Codespaces → Commit & Push again
# ────────────────────────────────────────────────

def is_even(n: int) -> bool:
    """Return True if n is even, otherwise False."""
    # TODO: return n % 2 == 0
    return (n % 2) == 0
