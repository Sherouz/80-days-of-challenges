# Challenge #2 - Beginner
# Remove duplicates from a list while preserving order
# Objective: Practice list manipulation, sets, and conditional logic

"""
Given a list of items, return a new list containing only the first occurrence
of each element, preserving the original order.

This exercise helps practice set usage for tracking seen elements and
understanding how to maintain order in Python lists.
"""

def remove_duplicates(items):
    """
    Remove duplicates from a list while keeping only the first occurrence
    of each element and preserving the original order in the returned list.
    Uses a set to efficiently track seen elements for O(1) lookup time.
    """
    first_seen = []
    memory = set()

    for item in items:
        if item not in memory:
            first_seen.append(item)  # Add first occurrence to the result
            memory.add(item)         # Mark item as seen

    return first_seen

# Example test
my_list = [3, 5, 2, 3, 5, 7, 2, 8, 3, 5, 5, 4, 5]
print(remove_duplicates(my_list))
