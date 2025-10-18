# Challenge #7 - Beginner
# Track final floor from a sequence of up/down instructions
# Objective: Practice counters, conditional logic, and loop iteration

"""
Calculate the final floor based on 'U' (up) and 'D' (down) moves.
This exercise helps understand cumulative counting and condition-based state tracking.
Useful for problems involving elevation or position changes.
"""

def track_final_floor(moves: str) -> int:
    """ Return the final floor after processing all moves. """
    current_floor = 0  # Start from ground floor

    for move in moves:
        if move == "U":
            current_floor += 1  # Move up one floor
        elif move == "D":
            current_floor -= 1  # Move down one floor

    return current_floor


# Example tests
print(track_final_floor("UUDU"))   # Expected output: 3
print(track_final_floor("DDDD"))   # Expected output: -4
