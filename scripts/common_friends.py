# Challenge #13 - Beginner/Intermediate
# Find common friends between two lists efficiently
# Objective: Practice sets, intersection, sorting, and flexible data handling

"""
Identify common friends between two or more lists using set operations.
Demonstrates efficient membership checking and intersection of sets.
Prints the result in sorted order or informs if there are no common friends.
"""

def find_the_common_friends():
    """
    Find shared friends between two predefined lists using sets.
    Uses intersection to quickly identify common elements.
    Prints the result sorted alphabetically, handling empty intersections.
    """
    paul_friends = ["Mary", "Sara", "Tim", "Mike", "Henry"]
    tina_friends = ["Tim", "Susan", "Mary", "Josh", "Sara"]

    # Convert lists to sets for faster intersection
    common_friends = set(paul_friends) & set(tina_friends)

    if common_friends:
        print(f"\nCommon friends: {', '.join(sorted(common_friends))}")
    else:
        print("\nNo common friends found.")


# Example test
if __name__ == "__main__":
    find_the_common_friends()
