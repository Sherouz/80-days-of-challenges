# Challenge #6 - Beginner
# Find the missing number using set difference
# Objective: Practice sets, range, and basic logic

"""
Find the missing number in a list of consecutive integers.

The function expects a list containing numbers from 1 to n with one missing.
It returns the missing number by comparing two sets (expected and actual).
"""

def locate_missing_value(sequence: list[int]) -> int:
    """
    locate_missing_value finds the single missing element in a sequence
    of consecutive integers starting from 1.
    """
    # The full range size including the missing value
    total_count = len(sequence) + 1  
    expected_numbers = set(range(1, total_count + 1))   # All numbers from 1 to n
    given_numbers = set(sequence)
    difference = expected_numbers - given_numbers   # Find what's missing
    # Return the missing number
    return difference.pop()  


# Example test
data = [1, 2, 3, 4, 6, 7, 8, 9, 10]
print(locate_missing_value(data))
