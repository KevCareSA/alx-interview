#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for index, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                index == 0 or (len(grid[index - 1]) > j and grid[index - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                index == n - 1 or (len(grid[index + 1]) > j and grid[index + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
