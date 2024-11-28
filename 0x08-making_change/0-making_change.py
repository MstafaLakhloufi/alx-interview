#!/usr/bin/python3
"""A function to determine the fewest number of coins needed
   to meet a given amount total"""


def makeChange(coins, total):
    """This function will take a list of coins and use
       that to calculate how much change the total will require
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