# Challenge #17 - Beginner/Intermediate
# Convert numeric grade to letter grade (robust version)
# Objective: Practice Python 3.10+ match-case statement, conditional logic, and robust input handling

"""
Enhanced version of the grade converter:
- Accepts both integer and decimal grades (e.g., 89.5)
- Cleans user input and handles invalid or out-of-range values
- Uses match-case for clear conditional branching
- Loops until a valid numeric grade (0–100) is entered
"""

def convert_to_letter_grade(grade: float) -> str:
    """
    Convert numeric grade (0–100) to a letter grade (A–F).
    Returns a letter grade based on the numeric value.
    """
    match grade:
        case grade if 90 <= grade <= 100:
            return "A"
        case grade if 80 <= grade < 90:
            return "B"
        case grade if 70 <= grade < 80:
            return "C"
        case grade if 60 <= grade < 70:
            return "D"
        case grade if 0 <= grade < 60:
            return "F"
        case _:
            return None  # Signal invalid value


def get_valid_grade() -> float:
    """
    Prompt user for a numeric grade until a valid float between 0 and 100 is entered.
    Cleans input and provides user-friendly feedback.
    """
    while True:
        raw_input_value = input("Enter your grade (0–100): ").strip()
        
        # Try to convert input to float
        try:
            grade = float(raw_input_value)
        except ValueError:
            print("⚠️ That doesn't look like a number. Please enter a valid numeric grade.")
            continue

        # Check range
        if not (0 <= grade <= 100):
            print("🚫 Grade must be between 0 and 100. Try again.")
            continue

        # If we got here, the input is valid
        return grade


# Main program flow
if __name__ == "__main__":
    while True:
        grade_value = get_valid_grade()
        letter = convert_to_letter_grade(grade_value)
        print(f"✅ Your letter grade is {letter}")

        again = input("Would you like to enter another grade? (y/n): ").strip().lower()
        if again != "y":
            print("🎓 Thanks for using the grade converter! Goodbye.")
            break
