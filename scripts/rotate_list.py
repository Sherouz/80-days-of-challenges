# Challenge #31 - Beginner
# Rotate list elements to the right by one position
# Objective: Practice list manipulation, indexing, and handling edge cases

"""
Rotate all elements in a list to the right by one position.
The last element becomes the first element.
Avoid using built-in rotation methods or slicing tricks like lst[-1:] + lst[:-1].
Focus on understanding how to manually shift list elements.
"""

def rotate_list_right(lst):
    """
    Rotate the given list to the right by one position.
    Returns the rotated list.
    """
    if len(lst) <= 1:
        return lst  # No change needed for empty or single-element lists

    last_element = lst[-1]   # Store last element
    for i in range(len(lst) - 1, 0, -1):   # Shift elements to the right
        lst[i] = lst[i - 1]
    lst[0] = last_element   # Place last element at the front

    return lst


# Example test
print(rotate_list_right([5, 3, 9, 1, 7]))
