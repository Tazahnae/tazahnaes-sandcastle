# 🔁 Exercise 3: Loops
# Welcome, STEAM Coder! ✨
#
# ────────────────────────────────────────────────
# 📘 BEFORE YOU BEGIN
# All coding is done in **GitHub Codespaces**.
# Open this file in Codespaces: python/level1/loops_03.py
# Complete the TODOs, then follow SAVE + CHECK steps.
#
# 📖 DEFINITIONS
# • Loop → repeats actions multiple times.
# • for-loop → goes through each item in a list.
# • while-loop → repeats while a condition is True.
# • Accumulator → a variable that collects a running result.
# ────────────────────────────────────────────────
#
# 📝 TASKS
# 1) write `sum_list(nums)` → return the sum of all numbers in the list using a for-loop
# 2) write `countdown(n)`   → return a list counting down from n to 1 using a while-loop
#
# 📚 Example Scenario:
# • sum_list: You’re tracking the points your team scores each round of a game.
#   sum_list([10, 15, 20]) → 45
#
# • countdown: You’re making a timer for a race.
#   countdown(3) → [3, 2, 1]
#
# EXAMPLES
#   sum_list([1, 2, 3])     → 6
#   countdown(5)            → [5, 4, 3, 2, 1]
#
# 💡 HINTS
# • Start your total at 0 and add each number (accumulator pattern).
# • For countdown, decrease n each loop until it reaches 0.
#
# 🧪 HOW TO TEST IN CODESPACES
# 1) Open the Terminal.
# 2) Type: python
# 3) Import functions:
#       from python.level1.loops_03 import sum_list, countdown
# 4) Try them:
#       sum_list([2, 5, 8])     → 15
#       countdown(3)            → [3, 2, 1]
# 5) Exit Python:  exit()  or press Ctrl + D
# ────────────────────────────────────────────────
# 💾 SAVE + CHECK YOUR WORK
# 1) Source Control → write a message (example: finish loops)
# 2) Click **Commit & Push** (or **Sync Changes**)
# 3) On GitHub → **Actions** tab → open *Python tests*
# 4) Look for:
#       ✅ Green check → You passed!
#       ❌ Red X → Fix in Codespaces → Commit & Push again
# ────────────────────────────────────────────────

from typing import List

def sum_list(nums: List[int]) -> int:
    """Return the sum of all integers in nums using a for-loop."""
    # TODO: accumulate total and return it
    total = 0
    for n in nums:
        total += n
    return total


def countdown(n: int) -> list:
    """Return [n, n-1, ..., 1] using a while-loop."""
    # TODO: build a list by decreasing n until it reaches 0
    out = []
    while n > 0:
        out.append(n)
        n -= 1
    return out
