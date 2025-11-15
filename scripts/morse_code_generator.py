# Challenge #35 - Intermediate
# Simple Morse Code Generator (Full A-Z)
# Objective: Practice dictionaries, mapping full alphabet, user input, and interactive processing

"""
Convert English text into Morse code using a complete A-Z mapping.
Demonstrates dictionary-based lookup and clean handling of unknown characters.
Produces single-space separation for letters and double-space separation for words.
Supports repeated user input through an interactive command loop.
Ignores unsupported characters or replaces them with a defined placeholder.
"""

from typing import Dict

# International Morse code mapping A-Z
MORSE_MAPPING: Dict[str, str] = {
    "A": ".-",    "B": "-...",  "C": "-.-.", "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",  "H": "....",
    "I": "..",    "J": ".---", "K": "-.-",  "L": ".-..",
    "M": "--",    "N": "-.",   "O": "---",  "P": ".--.",
    "Q": "--.-",  "R": ".-.",  "S": "...",  "T": "-",
    "U": "..-",   "V": "...-", "W": ".--",  "X": "-..-",
    "Y": "-.--",  "Z": "--.."
}

def generate_simple_morse(text: str, unknown_placeholder: str = "?") -> str:
    """
    Translate a text string into Morse code using A-Z dictionary mapping.
    Converts characters to uppercase before processing for consistent lookup.
    Replaces unsupported characters with a configurable placeholder symbol.
    Splits the input into words, then encodes each letter individually.
    Joins encoded letters with single spaces and words with double spaces.
    """
    # Convert to uppercase to match mapping keys
    text = text.upper()
    words = text.split()  # split into words by whitespace
    morse_words = []

    for word in words:
        morse_letters = []
        for ch in word:
            morse_letters.append(MORSE_MAPPING.get(ch, unknown_placeholder))
        # join letters with single space
        morse_words.append(" ".join(morse_letters))

    # join words with two spaces
    return "  ".join(morse_words)


if __name__ == "__main__":
    print("\n📡 Simple Morse Code Generator (A-Z) 🚀\n")
    while True:
        user_input = input("Enter a sentence (or type 'q' to quit): ").strip()
        if user_input.lower() == "q":
            print("\n👋 Goodbye!\n")
            break
        morse = generate_simple_morse(user_input)
        print(f"\nMorse Code: {morse}\n")
