# Challenge #51 - Intermediate
# First Non-Repeating Character
# Objective: Practice frequency counting, iteration, and handling edge cases efficiently.

"""
Given a string, find the first character that does NOT repeat.
Return None if there is no unique character.
"""

def first_unique_char(s: str):
    """
    Return the first non-repeating character in the given string.
    Uses a frequency map to count occurrences, then scans again
    to find the first character with count equal to 1.
    """
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch

    return None


# Main program
user_input = input("Enter a string: ").strip()

result = first_unique_char(user_input)

if result is None:
    print("No unique character found.")
else:
    print("First non-repeating character:", result)
