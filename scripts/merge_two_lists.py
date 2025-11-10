# Challenge #30 - Beginner
# Merge two lists into one
# Objective: Practice list manipulation, loops, and combining sequences

"""
Combine two separate lists into a single list.
Avoid using built-in shortcuts like list1 + list2 to focus on logic and iteration.
This helps understand how lists work internally and how to handle indexes manually.
"""

def merge_lists(list_1, list_2):
    """
    Return a new list that contains all elements from list_1 followed by all elements from list_2.
    """
    merged = []

    # Add elements from the first list
    for item in list_1:
        merged.append(item)

    # Add elements from the second list
    for item in list_2:
        merged.append(item)

    return merged


# Example test
list_a = [1, 3, 5, 7]
list_b = [2, 4, 6, 8]

print(f"\nMerged list: {merge_lists(list_a, list_b)}\n")
