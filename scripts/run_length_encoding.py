# Challenge #58 - Intermediate
# Run-Length Encoding (RLE)
# Objective: Compress a string by counting consecutive character occurrences.

"""
Encode a string using Run-Length Encoding (RLE).
Converts sequences of repeated characters into a compact 'char + count' form.
Useful for demonstrating pattern scanning and basic compression logic.
"""

def rle_encode(text: str) -> str:
    """
    Return the RLE-encoded form of the input string.
    Example: "AAABBC" -> "A3B2C1"
    """
    if not text:
        return ""

    result = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(f"{text[i - 1]}{count}")
            count = 1

    # Handle the final run
    result.append(f"{text[-1]}{count}")

    return "".join(result)


def main():
    user_input = input("Enter a string to encode: ").strip()

    if user_input == "":
        print("No input provided. Exiting.")
        return

    encoded = rle_encode(user_input)
    print(f"Encoded (RLE): {encoded}")


if __name__ == "__main__":
    main()
