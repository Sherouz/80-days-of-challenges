# Challenge #80 - Intermediate
# Search in Rotated Sorted Array
# Objective: Find an element using modified binary search.

"""
Search for a target value in a rotated sorted array.
Demonstrates binary search adaptation with rotation logic.
Useful for understanding decision-based search optimization.
"""

def search_rotated(nums: list[int], target: int) -> int:
    """Return index of target in rotated sorted array, or -1 if not found."""
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1          # target in left half
            else:
                left = mid + 1           # target in right half
        # right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1           # target in right half
            else:
                right = mid - 1          # target in left half

    return -1


if __name__ == "__main__":
    raw = input("Enter rotated sorted numbers (space-separated): ").strip()
    nums = list(map(int, raw.split()))

    target = int(input("Enter target value: ").strip())

    index = search_rotated(nums, target)
    print(f"Target index: {index}")