# Challenge #40 - Intermediate
# Armstrong numbers in a range
# Objective: Practice digit extraction, exponentiation, loops, and helper function.

"""
Find all Armstrong numbers within a given range.
An Armstrong number equals the sum of its digits raised to the digit count.
"""


def is_armstrong(n: int) -> bool:
    """
    Return True if n is an Armstrong number.
    """
    s = str(n)
    power = len(s)
    total = 0

    # Sum each digit raised to 'power'
    for d in s:
        total += int(d) ** power

    return total == n


# User input
start = int(input("Start: "))
end = int(input("End: "))

# Validate range
if start < 0 or end < 0:
    print("Range must contain non-negative integers only.")
    raise SystemExit

if start > end:
    print("Invalid range: start must be <= end.")
    raise SystemExit

# Collect Armstrong numbers
armstrong_nums = []

for num in range(start, end + 1):
    if is_armstrong(num):
        armstrong_nums.append(num)

# Output result
if armstrong_nums:
    print("Armstrong numbers in this range:")
    print(*armstrong_nums)
else:
    print("No Armstrong numbers found in this range.")
