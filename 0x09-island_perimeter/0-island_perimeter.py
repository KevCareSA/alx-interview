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
    for idx, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                idx == 0 or grid[idx - 1][j] == 0,
                j == m - 1 or row[j + 1] == 0,
                idx == n - 1 or grid[idx + 1][j] == 0,
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
