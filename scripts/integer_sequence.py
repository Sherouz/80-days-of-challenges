# Challenge #36 - Intermediate
# Integer Sequence Generator (Optimized + Interactive + Grouped Output)
# Objective: Efficient string building, user input handling, and readable grouped formatting.

"""
Interactive version of the Integer Sequence generator.
User enters a positive integer n.
Program prints the concatenated integer sequence from 1 to n,
formatted with 3-digit grouping for readability.
"""

def integer_sequence(n: int) -> str:
    """
    Efficiently build a concatenated string of integers from 1 to n.
    Uses list accumulation + join to avoid O(n^2) string concatenation.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")

    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    numbers = [str(i) for i in range(1, n + 1)]
    return "".join(numbers)


def group_by_three(s: str) -> str:
    """
    Group the output string into chunks of 3 characters.
    Example: '1234567' -> '123,456,7'
    """
    return ",".join(s[i:i+3] for i in range(0, len(s), 3))


# ----- Example test -----
if __name__ == "__main__":
    print("\n🔢 Integer Sequence Generator")
    print("Enter a positive integer, and I'll generate the full sequence from 1 to n.\n")

    try:
        user_input = input("➡️  Enter a positive integer: ").strip()

        if not user_input.isdigit():
            raise ValueError("Input must be a positive integer (digits only).")

        n = int(user_input)

        result = integer_sequence(n)
        grouped = group_by_three(result)

        print("\n✨ Result (Grouped for readability):")
        print(grouped)
        print("\n✔️  Done \n")

    except Exception as e:
        print(f"\n❌ Error: {e}")
