# Challenge #27 - Beginner
# Find the most frequent element in a list (Mode)
# Objective: Practice dictionary counting and looping logic

"""
Given a list of items (numbers or strings), find and return
the element that appears most frequently in the list.
This demonstrates how to use dictionaries to count occurrences.
"""

def most_frequent_element(items):
    """
    Return the most frequent element from the given list.
    """
    if not items:
        raise ValueError("items must not be empty")
    
    frequency = {}  # Dictionary to store element counts
    
    for item in items:
        frequency[item] = frequency.get(item, 0) + 1  # Increment count or set to 1
    
    # Find element with the highest count
    most_common = max(frequency, key=frequency.get)
    
    return most_common


# Example tests
print(most_frequent_element([1, 3, 2, 1, 4, 1]))  # -> 1
print(most_frequent_element(['apple', 'banana', 'apple', 'orange', 'apple']))  # -> 'apple'
print(most_frequent_element([5, 2, 5, 2, 5]))  # -> 5
