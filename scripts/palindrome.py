# Challenge #18 - Beginner
# Palindrome checker (case & punctuation insensitive)
# Objective: Practice string cleaning, slicing, and conditional logic

"""
Check whether a given text is a palindrome.
Ignores capitalization, spaces, and punctuation to focus purely on the character sequence.
Demonstrates string normalization and slicing in Python.
"""

def is_palindrome(text: str) -> bool:
    """
    Return True if the given text is a palindrome, ignoring case and punctuation.
    """
    # convert to lowercase and keep only alphanumeric characters
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())  # keep only letters and numbers
    return cleaned == cleaned[::-1]   # check if the cleaned string is the same forwards and backwards (palindrome check)


def run_palindrome_checker():
    """
    Interactively ask the user for input and display whether it's a palindrome.
    Handles empty input gracefully.
    """
    user_input = input("Enter text to check if it's a palindrome: ").strip()

    if not user_input:
        print("You entered an empty string. Try again with some text!")
        return

    if is_palindrome(user_input):
        print(f"✅ '{user_input}' is a palindrome!")
    else:
        print(f"❌ '{user_input}' is not a palindrome.")


# Example test
if __name__ == "__main__":
    run_palindrome_checker()
