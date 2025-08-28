# 🐍 Exercise 4: Functions & Logic (Even Numbers)
# You made it this far STEAMER — nice! ✨
#
# In this challenge you’ll combine **functions** with a bit of **logic**.
# Even numbers are divisible by 2 (no remainder).
#
# 📝 Task:
# Write a function `is_even(n)` that returns:
#   True  if n is even
#   False otherwise
#
# Examples:
#   is_even(4)  → True
#   is_even(3)  → False
#
# ▶️ Run tests with:
#   source .venv/bin/activate
#   pytest -q
#
# 💡 Hint: Use the modulo operator `%` to get the remainder (n % 2)

def is_even(n: int) -> bool:
    """Return True if n is even, else False."""
    return n % 2 == 0


# 📖 Explanation (read after you solve!)
#
# - `n % 2` gives the remainder after dividing n by 2
# - Even numbers have remainder 0 → (n % 2 == 0) is True
# - Odd numbers have remainder 1 → (n % 2 == 0) is False
#
# Example walk-through:
#   n = 10 → 10 % 2 == 0 → True
#   n =  7 →  7 % 2 == 1 → False
#
# 🚀 Bonus Challenge:
# - Write `is_odd(n)` using your `is_even`:
#     def is_odd(n): return not is_even(n)
# - Write `only_evens(nums: list[int]) -> list[int]` that filters a list to just the even numbers.
