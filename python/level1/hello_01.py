# 🐍 Exercise 1: Say Hello
# ────────────────────────────────────────────────
# 📘 BEFORE YOU BEGIN:
# Read docs/STUDENT_QUICK_START.md
# That guide shows how to use Codespaces, the Terminal,
# and how to save your work (Commit & Push).
#
# 🌟 GOAL
# Write a function that returns:
#   "Hello, <name>"
#
# 📝 TASK
# 
# Write a function `say_hello(name)` that returns exactly:
#  
#
# 📚 Example Scenario:
# Imagine you are building a robot greeter at the front of a museum.
# When someone types their name, the robot should greet them back:
#   say_hello("Maya") → "Hello, Maya"#
#
# 💡 HINT
# Use: return "Hello, " + name
# (Don’t print — tests check the return value.)
#
# 📖 DEFINITIONS
# • Function → a reusable block of code that does one job.
# • Parameter → the input a function needs (here: `name`).
# • Return value → the single value the function sends back.
# • String concatenation → joining strings with `+`
#       Example: "Hello, " + name
# ────────────────────────────────────────────────

def say_hello(name: str) -> str:
    # TODO: return "Hello, <name>"
    return "Hello, " + name


# 🧪 HOW TO TEST IN CODESPACES
# 1) Open the Terminal at the bottom.
# 2) Type: python
# 3) Import your function:
#       from python.level1.hello_01 import say_hello
# 4) Call it:
#       say_hello("Taz")   → 'Hello, Taz'
#       say_hello("STEAM") → 'Hello, STEAM'
# 5) Exit Python with: exit()


# 📖 EXPLANATION OF THE CODE
#
# 1. def say_hello(name: str) -> str:
#    • `def` means we are defining a function.
#    • `say_hello` is the function’s name.
#    • `(name: str)` means the function takes one input called `name` (a string).
#    • `-> str` tells us the function will return a string.
#
# 2. return "Hello, " + name
#    • `"Hello, "` is a string.
#    • `+ name` joins the input name to that string.
#    • Example: if name = "Taz", then "Hello, " + "Taz" → "Hello, Taz"
#    • `return` sends this final string back to whoever called the function.
#
# Example Walk-through:
#   say_hello("STEAM")
#   → "Hello, " + "STEAM"
#   → "Hello, STEAM"
#
# 🎉 That’s it! You just wrote your first Python function.
#
# 🚀 BONUS (Optional)
# 1) Handle empty input:
#       if name == "": return "Hello!"
# 2) Format nicely:
#       return "Hello, " + name.title()
# 3) Add a second parameter:
#       def say_hello(name: str, greeting: str = "Hello") -> str:
#           return f"{greeting}, {name}"
