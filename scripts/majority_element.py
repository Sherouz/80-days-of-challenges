# Challenge #45 - Intermediate
# Boyer-Moore Majority Vote Algorithm
# Objective: Find the element that appears more than n/2 times with O(n) time and O(1) space.

"""
Return the majority element using Boyer-Moore voting.
Guaranteed that a majority element exists.
"""

def majority_element(nums):
    """
    Track a candidate and adjust count.
    Majority exists, so candidate at the end is the answer.
    """
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate


# Main program
arr = list(map(int, input("Enter numbers separated by space: ").split()))
result = majority_element(arr)
print(f"Majority element: {result}")
