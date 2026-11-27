
#!/usr/bin/python3
"""
Calculate the amount of rainwater retained between walls.
"""

def rain(walls):
    if not walls:
        return 0

    total_water = 0

    for i in range(len(walls)):
        left_max = max(walls[:i + 1])
        right_max = max(walls[i:])

        water = min(left_max, right_max) - walls[i]

        if water > 0:
            total_water += water

    return total_water

