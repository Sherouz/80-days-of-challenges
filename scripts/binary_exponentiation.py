# Challenge #76 - Intermediate
# Binary Exponentiation
# Objective: Compute x^n efficiently in O(log n) time.

"""
Compute power using binary exponentiation.
Demonstrates logarithmic-time exponentiation and bit-based logic.
Useful for math-heavy algorithms and performance-critical code.
"""

def fast_power(x: float, n: int) -> float:
    """Return x raised to the power n using binary exponentiation."""
    if n == 0:
        return 1.0                     # base case: x^0 = 1

    if n < 0:
        x = 1 / x                     # invert base for negative exponent
        n = -n

    result = 1.0

    while n > 0:
        if n % 2 == 1:
            result *= x               # multiply when current bit is 1

        x *= x                        # square the base
        n //= 2                       # shift exponent right (divide by 2)

    return result


if __name__ == "__main__":
    base = float(input("Enter base (x): ").strip())
    exponent = int(input("Enter exponent (n): ").strip())

    value = fast_power(base, exponent)
    print(f"{base}^{exponent} = {value}")
