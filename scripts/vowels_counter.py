# Challenge #19 - Beginner
# Count vowels in a given text using a function
# Objective: Practice functions, loops, string methods, and counting

"""
Define a function to count vowels in any given text.
Shows how to encapsulate logic in a function and return results cleanly.
"""

def count_vowels(text_input: str) -> int:
    """Return the number of vowels in the given text (case-insensitive)."""
    vowels_list = ["a", "e", "i", "o", "u"]
    count = 0
    for letter in text_input:
        if letter.lower() in vowels_list:
            count += 1
    return count

# Example usage
user_text = input("💬 Type something, and I'll find all the vowels for you: ")
total_vowels = count_vowels(user_text)
print(f"Your text contains {total_vowels} vowels.")
