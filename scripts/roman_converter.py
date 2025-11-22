# Challenge #42 - Intermediate
# Roman ↔ Integer Converter
# Objective: Practice dictionary mapping, loops, string manipulation, and number conversion.

"""
Convert numbers between Roman numerals and integers.
Supports both directions: Roman -> Integer and Integer -> Roman.
Handles numbers from 1 to 3999.
"""

def roman_to_int(s: str) -> int:
    """
    Convert a Roman numeral string to an integer.
    Reads the string from right to left and applies subtraction rules.
    """
    roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    total = 0
    prev = 0
    
    for char in reversed(s):      # Read from last character to first
        value = roman[char]
        if value < prev:           # Subtract if smaller than previous
            total -= value
        else:                      # Otherwise add
            total += value
        prev = value
    
    return total


def int_to_roman(num: int) -> str:
    """
    Convert an integer (1–3999) to a Roman numeral string.
    Iteratively subtracts values and appends symbols.
    """
    vals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
        (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"), (1, "I")
    ]
    result = ""
    for value, symbol in vals:
        while num >= value:
            result += symbol
            num -= value
    return result


# Main program
print("\n=== Roman <-> Integer Converter ===")
choice = input("1: Roman -> Integer\n2: Integer -> Roman\nChoose (1 or 2): ")

if choice == "1":
    roman = input("Enter a Roman numeral (e.g., MCMXCIV): ").strip().upper()
    try:
        print(f"Result: {roman_to_int(roman)}")
    except KeyError:
        print("Invalid Roman numeral!")
    
elif choice == "2":
    num = int(input("Enter an integer (1–3999): "))
    if 1 <= num <= 3999:
        print(f"Roman numeral: {int_to_roman(num)}")
    else:
        print("Number must be between 1 and 3999!")
else:
    print("Invalid choice!")
