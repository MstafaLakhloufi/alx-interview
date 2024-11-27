#!/usr/bin/python3
"""A function to determine the fewest number of coins needed
   to meet a given amount total."""

def makeChange(coins, total):
    """
    Calculate the minimum number of coins needed to achieve the total.

    Args:
        coins (list): Available coin denominations.
        total (int): Target total to achieve.

    Returns:
        int: Fewest number of coins needed, or -1 if not possible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  
    counter = 0

    for coin in coins:
        if total == 0:
            break
        count, total = divmod(total, coin)
        counter += count

    return counter if total == 0 else -1