# Challenge #15 - Beginner/Intermediate
# Calculate average expenses for each semester
# Objective: Practice for loops, enumerate(), tuple unpacking, and basic arithmetic

"""
Calculate average spending for each semester (Jan–Jun and Jul–Dec)
from a list of monthly expenses. Demonstrates function design,
tuple unpacking, loops, and basic arithmetic with formatted output.
"""

monthly_spending = [2950.75, 3120.40, 2805.60, 2650.10, 3302.45, 3415.20,
                    2100.35, 2758.90, 3620.50, 3389.80, 2895.25, 4010.65]


def calculate_semester_averages(expenses):
    """
    Calculate and return average spending for each semester.
    Uses a for loop and enumerate() to separate months Jan–Jun and Jul–Dec.
    Returns a tuple: (first_semester_avg, second_semester_avg)
    """
    first_semester_total = 0
    second_semester_total = 0

    # Use enumerate() to get both month index and expense value
    for index, expense in enumerate(expenses):
        if index < 6:   # First six months (Jan–Jun) belong to the first semester
            first_semester_total += expense  # Sum expenses for Jan–Jun
        else:
            second_semester_total += expense  # Sum expenses for Jul–Dec

    first_avg = first_semester_total / 6
    second_avg = second_semester_total / 6
    return first_avg, second_avg  # Return averages as a tuple


# Example usage
first_avg, second_avg = calculate_semester_averages(monthly_spending)

print(f"\nAverage expenses for the first semester:  ${first_avg:.2f}")
print(f"Average expenses for the second semester: ${second_avg:.2f}\n")
