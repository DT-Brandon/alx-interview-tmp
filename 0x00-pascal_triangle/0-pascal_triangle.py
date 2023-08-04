#!/usr/bin/python3
"""
Defines function that returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """Prints a pascal triangle"""
    arr = []

    if (n <= 0):
        return arr

    previous = [1]
    for row_index in range(n):
        rowlist = []
        if row_index == 0:
            rowlist = [1]
        else:
            for i in range(row_index + 1):
                if i == 0:
                    rowlist.append(0 + previous[i])
                elif i == (row_index):
                    rowlist.append(previous[i - 1] + 0)
                else:
                    rowlist.append(previous[i - 1] + previous[i])
        previous = rowlist
        arr.append(rowlist)

    return arr
