#!/usr/bin/python3

'''
 Rotate 2D Matrix
'''
def rotate_2d_matrix(matrix) :
    '''
    rotates a 2d matrix 90° clockwise
    Returns: Nothing
    '''
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
