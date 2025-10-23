# Challenge #12 - Beginner
# Find the longest word in a sentence (without using len)
# Objective: Practice manual counting, loops, and logic

"""
Return the longest word from a given sentence.
Counts character lengths manually using loops instead of len().
Good for understanding how len() works internally and reinforcing loop logic.
"""

def find_longest_word(sentence: str) -> tuple[str, int]:
    """
    Find the longest word in a sentence without using len().
    Returns the word and its length. Returns an empty string and zero if input is blank.
    """
    if not sentence.strip():
        return "", 0   # Handle empty or whitespace-only input
    
    word_list = sentence.split()   # Split the sentence into a list of words
    longest_word = ""
    longest_length = 0

    # Iterate through each word in the list to find the longest one
    for current_word in word_list:
        # Count manually instead of using len()
        current_length = 0
        for _ in current_word:
            current_length += 1

        # If current word is longer than the longest found so far, update longest_word and longest_length
        if current_length > longest_length:
            longest_word = current_word
            longest_length = current_length

    # Return the longest word and its length as a tuple
    return longest_word, longest_length   


# Example usage
user_sentence = input("Enter a sentence: ")
word, length = find_longest_word(user_sentence)
print(f"\nThe longest word is '{word}' with length {length}.\n")
