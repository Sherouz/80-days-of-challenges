# Challenge #25 - Beginner
# Coin flip guessing game
# Objective: Practice user input, random module, and conditional logic for basic interactivity

"""
A simple coin-flip guessing game.
Demonstrates user input handling, random choice generation, and conditional logic.
Encourages interactive coding and introduces randomness in Python.
"""

import random

def coin_flip_game() -> None:
    """
    Simulate a coin flip and let the user guess the result.
    """
    print("\n🎯 Welcome to the Coin Flip Guessing Game!\n")

    # 1. Define possible outcomes and let the computer randomly choose one
    options = ["Heads", "Tails"]
    computer_choice = random.choice(options)

    # 2. Get the user's guess and normalize input
    user_input = input("What's your guess? (Heads / Tails): ").strip().lower()

    # 3. Normalize user input for easier comparison
    if user_input.startswith('h'):
        user_guess = "Heads"
    elif user_input.startswith('t'):
        user_guess = "Tails"
    else:
        print("⚠️ Invalid input. Please enter 'Heads' or 'Tails'.")
        return  # End the game if input is invalid

    # 4. Reveal the result
    print("\n The coin is flipping...")
    print(f"Result: {computer_choice}!\n")

    # 5. Compare guesses and announce the result
    if user_guess == computer_choice:
        print("🎉 Congratulations! You guessed correctly!")
    else:
        print("😔 Sorry, better luck next time!")


# Example play
if __name__ == "__main__":
    coin_flip_game()
