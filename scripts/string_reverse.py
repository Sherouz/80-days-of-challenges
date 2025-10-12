# Challenge #1 - Beginner
# Reverse a string using two-pointer method
# Objective: Practice list manipulation, pointers, and while loops

"""
Reverse a given string without using built-in reversal functions
(e.g., [::-1] or reversed()) to practice list manipulation and two-pointer logic.
"""

def reverse_string_pointers(text):
    """
    Reverse a string using the two-pointer method.
    """
    text_list = list(text)  # Convert string to list so we can swap characters
    left, right = 0, len(text) - 1  # Initialize two pointers: start and end

    while left < right:
        text_list[left], text_list[right] = text_list[right], text_list[left] # Swap characters
        left += 1   # Move left pointer right
        right -= 1

    return "".join(text_list) # Convert list back to string


# Example test
print(reverse_string_pointers("\nPython"))
