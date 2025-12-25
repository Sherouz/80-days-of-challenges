# Challenge #75 - Intermediate
# Counting Sort by Number of Zeros
# Objective: Sort numbers based on count of zeros using counting sort logic.

"""
Sort numbers based on the number of zeros in their decimal representation.
Demonstrates non-comparison sorting using counting/bucket strategy.
Useful when sorting by small, bounded keys.
"""

def count_zeros(n: int) -> int:
    """Return number of '0' digits in the integer."""
    return str(n).count("0")


def counting_sort_by_zeros(nums: list[int]) -> list[int]:
    """Sort numbers by the count of zeros using counting sort."""
    buckets = {}                      # map zero-count -> list of numbers

    for num in nums:
        z = count_zeros(num)          # count zeros in current number
        if z not in buckets:
            buckets[z] = []
        buckets[z].append(num)        # place number in its bucket

    result = []

    for z in sorted(buckets.keys()):  # iterate in increasing zero-count order
        result.extend(buckets[z])     # append numbers in each bucket

    return result


if __name__ == "__main__":
    raw = input("Enter numbers (space-separated): ").strip()
    nums = list(map(int, raw.split()))

    sorted_nums = counting_sort_by_zeros(nums)
    print(f"Sorted by zero count: {sorted_nums}")
