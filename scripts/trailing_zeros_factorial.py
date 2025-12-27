# Challenge #77 - Intermediate
# Trailing Zeros in Factorial
# Objective: Count trailing zeros in n! using number theory.

"""
Count the number of trailing zeros in the factorial of a number.
Demonstrates number theory insight by counting factors of 5.
Useful for large-number analysis without computing factorial directly.
"""

def trailing_zeros(n: int) -> int:
    """Return the number of trailing zeros in n!."""
    count = 0
    divisor = 5

    while divisor <= n:
        count += n // divisor        # count multiples of current power of 5
        divisor *= 5                 # move to next power of 5

    return count


if __name__ == "__main__":
    n = int(input("Enter a non-negative integer: ").strip())
    zeros = trailing_zeros(n)

    print(f"Trailing zeros in {n}! : {zeros}")
