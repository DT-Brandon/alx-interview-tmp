#!/usr/bin/python3

"""
Module/Function Documentation:

island_perimeter(grid):
    Calculates the perimeter of an island in a grid.

    Args:
        grid: A list of lists representing the grid.

    Returns:
        The perimeter of the island.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.

    Args:
        grid: A list of lists representing the grid.

    Returns:
        The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell contributes 4 to the perimeter

                # Check if adjacent cells are also land
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 for each shared side
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 for each shared side

    return perimeter
