"""Lecture 10 demo: catch a logic bug with the step-by-step debugger.

Open this file in PyCharm or VS Code.
1. Click next to line 15 (total = total + price): a red dot, the breakpoint.
2. Run with Debug (the bug icon). The program pauses before line 15.
3. Press Step Over (PyCharm F8, VS Code F10) and watch price and total.
   Round 2: total should be 30, but it is 20. Why?
4. Fix: move "total = 0" above the loop, and run again. Expected: 60
"""


def total_price(prices):
    for price in prices:
        total = 0
        total = total + price
    return total


print(total_price([10, 20, 30]))
