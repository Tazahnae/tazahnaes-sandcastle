# 🐍 Exercise 2: Variables & Add
# Welcome back, STEAM Coder! ✨
#
# ────────────────────────────────────────────────
# 📘 BEFORE YOU BEGIN:
# Remember: all coding is done in **GitHub Codespaces**.
# Open this file in Codespaces (python/level1/variables_02.py)
# and complete the TODO inside the function.
#
# DEFINITIONS
# • Variable → a box that stores a value (like a number or word).
# • Operator → a symbol like + or - that tells Python what to do.
# • Parameter → the input your function needs (here: a, b).
# • Return value → the answer your function sends back.
#
# ────────────────────────────────────────────────
#
# # 📝 TASK
# Write a function `combine(a, b)` that returns the sum of a and b.
#
# 📚 Example Scenario:
# You are running a lemonade stand.
# You sell 2 cups in the morning and 3 cups in the afternoon.
# Your program should add them up:
#   combine(2, 3) → 5# 
#
#
# 🧪 HOW TO TEST IN CODESPACES
# 1) Open the Terminal at the bottom.
# 2) Type: python
# 3) Import your function:
#       from python.level1.variables_02 import combine
# 4) Try it:
#       combine(2, 3)     → 5
#       combine(10, -4)   → 6
# 5) Exit Python: exit() or Ctrl+D
#
# ────────────────────────────────────────────────
# 💾 SAVE + CHECK YOUR WORK
# 1) When you’re done, go to Source Control (left panel).
# 2) Write a short message (example: finish combine).
# 3) Click **Commit & Push**.
# 4) Go back to GitHub (your repo page).
# 5) Click the **Actions** tab → open the latest run called *Python tests*.
# 6) Look for:
#       ✅ Green check → You passed!
#       ❌ Red X → Something is wrong, fix and Commit & Push again.
# ────────────────────────────────────────────────

def combine(a: int, b: int) -> int:
    # TODO: return the sum of a and b
    return a + b


# 📖 EXPLANATION (read after you solve!)
#
# - `a` and `b` are **parameters** (inputs to your function).
# - When you call `combine(2, 3)`, Python assigns:
#       a = 2
#       b = 3
# - `a + b` → 5
# - The `return` keyword sends that value back.
#
# Example:
#   combine(10, -4) → 6
#
# ✅ That’s it! You’ve just used variables and addition to build a real function.
#
# 🚀 BONUS CHALLENGE (not graded):
# - Write a function `subtract(a, b)` that returns the difference.
# - Write a function `multiply(a, b)` that returns the product.
