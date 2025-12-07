# Challenge #57 - Intermediate
# GCD & LCM (Euclidean Algorithm)
# Objective: Implement GCD using Euclid's method and compute LCM using the GCD.

"""
Compute the GCD and LCM of two positive integers without using math.gcd.
Demonstrates Euclidean reduction for efficient divisor computation
and shows how modular function design combines results to compute LCM.
"""

def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor using Euclid's algorithm."""
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Return the least common multiple using the GCD result."""
    return abs(a * b) // gcd(a, b)


# Main program
raw_a = input("Enter first positive integer: ").strip()
raw_b = input("Enter second positive integer: ").strip()

if not raw_a or not raw_b:
    print("Invalid input. Exiting.")
else:
    a = int(raw_a)
    b = int(raw_b)

    result_gcd = gcd(a, b)
    result_lcm = lcm(a, b)

    print(f"GCD: {result_gcd}")
    print(f"LCM: {result_lcm}")
