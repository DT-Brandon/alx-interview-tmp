#!/usr/bin/python3
"""
    provides a function that returns the minimum number of operations
    to reach a number of  n H
"""


def minOperations(n):
    """
    Calculate the minimum number of operations to reduce a number to 1.

    Args:
        n (int): The number to be reduced.

    Returns:
        int: The total number of operations.
    """

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operations
