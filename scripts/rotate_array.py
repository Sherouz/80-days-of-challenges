# Challenge #47 - Intermediate
# Rotate Array
# Objective: Practice list slicing, indexing, and handling large k values.

"""
Rotate a list to the right by k steps.
Handles cases where k > len(nums) efficiently.
Example:
    [1,2,3,4,5], k=2 -> [4,5,1,2,3]
"""

def rotate_list(nums: list[int], k: int) -> list[int]:
    """
    Rotate the input list to the right by k positions.
    Returns a new rotated list without modifying the original.
    """
    n = len(nums)
    if n == 0:
        return nums  # empty list, nothing to rotate
    k = k % n  # handle k > n
    return nums[-k:] + nums[:-k]  # slice and concatenate


# Main program
input_nums = list(map(int, input("Enter the list of numbers (space-separated): ").split()))
k_steps = int(input("Enter the number of steps to rotate: "))
rotated = rotate_list(input_nums, k_steps)
print("Rotated list:", rotated)

