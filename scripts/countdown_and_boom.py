# Challenge #24 - Beginner
# Countdown with "Boom" on multiples of 3
# Objective: Practice for loops, range() with step, and conditional checks using the modulo operator

"""
Perform a countdown from n to 1, printing "Boom" for every number divisible by 3.
Demonstrates reverse iteration with range() and conditional branching in Python.
A simple exercise for mastering loop control and arithmetic conditions.
"""

def countdown_and_boom(n: int) -> None:
    """
    Count down from n to 1, printing "Boom" instead of numbers divisible by 3.
    """
    print(f"\n--- Starting countdown from {n} ---")

    # Use a for loop with range() to count down
    # range(start, stop, step) -> stop is exclusive, so it stops right before 0
    for i in range(n, 0, -1):
        # Check divisibility by 3 using the modulo (%) operator
        if i % 3 == 0:
            print("Boom")     # Print "Boom" for multiples of 3
        else:
            print(i)          # Otherwise, print the number itself

    print("--- Countdown finished ---\n")


# Example test
countdown_and_boom(7)
