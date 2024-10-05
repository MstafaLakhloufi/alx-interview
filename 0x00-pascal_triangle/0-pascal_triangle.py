#!/usr/bin/python3
"""
Defines a function that returns a list of lists
of integers that represents the pascal's triangle.
"""

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle up to level n.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        row = [1]  # Every row starts with 1
        for j in range(1, i):
            # Sum of two elements from the previous row
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Every row ends with 1
        triangle.append(row)

    return triangle
