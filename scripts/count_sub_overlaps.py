# Challenge #53 - Intermediate
# Count Overlapping Substrings
# Objective: Practice manual substring searching, index management, and edge-case handling.

"""
Count occurrences of a pattern inside a text including overlapping matches.

Python's str.count() does NOT count overlapping occurrences,
so we implement a simple sliding-window check.
"""

def count_overlapping_substrings(text: str, pattern: str) -> int:
    """
    Return the number of times 'pattern' appears in 'text',
    counting overlapping occurrences.

    Behavior notes:
    - If pattern is empty, returns 0 (no well-defined matches).
    - Case-sensitive by default.
    """
    if not pattern:    # avoid infinite/ambiguous matches
        return 0

    n, m = len(text), len(pattern)
    if m > n:       # pattern longer than text -> zero matches
        return 0

    count = 0
    # Slide a window of length `m` over `text` and compare slices
    for i in range(0, n - m + 1):    # i is the start index of the window
        if text[i : i + m] == pattern:
            count += 1

    return count


# Main program
text_input = input("Enter the text: ").rstrip("\n")
pattern_input = input("Enter the pattern to search for: ").rstrip("\n")

if pattern_input == "":
    print("Pattern is empty. Returning 0.")
else:
    occurrences = count_overlapping_substrings(text_input, pattern_input)
    print(f"Overlapping occurrences of '{pattern_input}' in the text:", occurrences)
