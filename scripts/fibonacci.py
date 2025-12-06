# Challenge #56 - Intermediate
# Fibonacci Sequence (Efficient)
# Objective: Compute the nth Fibonacci number using an O(n) iterative approach.

"""
Compute the nth Fibonacci number efficiently using iterative updates.
Demonstrates state tracking and numeric progression without recursion overhead.
Useful for understanding optimized sequence generation in algorithm design.
"""

def fibonacci(n: int) -> int:
    """
    Return the nth Fibonacci number using an iterative O(n) method.
    Handles n = 0 and n = 1 explicitly.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return 0
    if n == 1:
        return 1

    prev = 0       # F0
    curr = 1       # F1

    for _ in range(2, n + 1):
        next_value = prev + curr
        prev = curr
        curr = next_value

    return curr


# Main program
raw = input("Enter n (non-negative integer): ").strip()

if raw == "":
    print("No input provided. Exiting.")
else:
    n = int(raw)
    result = fibonacci(n)
    print(f"Fibonacci number F{n} =", result)
