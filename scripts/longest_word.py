# Challenge #8 - Beginner
# Find the longest word in a sentence
# Objective: Practice string manipulation, loops, and basic logic

"""
Return the longest word from a given sentence.
If multiple words share the maximum length, return the first one.
Useful for learning how to iterate over lists and compare lengths.
"""

def find_longest_word(sentence: str) -> str:
    """
    Find the longest word in a sentence.
    Returns the first one if there are ties.
    """
    if not sentence.strip():
        return ""   # Handle empty or whitespace-only input
    
    word_list = sentence.split()
    longest_word = ""

    for current_word in word_list:
        if len(current_word) > len(longest_word):
            longest_word = current_word

    return longest_word


# Example usage
sentence = "Python is an amazing programming language"
longest = find_longest_word(sentence)
print(f"\nThe longest word is '{longest}' with length {len(longest)}.\n")
