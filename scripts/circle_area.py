# Challenge #10 - Beginner
# Calculate the area of a circle
# Objective: Practice math operations, user input validation, and functions

"""
Program to calculate the area of a circle.
Prompts user for radius, validates input, and returns the area.
Helps practice math module usage, input handling, and function design.
"""

import math


def calculate_circle_area(radius):
    """
    Calculate and return the area of a circle given its radius.
    Formula: area = π * r^2
    """
    return math.pi * radius ** 2


def run_circle_calculator():
    """
    Handle user input, validation, and output for circle area calculation.
    Demonstrates structured program flow and function encapsulation.
    """
    while True:
        try:
            # Ask the user to enter the circle radius
            radius = float(input("Enter the radius of the circle: "))

            # Ensure the radius is a positive number
            if radius <= 0:
                print("Radius must be a positive number. Try again.")
            else:
                break

        except ValueError:
            # Handle the case where the user enters a non-numeric value
            print("Invalid input. Please enter a number.")

    # --- Calculate and display result ---
    area = calculate_circle_area(radius)  # Call the function to compute the area
    print(f"The area of the circle is: {area:.2f}")  # Display result with 2 decimal places


# --- Program entry point ---
if __name__ == "__main__":
    run_circle_calculator()
