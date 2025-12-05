# Challenge #55 - Intermediate
# Manual Statistics: Mean & Median
# Objective: Calculate mean and median manually without using 'statistics'.

"""
Compute the mean and median of a numeric list without external libraries.
Demonstrates manual data analysis logic through sorting and index-based selection.
Useful for understanding basic statistical calculations in data processing workflows.
"""

def calculate_stats(nums: list[int]) -> dict:
    """
    Compute mean and median manually.
    Returns a dictionary: {'mean': X, 'median': Y}
    """
    if not nums:
        return {'mean': None, 'median': None}  # handle empty input safely

    n = len(nums)

    # Mean
    mean_value = sum(nums) / n

    # Median
    sorted_nums = sorted(nums)
    mid = n // 2

    if n % 2 == 1:
        median_value = sorted_nums[mid]   # odd length -> middle number
    else:
        median_value = (sorted_nums[mid] + sorted_nums[mid - 1]) / 2   # even length

    return {
        'mean': mean_value,
        'median': median_value
    }


# Main program
raw = input("Enter numbers (space-separated): ").strip()

if raw == "":
    print("No input provided. Exiting.")
else:
    nums = list(map(int, raw.split()))
    stats = calculate_stats(nums)
    print("Mean:", stats['mean'])
    print("Median:", stats['median'])
