# Challenge #69 - Intermediate
# Conway's Game of Life
# Objective: Simulate one step of the Game of Life on a grid.

"""
Simulate a single iteration of Conway's Game of Life.
Demonstrates neighbor scanning and grid-based state transitions.
Useful for practicing matrix traversal and simulation logic.
"""

def game_of_life_step(grid: list[list[int]]) -> list[list[int]]:
    """Return the next state of the grid after one simulation step."""
    rows = len(grid)
    cols = len(grid[0])

    next_grid = [[0] * cols for _ in range(rows)]   # new grid for next state

    for r in range(rows):
        for c in range(cols):
            live_neighbors = 0

            # check all 8 neighboring cells
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue                    # skip the cell itself

                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        live_neighbors += grid[nr][nc]

            # apply Conway's rules
            if grid[r][c] == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    next_grid[r][c] = 1             # cell survives
                else:
                    next_grid[r][c] = 0             # cell dies
            else:
                if live_neighbors == 3:
                    next_grid[r][c] = 1             # cell becomes alive

    return next_grid


if __name__ == "__main__":
    # initial grid (0 = dead, 1 = alive)
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ]

    print("Initial grid:")
    for row in grid:
        print(row)

    next_state = game_of_life_step(grid)

    print("\nNext generation:")
    for row in next_state:
        print(row)
