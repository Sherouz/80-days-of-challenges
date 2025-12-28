# Challenge #78 - Intermediate
# Move Zeros to End
# Objective: Move all zeros to the end while preserving order.

"""
Move all zeros in an array to the end without changing
the relative order of non-zero elements.
Demonstrates in-place array manipulation with two pointers.
"""

def move_zeros(nums: list[int]) -> None:
    """Modify the list in-place by moving zeros to the end."""
    write = 0    # position to write next non-zero

    # move non-zero elements forward
    for num in nums:
        if num != 0:
            nums[write] = num
            write += 1

    # fill remaining positions with zeros
    for i in range(write, len(nums)):
        nums[i] = 0


if __name__ == "__main__":
    raw = input("Enter numbers (space-separated): ").strip()
    nums = list(map(int, raw.split()))

    move_zeros(nums)
    print(f"After moving zeros: {nums}")
