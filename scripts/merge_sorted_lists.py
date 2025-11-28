# Challenge #48 - Intermediate
# Merge Two Sorted Lists (Two-Pointer Technique)
# Objective: Practice pointer-based merging without using built-in sorting.

"""
Merge two individually sorted lists into a single sorted list.
Uses the two-pointer technique for O(n) time merging.
Avoids using sort() or sorted() on the combined list.
"""

def merge_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:
    """
    Merge two pre-sorted lists into one sorted list using the two-pointer method.
    Returns a new sorted list containing all elements from both lists.
    """
    i, j = 0, 0
    result = []

    # Merge while both lists have elements remaining
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    # Add remaining elements from list1 (if any)
    while i < len(list1):
        result.append(list1[i])
        i += 1

    # Add remaining elements from list2 (if any)
    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result


# Main program
print("Enter the first sorted list (space-separated integers): ")
list1 = list(map(int, input().strip().split()))

print("Enter the second sorted list (space-separated integers): ")
list2 = list(map(int, input().strip().split()))

merged = merge_sorted_lists(list1, list2)
print("Merged result:", merged)
