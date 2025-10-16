# Challenge #5 - Beginner/Intermediate
# Safe interactive factorial calculator
# Objective: Practice loops, recursion, input validation, and user-friendly I/O

"""
Interactive factorial calculator handling both iterative and recursive methods.
Prompts user for non-negative integers and validates input until correct.
Displays results safely for large numbers and warns when recursion depth is exceeded.
"""

def factorial_iterative(n: int) -> int:
    """
    Calculate n! using an iterative loop.
    n: non-negative integer.
    Returns 1 for 0; raises ValueError for negative n.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiply step by step

    return result


def factorial_recursive(n: int) -> int:
    """
    Calculate n! using recursion.
    n: non-negative integer.
    Returns 1 for 0; raises ValueError for negative n.
    Note: limited by Python's recursion depth (~1000).
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)  # Recursive case


def get_non_negative_integer(prompt="Enter a non-negative integer: ") -> int:
    """Prompt user until they enter a valid non-negative integer."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("⚠️  Please enter a non-negative integer.")
                continue
            return value
        except ValueError:
            print("⚠️  Invalid input. Please enter an integer.")


# Optional interactive section
if __name__ == "__main__":
    n = get_non_negative_integer()

    # Iterative factorial (always safe)
    iterative_result = factorial_iterative(n)

    # Recursive factorial (may fail for large n)
    try:
        recursive_result = factorial_recursive(n)
    except RecursionError:
        recursive_result = None
        print(f"  Recursive factorial not calculated: n={n} is too large for recursion.")

    # Print results
    print(f"\nIterative factorial of {n}:", iterative_result)
    if recursive_result is not None:
        print(f"Recursive factorial of {n}:", recursive_result)

    # If the number is huge, summarize length
    if len(str(iterative_result)) > 100:
        print(f"ℹ️  Note: The factorial has {len(str(iterative_result))} digits. Displaying first 100 digits:")
        print(str(iterative_result)[:100] + "...")
