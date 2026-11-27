#!/usr/bin/python3
"""Calculates how much rainwater is retained between walls."""


def rain(walls):
    """Return the total units of rainwater retained between walls.

    Uses two pointers moving inward. The water above any position is
    limited by the shorter of the tallest walls to its left and right,
    so the side with the smaller running maximum can always be settled.
    Runs in O(n) time with O(1) extra space.

    Args:
        walls (list): non-negative integers giving wall heights.

    Returns:
        int: total amount of rainwater retained.
    """
    if not walls:
        return 0

    left, right = 0, len(walls) - 1
    left_max = right_max = 0
    water = 0

    while left < right:
        if walls[left] < walls[right]:
            if walls[left] >= left_max:
                left_max = walls[left]
            else:
                water += left_max - walls[left]
            left += 1
        else:
            if walls[right] >= right_max:
                right_max = walls[right]
            else:
                water += right_max - walls[right]
            right -= 1

    return water
