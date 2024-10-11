#!/usr/bin/python3
"""
A function that returns the perimeter on an island
"""


def island_perimeter(grid):
    """
    Initialize the perimeter on an island with 0
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    """
    Iterate through each cell in the grid, checking if it's an island
    """
    for row in range(rows):
        for col in range(cols):

            if grid[row][col] == 1:
                perimeter += 4

                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 2
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 2
    return perimeter
