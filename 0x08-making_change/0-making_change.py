#!/usr/bin/python3
"""
Determine the fewest number of coins
needed to meet a given total.
"""
    

def makeChange(coins, total):
    """
    This function will take a list of coins and use
    that to calculate how much change the total will require
    
    Returns:
        int: Fewest number of coins needed to meet the total, or -1 if it cannot be met.
    """
    if total <= 0:
        return 0
    
    # Initialize an array to store the minimum coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  
    
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1

  
