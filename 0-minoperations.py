#!/usr/bin/python3
"""
This module defines minOperations, a function that calculates the
fewest number of Copy All and Paste operations needed to end up with
exactly n H characters in a text file.
"""


def minOperations(n):
    """Return the fewest operations needed to get exactly n H characters.

    The answer is the sum of the prime factors of n. Returns 0 if n is
    impossible to achieve (n less than 2).
    """
    if not isinstance(n, int) or n < 2:
        return 0
    operations = 0
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    if n > 1:
        operations += n
    return operations
EOF
