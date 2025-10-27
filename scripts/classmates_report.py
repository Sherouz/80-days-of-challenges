# Challenge #16 - Intermediate
# Find and display classmates with shared classes
# Objective: Practice nested loops, set operations, and formatted terminal output

"""
Generate a clean, colorized report showing which students share classes.
Uses set intersections to find shared courses and ANSI codes for colorful output.
Demonstrates nested loop logic and string formatting for readability.
"""

# ANSI color codes for colorful terminal output
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Dictionary mapping each student to the set of classes they are enrolled in
students_classes = {
    "Alice": {"Painting", "Pottery"},
    "Sarah": {"Painting", "Pottery"},
    "John": {"Pottery", "Programming"},
    "Emily": {"Programming"},
    "David": {"Chess", "Programming"},
    "James": {"Painting"},
    "Olivia": {"Painting", "Chess"},
}


def find_classmates(data):
    """
    Print a clean, colorized, grouped list of classmates for each student.
    """
    # Header for the classmates report
    print(f"\n{CYAN}{'='*25} 🎓 Classmates Report {'='*25}{RESET}")

    # Outer loop: iterate through each student
    for student_1, classes_1 in data.items():
        classmates = []

        # Inner loop: compare current student with every other student
        for student_2, classes_2 in data.items():
            if student_1 != student_2:
                # Find shared classes using set intersection
                shared = classes_1 & classes_2
                if shared:
                    # Format and add the result to the list
                    classmates.append(f"{GREEN}•{RESET} {student_2:<8} → {', '.join(sorted(shared))}")

        # Print the classmates for the current student (if any)
        if classmates:
            print(f"\n{YELLOW}{student_1}{RESET} shares classes with:")
            print("\n".join(classmates))
            print(f"{'-'*55}")

    # Footer line
    print(f"\n{CYAN}{'='*70}{RESET}\n")


# Example test run
if __name__ == "__main__":
    find_classmates(students_classes)
