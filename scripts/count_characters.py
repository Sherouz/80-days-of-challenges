# Challenge #3 - Beginner
# Count character frequency in a string
# Objective: Practice dictionary usage, string manipulation, and loops

"""
Count the occurrence of each character in a given string.
The function ignores case by converting all letters to lowercase.
"""

def count_chars(text):
    """
    Count the frequency of each character in a string.
    Converts all letters to lowercase for case-insensitive counting.
    Returns a dictionary mapping characters to their counts.
    """
    text = text.lower()  
    counts = {}  

    for char in text: 
        if char in counts:
            counts[char] += 1  # Increment count if character already in dictionary
        else:
            counts[char] = 1   # Add new character to dictionary with count 1

    return counts


# Example usage
text = "Hello world"
result = count_chars(text)

# Sort dictionary by key for nicer output
sorted_result = dict(sorted(result.items()))
print(sorted_result)
