# 🐍 Exercise 4: Functions & Logic (Even Numbers)
# You made it this far STEAMER — nice! ✨
#
# In this challenge you’ll combine **functions** with a bit of **logic**.
# Even numbers are divisible by 2 (no remainder).
#
# # 📝 TASK
# Write a function `combine(a, b)` that returns the sum of a and b.
#
# 📚 Example Scenario:
# You are running a lemonade stand.
# You sell 2 cups in the morning and 3 cups in the afternoon.
# Your program should add them up:
#   combine(2, 3) → 5
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
