# Challenge #4 - Beginner-Intermediate
# Prime number checker (optimized)
# Objective: Practice loops, conditionals, and optimization using the 6k ± 1 rule.

"""
Determine whether a given number is prime.

A prime number is greater than 1 and has no divisors other than 1 and itself.
This version uses an optimized approach that checks divisibility only up to √n,
and skips even numbers and multiples of 3 to improve performance.
"""

def check_prime(n):
    """
    Check if a number is prime using an optimized method.
    Returns True if the number is prime, False otherwise.
    """
    # Numbers less than 2 are not prime
    if n < 2:
        return False

    # 2 and 3 are prime numbers
    if n in (2, 3):
        return True

    # Eliminate even numbers and multiples of 3 early
    if n % 2 == 0 or n % 3 == 0:
        return False 

    # Check potential divisors using the 6k ± 1 rule
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False  # Found a divisor, not prime

    # If no divisors found, the number is prime
    return True


# Example usage
number = int(input("Enter a number: "))
print("Prime" if check_prime(number) else "Not prime")
