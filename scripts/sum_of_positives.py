# Challenge #23 - Beginner
# Sum of positive numbers in a list
# Objective: Practice conditional statements, for loops, and basic accumulation logic

"""
Calculate the sum of all positive numbers in a given list.
Demonstrates iteration, conditional checks, and numeric accumulation in Python.
Useful for filtering and aggregating specific data from collections.
"""

def sum_of_positives(numbers: list[int]) -> int:
    """
    Return the sum of positive numbers from the input list.
    """
    # Initialize a variable to keep the running total of positive numbers
    total = 0
    for number in numbers:           # Loop through each number in the list
        if number > 0:               # Check if the current number is positive
            # Add it to the total if it's positive
            total += number
    return total



# Example usage
sample_list = [5, -3, 15, -10, 2, 0, -13, 1]
result = sum_of_positives(sample_list)
print(f"\nList: {sample_list}")
print(f"Sum of positive numbers: {result}\n")
