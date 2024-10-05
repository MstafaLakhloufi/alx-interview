#!/usr/bin/python3
"""
Pascal's Triangle Using Dynamic Programming
"""

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle up to level n.
    """
    if n <= 0:
        return []

    triangle = [[1] * (i + 1) for i in range(n)]

    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle
