# 🐍 Exercise 2: Variables & Add
# Welcome back, STEAM Coder! ✨
#
# In this challenge, you’ll practice using **variables** and the `+` operator.
# A variable is like a box that stores a value (such as a number).
# The `+` operator lets you add numbers together.
#
# 📝 Task:
# Write a function `combine(a, b)` that returns the sum of a and b.
#
# Example:
#   combine(2, 3) → 5
#   combine(10, -4) → 6
#
# ▶️ Run tests with:
#   source .venv/bin/activate
#   pytest -q
#
# 💡 Hint: Use `return a + b` inside your function.

def combine(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


# 📖 Explanation (read after you solve!)
#
# - `a` and `b` are **parameters** (inputs to your function).
# - When you call `combine(2, 3)`, Python assigns:
#     a = 2
#     b = 3
# - `a + b` → 5
# - The `return` keyword sends that value back.
#
# Example:
#   combine(10, -4) → 6
#
# ✅ That’s all! You’ve used variables and addition to build a real function.
#
# 🚀 Bonus Challenge:
# - Write a function `subtract(a, b)` that returns the difference.
# - Write a function `multiply(a, b)` that returns the product.
