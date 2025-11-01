# Challenge #21 - Beginner/Intermediate
# Turn-based FizzBuzz: Player vs Machine
# Objective: Practice while loops, string comparison, and alternating turns

"""
Turn-based FizzBuzz game between the player and the computer.
Each turn, they count upward starting from 1.
Player must correctly say the next FizzBuzz value ("Fizz", "Buzz", "FizzBuzz", or number).
You can also use shortcuts like 'F', 'B', or 'FB'. Game ends if the player is wrong or quits.
"""

def fizzbuzz_label(n: int) -> list[str]:
    """Return acceptable answers for the given number."""
    if n % 3 == 0 and n % 5 == 0:
        return ["FizzBuzz", "FB", "fizzbuzz", "fb"]
    elif n % 3 == 0:
        return ["Fizz", "F", "fizz", "f"]
    elif n % 5 == 0:
        return ["Buzz", "B", "buzz", "b"]
    else:
        return [str(n)]

def print_separator():
    print("\n" + "―" * 45 + "\n")

def play_fizzbuzz_game():
    print("\n" + "="*25 + "  🎯  WELCOME TO TURN-BASED FIZZBUZZ  🎯  " + 25*"="  + "\n")

    print("🧠  RULES:")
    print(" • You and the machine take turns counting upward.")
    print(" • Say 'Fizz' for multiples of 3, 'Buzz' for multiples of 5, 'FizzBuzz' for both.")
    print(" • You can also type short versions: 'F', 'B', or 'FB'.")
    print(" • Type 'q' to quit anytime.\n")

    print("🚀  LET’S BEGIN!\n")
    print_separator()

    current_number = 1
    player_turn = True

    while True:
        expected = fizzbuzz_label(current_number)

        if player_turn:
            print(f"🧍  Your turn → Number: {current_number}")
            user_input = input("👉  Your answer: ").strip().lower()

            if user_input in ("q", "quit"):
                print("\n👋 You quit the game. Thanks for playing!")
                break

            if user_input not in [ans.lower() for ans in expected]:
                print(f"\n❌  Oops! Expected one of {expected}, but you said '{user_input}'.")
                print("💻  Machine wins this round! 💀")
                break
            else:
                print("✅  Nice! That’s correct! 💪")
        else:
            print(f"🤖  Machine’s turn → Number: {current_number}")
            print(f"💬  Machine says: {expected[0]}")

        player_turn = not player_turn
        current_number += 1
        print_separator()

    print(f"🏁  FINAL NUMBER REACHED: {current_number - 1}")
    print("🎮  GAME OVER — THANKS FOR PLAYING! ✨\n")


# Example run
if __name__ == "__main__":
    play_fizzbuzz_game()
