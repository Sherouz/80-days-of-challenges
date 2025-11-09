# Challenge #29 - Beginner/Intermediate
# Strong Random Password Generator
# Objective: Build a password generator that ensures a mix of characters.

"""
Generates a strong random password containing at least one uppercase letter,
one digit, and one special symbol. Handles lengths outside allowed range
automatically and demonstrates use of loops, random choice, and shuffling.
"""

import random, string

def generate_strong_password(length=12):
    """Generate a random strong password with letters, digits, and symbols."""
    
    # Automatically adjust length if it's outside the allowed range
    if length < 8:
        print("⚠️  Password length is less than minimum 8. Automatically set to 8.")
        length = 8
    elif length > 25:
        print("⚠️  Password length exceeds maximum 25. Automatically set to 25.")
        length = 25

    # Character pools
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{};:,.<>?"

    # Ensure at least one uppercase, one digit, and one symbol
    base = [
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()")
    ]

    # Fill the remaining length randomly
    base += random.choices(chars, k=length - 3)

    # Shuffle to avoid predictable patterns
    random.shuffle(base)

    # Convert list of characters to string
    return "".join(base)


# Example usage:
print(f"\n🔐 Generated password: {generate_strong_password(16)}\n")
print(f"🔐 Generated password: {generate_strong_password(30)}\n")
print(f"🔐 Generated password: {generate_strong_password(6)}\n")
