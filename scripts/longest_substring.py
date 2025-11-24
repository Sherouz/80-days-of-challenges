# Challenge #44 - Intermediate
# Longest Substring Without Repeating Characters
# Objective: Practice sliding window technique, sets, and substring tracking.

"""
Find the length of the longest substring without repeating characters.
Uses a sliding window approach for O(n) time complexity.
"""

def length_of_longest_substring(s: str) -> int:
    """
    Return the length of the longest substring without duplicates.
    Sliding window approach using a set for current window characters.
    """
    char_set = set()  # Set for current window characters
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:  # If duplicate, shrink window from left
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Main program
input_str = input("Enter a string: ").strip()
result = length_of_longest_substring(input_str)
print(f"Result: {result}")
