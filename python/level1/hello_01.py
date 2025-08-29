# 🐍 Exercise 1: Say Hello
# Welcome, STEAM Coder! 🎉
#
# ────────────────────────────────────────────────
# INSTRUCTIONS
# 1) Read the definitions below.
# 2) Complete the task: write a function `say_hello(name)` that returns:
#        "Hello, <name>"
#    (No exclamation mark — the tests expect exactly that.)
# 3) Try the examples mentally, then run the tests.
#
# DEFINITIONS
# • Function → a reusable block of code that does one job.
# • Parameter → the input a function needs (here: `name`).
# • Return value → the single value the function sends back.
# • String concatenation → joining strings with `+`
#       Example: "Hello, " + name
#
# TASK
# Write a function `say_hello(name)` that returns exactly:
#   "Hello, <name>"
#
# EXAMPLES
#   say_hello("Taz")    → "Hello, Taz"
#   say_hello("STEAM")  → "Hello, STEAM"
#
# RUN TESTS (in Codespaces or local)
#   source .venv/bin/activate
#   pytest -q
#
# HINTS
# • Use: return "Hello, " + name
# • Don’t print — the grader checks the return value, not the screen output.
# ────────────────────────────────────────────────


# ✅ YOUR CODE (solution)
def say_hello(name: str) -> str:
    return "Hello, " + name


# 📖 EXPLANATION OF THE SOURCE CODE
#
# Line by line:
#
# 1. def say_hello(name: str) -> str:
#    • `def` starts the function definition.
#    • `say_hello` is the function name.
#    • `(name: str)` means the function takes one input (a string called `name`).
#    • `-> str` tells us the function will return a string.
#
# 2. return "Hello, " + name
#    • `"Hello, "` is a string.
#    • `+ name` adds (concatenates) the user’s name to that string.
#    • Example: if name = "Taz", then "Hello, " + "Taz" → "Hello, Taz"
#    • `return` gives this final string back to whoever called the function.
#
# Example Walk-through:
#   say_hello("STEAM")
#   → "Hello, " + "STEAM"
#   → "Hello, STEAM"
#
# That’s it! 🎉 You’ve just created your first function.
#
# 🚀 BONUS IDEAS (optional, not graded in tests)
# 1) Handle empty input:
#       if name == "": return "Hello!"
# 2) Format nicely:
#       return "Hello, " + name.title()
# 3) Add a second parameter (default value):
#       def say_hello(name: str, greeting: str = "Hello") -> str:
#           return f"{greeting}, {name}"
