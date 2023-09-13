#!/usr/bin/python3

"""
This module contains a function to rotate a 2D matrix.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a given 2D matrix.
    
    Args:
        matrix (list): The 2D matrix to rotate.
    
    Returns:
        None. The matrix is rotated in-place.
    """
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row of the transposed matrix
    for i in range(n):
        matrix[i] = matrix[i][::-1]
