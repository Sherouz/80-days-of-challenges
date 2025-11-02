# Challenge #22 - Beginner
# Count even and odd numbers in a list with improved messages
# Objective: Practice loops, conditionals, type checking, and dictionary usage

"""
Count the number of even and odd integers in a list.
Raises an error if any float is found in the list.
Returns a clear, user-friendly message with the counts.
Good practice for loops, conditionals, and type checking.
"""

def count_even_odd(numbers: list) -> str:
    """
    Counts even and odd integers in the list.
    Raises an error if a float is found.
    Returns a user-friendly message.
    """
    even_count = 0  # initialize even counter
    odd_count = 0   # initialize odd counter

    for num in numbers:
        # Check if the number is a float
        if isinstance(num, float):
            raise ValueError(f"Error: Found a float value ({num}). Please provide only integers.\n")
        
        # Count even or odd
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Return formatted message
    return f"\nIn your list: {even_count} even numbers and {odd_count} odd numbers.\n"


# Example usage
try:
    my_list = [10, 21, 4, 45, 66, 93, 0]  # example list with integers
    message = count_even_odd(my_list)
    print(message)
except ValueError as ve:
    # Print error message in a clear format
    print(f"\n[ERROR] {ve}")
