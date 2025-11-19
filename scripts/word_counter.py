# Challenge #39 - Beginner
# Word Counter
# Objective: Count the number of words in a given string

"""
This simple challenge takes a text input and counts the words.
It helps practice string manipulation, whitespace handling, and basic list operations.
"""

def word_counter(text: str) -> int:
    """
    Count the number of words in the given text.
    """
    # Remove leading and trailing whitespaces
    clean_text = text.strip()
    
    # Split the text by spaces (handles multiple spaces between words)
    words = clean_text.split()
    
    # Return the number of words
    return len(words)


# Optional extensions: count characters without spaces and sentences
def word_counter_extended(text: str) -> tuple:
    """
    Count words, characters (without spaces), and sentences in the text.
    Returns a tuple: (words_count, chars_count, sentences_count)
    """
    clean_text = text.strip()
    words = clean_text.split()
    words_count = len(words)
    
    # Count characters excluding spaces
    chars_count = len(clean_text.replace(" ", ""))
    
    # Count sentences by looking for ., !, ?
    sentences_count = sum(clean_text.count(p) for p in ".!?")
    
    return words_count, chars_count, sentences_count


# Example usage
if __name__ == "__main__":
    sample_text = "  Python   is    awesome!  "
    print(sample_text)
    print("Words:", word_counter(sample_text))
    print("Extended:", word_counter_extended(sample_text))
