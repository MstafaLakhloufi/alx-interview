#!/usr/bin/python3
"""
Prima Game
"""


def primeNumbers(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    prime_numbers = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            prime_numbers.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return prime_numbers


def isWinner(x, nums):
    """x - rounds
    nums - numbers list
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    maria_wins = 0
    ben_wins = 0
    for i in range(x):
        prime_numbers = primeNumbers(nums[i])
        if len(prime_numbers) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None
