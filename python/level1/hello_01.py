# 🐍 Exercise 1: Say Hello
# Welcome, STEAM Coder! 🎉
#
# ──────────────────────────────────────────────────────────────────────────────
# INSTRUCTIONS
# 1) Read the definitions below.
# 2) Complete the task: write a function `say_hello(name)` that returns
#       "Hello, <name>"
#    (No exclamation mark — the tests expect exactly that.)
# 3) Try the examples mentally, then run the tests (see “Run tests”).
#
# DEFINITIONS
# • Function: a reusable block of code that does one job.
# • Parameter: the input a function needs (here: `name`).
# • Return value: the single value the function sends back.
# • String concatenation: joining strings with `+`, e.g. "Hello, " + name
#
# TASK
# Write a function `say_hello(name)` that returns exactly:
#   "Hello, <name>"
#
# EXAMPLES
#   say_hello("Taz")    → "Hello, Taz"
#   say_hello("STEAM")  → "Hello, STEAM"
#
# RUN TESTS
#   source .venv/bin/activate
#   pytest -q
#
# HINTS
# • Use: return "Hello, " + name
# • Don’t print — the grader checks the return value, not the screen output.
# ──────────────────────────────────────────────────────────────────────────────

def say_hello(name: str) -> str:
    """Return 'Hello, <name>' exactly (no exclamation mark)."""
    return "Hello, " + name


# 📖 EXPLANATION (read after you solve!)
# - `def say_hello(name: str)` defines a function named say_hello that takes a
#   single parameter `name` (a string).
# - `"Hello, " + name` builds a new string using concatenation.
# - `return` hands that string back to the caller.
#
# Walk-through:
#   say_hello("STEAM")
#   → "Hello, " + "STEAM"
#   → "Hello, STEAM"
#
# 🚀 BONUS (optional, not graded in Level 1 tests)
# 1) Handle empty input:
#      if name == "": return "Hello!"
# 2) Format nicely:
#      return "Hello, " + name.title()
# 3) Add a second parameter (default value):
#      def say_hello(name: str, greeting: str = "Hello") -> str:
#          return f"{greeting}, {name}"
