# Challenge #43 - Intermediate
# Valid Parentheses Checker (Stack-based)
# Objective: Practice stack operations, dictionary mapping, and string scanning.

"""
Check if a string has valid parentheses using a stack.
Supports (), {}, [] and ignores all other characters.
Runs in O(n) time.
"""

def is_valid(s: str) -> bool:
    """
    Validate parentheses using stack logic.
    Returns True if all brackets close correctly.
    """
    stack = []  # Stack for open brackets
    pairs = {")": "(", "}": "{", "]": "["}  # Closing -> Opening

    for char in s:
        if char in pairs.values():  # Opening bracket
            stack.append(char)
        elif char in pairs:  # Closing bracket
            if not stack or stack.pop() != pairs[char]:
                return False
        # Ignore all non-bracket characters

    return len(stack) == 0  # Must end with an empty stack


# Main program
input_str = input("Enter a string: ").strip()

if is_valid(input_str):
    print("Result: True (valid parentheses)\n")
else:
    print("Result: False (invalid parentheses)\n")
