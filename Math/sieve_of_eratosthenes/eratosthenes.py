"""
Generate prime numbers up to limit using the sieve of Eratosthenes.
"""

import math

def primes(limit):
    numbers = list(range(limit))

    numbers[0] = 0
    numbers[1] = 0

    #For each number still in the list, eliminate all its multiples
    #We only need to check up to the square root of the biggest number
    for i in range(2, int(math.sqrt(limit)) + 1):
        if numbers[i] == 0:
            continue
        for j in range(i, limit, i):
            if j == i:
                continue
            numbers[j] = 0
    return list(filter(lambda x: x != 0, numbers))
