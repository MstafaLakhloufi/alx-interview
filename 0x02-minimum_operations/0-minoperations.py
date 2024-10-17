#!/usr/bin/python3

'''Minimum Operations python3 challenge'''


def minOperations(n):
    '''calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Returns:
        Integer : if n is impossible to achieve, return 0
    '''

    current = 1
    initial = 0
    count = 0
    while current < n:
        remainder = n - current
        if (remainder % current == 0):
            initial = current
            current += initial
            count += 2
        else:
            current += initial
            count += 1
    return count
