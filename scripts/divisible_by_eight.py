# Challenge #11 - Beginner
# Print numbers divisible by 8
# Objective: Practice loops, list comprehension, and input validation

"""
Ask the user for a positive integer and print all numbers
from 1 up to that integer that are divisible by 8.
Focus on practicing iteration, conditions, and input handling.
"""

def print_divisible_by_eight(limit: int) -> None:
    """
    Print all numbers from 1 to 'limit' that are divisible by 8.
    """
    # Use list comprehension to collect numbers in range(1, limit+1) where modulo 8 equals zero
    divisible_numbers = [num for num in range(1, limit + 1) if num % 8 == 0]  # Find numbers divisible by 8
    print(f"Numbers from 1 to {limit} divisible by 8: {divisible_numbers}")    # Display result


def get_positive_integer() -> int:
    """
    Ask the user for a positive integer input.
    """
    while True:
        try:
            value = int(input("Enter a positive integer: "))  # Convert input to integer
            if value > 0:
                return value
            print("The number must be positive. Try again.")  # Handle non-positive input
        except ValueError:
            print("Invalid input. Enter a valid integer.")    # Handle invalid input


# Example test
if __name__ == "__main__":
    number = get_positive_integer()
    print_divisible_by_eight(number)
