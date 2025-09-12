# 🐍 Exercise 1: Say Hello
# Welcome, STEAM Coder! 🎉
#
# ────────────────────────────────────────────────
# 📘 BEFORE YOU BEGIN
# All coding is done in **GitHub Codespaces**.
# Open this file in Codespaces: python/level1/hello_01.py
# Complete the TODO inside the function, then follow SAVE + CHECK steps.
#
# 📖 DEFINITIONS
# • Function → a reusable block of code that does one job.
# • Parameter → the input a function needs (here: `name`).
# • Return value → the answer your function sends back.
# • String concatenation → joining strings with `+` (e.g., "Hello, " + name)
# ────────────────────────────────────────────────
#
# 📝 TASK
# Write a function `say_hello(name)` that returns exactly:
#   "Hello, <name>"
# (No exclamation mark — tests expect the exact text.)
#
# 📚 Example Scenario:
# Imagine you are building a robot greeter at the front of a museum.
# When someone types their name, the robot should greet them back:
#   say_hello("Maya") → "Hello, Maya"
#
# EXAMPLES
#   say_hello("Taz")    → "Hello, Taz"
#   say_hello("STEAM")  → "Hello, STEAM"
#
# 💡 HINT
# Use: return "Hello, " + name
# (Don’t print — tests check the return value.)
#
# 🧪 HOW TO TEST IN CODESPACES
# 1) Open the Terminal (bottom of Codespaces).
# 2) Type: python
# 3) Import your function (exactly, no leading # or spaces):
#       from python.level1.hello_01 import say_hello
# 4) Try it:
#       say_hello("Taz")    → 'Hello, Taz'
#       say_hello("STEAM")  → 'Hello, STEAM'
# 5) Exit Python:  exit()  or press Ctrl + D
# ────────────────────────────────────────────────
# 💾 SAVE + CHECK YOUR WORK
# 1) Go to **Source Control** (left panel).
# 2) Write a short message (example: finish say_hello).
# 3) Click **Commit & Push** (or **Sync Changes**).
# 4) On GitHub, open the **Actions** tab → open *Python tests*.
# 5) Look for:
#       ✅ Green check → You passed!
#       ❌ Red X → Fix code in Codespaces → Commit & Push again.
# ────────────────────────────────────────────────


def say_hello(name: str) -> str:
    # TODO: return "Hello, <name>"
    return "Hello, " + name


# 📖 EXPLANATION (read after you solve)
# 1) def say_hello(name: str) -> str:
#    • defines a function named say_hello that takes a string called `name`
#    • -> str means it returns a string
# 2) return "Hello, " + name
#    • builds the exact message and returns it (no printing)
#
# Example:
#   say_hello("STEAM") → "Hello, STEAM"
