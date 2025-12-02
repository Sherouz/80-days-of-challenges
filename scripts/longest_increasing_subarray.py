# Challenge #52 - Intermediate
# Longest Continuous Increasing Subsequence (LCIS)
# Objective: Practice loop logic, neighbor comparison, state tracking, and edge-case handling.

"""
Find the length of the longest continuous strictly-increasing subsequence.

A "continuous increasing subsequence" means elements must be
adjacent in the list and each number must be strictly greater
than the previous one.
"""

def find_longest_increasing_subarray(nums: list[int]) -> int:
    """
    Return the length of the longest continuous strictly-increasing subsequence.
    Uses a simple linear scan comparing each element with its previous one.
    """
    if not nums:
        return 0

    max_streak = 1    # longest streak found so far
    current_streak = 1    # length of the current increasing sequence

    # iterate from the second element onward
    for i in range(1, len(nums)):

        # check if current number is strictly increasing
        if nums[i] > nums[i - 1]:
            current_streak += 1    # extend current streak
        else:
            current_streak = 1    # reset when sequence breaks

        # update maximum if needed
        if current_streak > max_streak:
            max_streak = current_streak

    # final length of longest increasing streak
    return max_streak


# Main program
raw_input_nums = input("Enter numbers (space-separated): ").strip()

if not raw_input_nums:
    print("No numbers provided. Exiting.")
else:
    nums = list(map(int, raw_input_nums.split()))
    result = find_longest_increasing_subarray(nums)
    print("Length of the longest continuous increasing subsequence:", result)
