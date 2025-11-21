# Challenge #41 - Intermediate
# Happy Number Checker
# Objective: Practice loops, digit extraction, sets for cycle detection, and step-by-step output.

"""
Check whether a number is a Happy Number.
A happy number eventually reaches 1 when replaced by the sum of the squares of its digits.
If it enters a cycle that does not include 1, it's unhappy.
"""

def sum_of_squares(n: int) -> int:
    """
    Return the sum of the squares of the digits of n.
    """
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** 2
        n //= 10
    return total


def is_happy(number: int) -> None:
    """
    Determine if 'number' is a happy number.
    Prints the full transformation sequence.
    """
    seen = set()       # To detect cycles
    steps = []         # To display the sequence

    while number != 1 and number not in seen:
        seen.add(number)
        steps.append(number)
        number = sum_of_squares(number)

    steps.append(number)  # Add final number (1 or repeated number)

    # Print the sequence
    print(" → ".join(map(str, steps)))

    if number == 1:
        print(f"Number {steps[0]} is a Happy Number! 🎉")
    else:
        print(f"Number {steps[0]} is NOT a Happy Number 😢 (stuck in a cycle)")


# User input
num = int(input("Enter a positive number: "))
if num < 1:
    print("Please enter a positive integer.")
else:
    is_happy(num)
