# Challenge #71 - Intermediate
# Three Sum
# Objective: Find all unique triplets that sum to zero using two pointers.

"""
Find all unique triplets in an array that sum to zero.
Demonstrates sorting, two-pointer technique, and duplicate handling.
Useful for mastering array scanning and pointer-based optimization.
"""

def three_sum(nums: list[int]) -> list[list[int]]:
    """Return all unique triplets [a, b, c] such that a + b + c == 0."""
    nums.sort()                         # sort array for two-pointer logic
    result = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue                    # skip duplicate first elements

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                # skip duplicate values for left pointer
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # skip duplicate values for right pointer
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1               # need a larger sum
            else:
                right -= 1              # need a smaller sum

    return result


if __name__ == "__main__":
    raw = input("Enter numbers (space-separated): ").strip()
    nums = list(map(int, raw.split()))

    triplets = three_sum(nums)
    print(f"Triplets with zero sum: {triplets}")
