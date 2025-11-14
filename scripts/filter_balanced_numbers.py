# Challenge #34 - Intermediate
# Balanced numbers filter (Enhanced)
# Objective: Practice modular design, input validation, and cleaner digit analysis.

"""
Check which numbers in a list are 'balanced'.
A balanced number has equal counts of even and odd digits.
Handles negative integers by ignoring the minus sign.
Validates input to ensure all elements are integers.
Uses a helper function to determine if a single number is balanced.
"""

from typing import Iterable, List


def count_even_odd_digits(num: int) -> tuple[int, int]:
    """
    Return a tuple (even_count, odd_count) for the given integer.
    Handles negative numbers by ignoring the minus sign.
    """
    even = 0
    odd = 0

    for digit in str(abs(num)):     # abs to ignore negative sign
        d = ord(digit) - 48         # faster than int(digit), still readable
        if d % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


def is_balanced_number(num: int) -> bool:
    """
    Return True if even digit count equals odd digit count.
    """
    # Count the number of even and odd digits in `num`
    even_count, odd_count = count_even_odd_digits(num)
    # Return True if the number of even digits equals the number of odd digits
    return even_count == odd_count



def filter_balanced_numbers(numbers: Iterable[int]) -> List[int]:
    """
    Return a list of balanced numbers from any iterable of integers.
    Raises a ValueError if elements are not integers.
    """
    result = []  # Empty list to store numbers that are balanced

    for n in numbers:  # Iterate over each element in the input list
        if not isinstance(n, int):  # If the element is not an integer, it's invalid
            raise ValueError(f"Invalid element detected: {n} (expected int)")  # Raise an error for invalid input types

        if is_balanced_number(n):  # Check whether the current number is balanced
            result.append(n)  # If balanced, add it to the result list

    return result  # Return the list of all balanced numbers found


# Example usage
if __name__ == "__main__":
    nums = [1234, 550, -78, 6, 2024, 51, 1314, -909, 33, 2023]
    balanced = filter_balanced_numbers(nums)
    print("\n🎯 Balanced numbers:", balanced, "\n")
