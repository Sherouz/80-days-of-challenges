# Challenge #72 - Intermediate
# Sliding Window Maximum
# Objective: Find maximum value in each sliding window using a deque.

"""
Find the maximum element in every sliding window of size k.
Demonstrates deque usage for optimal O(n) window processing.
Useful for streaming data and real-time analytics.
"""

from collections import deque


def sliding_window_max(nums: list[int], k: int) -> list[int]:
    """Return list of maximums for each sliding window."""
    dq = deque()          # store indices of useful elements
    result = []

    for i, val in enumerate(nums):
        # remove indices that are out of the current window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # remove smaller values from the back
        while dq and nums[dq[-1]] <= val:
            dq.pop()

        dq.append(i)      # add current index

        # window becomes valid when i >= k - 1
        if i >= k - 1:
            result.append(nums[dq[0]])  # front holds max

    return result


if __name__ == "__main__":
    raw = input("Enter numbers (space-separated): ").strip()
    nums = list(map(int, raw.split()))

    k = int(input("Enter window size k: ").strip())

    output = sliding_window_max(nums, k)
    print(f"Sliding window maximums: {output}")
