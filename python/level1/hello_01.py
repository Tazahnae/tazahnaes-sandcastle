# 🐍 Exercise 1: Say Hello
# Welcome, STEAM Coder! 🎉
#
# In this first challenge you’ll write a tiny **function**.
# A function is a reusable block of code that takes input and returns output.
#
# 📝 Task:
# Write a function `say_hello(name)` that returns this exact format:
#   "Hello, <name>"
#
# Examples:
#   say_hello("Taz")    → "Hello, Taz"
#   say_hello("STEAM")  → "Hello, STEAM"
#
# ▶️ Run tests with:
#   source .venv/bin/activate
#   pytest -q
#
# 💡 Hint: Use string concatenation:  "Hello, " + name

def say_hello(name: str) -> str:
    """Return 'Hello, <name>'."""
    return "Hello, " + name


# 📖 Explanation (read after you solve!)
#
# - def say_hello(name: str) defines a function named `say_hello`
# - `name` is a parameter (the input you pass in)
# - `"Hello, " + name` builds a new string like "Hello, Taz"
# - `return` sends that string back to whoever called the function
#
# Example walk-through:
#   say_hello("STEAM")
#   → "Hello, " + "STEAM"
#   → "Hello, STEAM"
#
# 🚀 Bonus Challenge:
# - If `name` is the empty string "", return just "Hello!"
# - Make it title case: say_hello("tazahnae") → "Hello, Tazahnae"
