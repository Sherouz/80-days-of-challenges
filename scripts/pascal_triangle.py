# Challenge #9 - Beginner/Intermediate
# Pascal's Triangle (Khayyam–Pascal Triangle)
# Objective: Practice nested loops, list building, and combinatorial logic

"""
Generate and print Pascal's Triangle (Khayyam–Pascal Triangle).
Each row is a list of integers representing the coefficients.
Includes a function to get a specific value using combinatorics.
"""

from math import factorial

def generate_pascals_triangle(n: int) -> list[list[int]]:
    """
    Generate Pascal's Triangle with a specified number of rows.
    Each row is a list of integers representing the coefficients.
    Returns the complete triangle as a list of rows.
    """

    if n <= 0:
        return []

    triangle = [[1]]    # Initialize with the first row

    for i in range(1, n):
        row = [1]   # Every row starts with 1
        for j in range(1, i):
            # Each inner element is the sum of the two numbers directly above it
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)   # Every row ends with 1
        triangle.append(row)    # Add the completed row to the triangle

    return triangle


def print_pascals_triangle(triangle: list[list[int]]) -> None:
    """
    print_pascals_triangle displays Pascal's Triangle in a nicely formatted manner.
    Each row is centered based on the width of the last row to maintain triangle shape.
    """
    n = len(triangle)   # total number of rows in triangle
    width = len("   ".join(map(str, triangle[-1])))   # width based on last row
    for row in triangle:
        line = "   ".join(f"{num}" for num in row)    # join numbers with spaces
        print(line.center(width))   # center each row for alignment


def get_pascal_value(row: int, col: int) -> int:
    """
    Return the value at the given row and column in Pascal's Triangle
    without generating the full triangle.

    Uses the combination formula:
    C(n, k) = n! / (k! * (n - k)!)
    """
    # Validate that the column index is within the valid range
    if col < 0 or col > row:    # check valid column index
        raise ValueError("Column must be between 0 and row inclusive.")
    # Use the combination formula directly to compute the Pascal value
    return factorial(row) // (factorial(col) * factorial(row - col))


def main():
    """
    Run the Pascal's Triangle program.
    Handles user input, prints the triangle,
    and demonstrates fetching a specific value.
    """
    try:
        # Get user input with a hint
        n = int(input("Enter the number of rows (recommended: 1–20): ").strip())

        # Limit to prevent overflow or huge output
        if n > 25:
            print("\n⚠️  Too large! Printing triangles over 25 rows may overflow your screen or memory.")
            print("Try a smaller number (e.g. between 5 and 20).\n")
        elif n <= 0:
            print("Number of rows must be positive.")
        else:
            triangle = generate_pascals_triangle(n)
            print_pascals_triangle(triangle)

            # Optional demonstration: quick test for specific value
            print("\nExample:")
            r, c = 5, 2   #
            print(f"Value at row {r}, column {c}: {get_pascal_value(r, c)}")

    except ValueError:
        print("❌ Invalid input. Please enter a positive integer between 1 and 25.")


if __name__ == "__main__":
    main()
