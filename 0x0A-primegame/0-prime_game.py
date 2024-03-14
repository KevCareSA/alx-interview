#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """Determines winner of the prime number game"""
    if x < 1 or not nums:
        return None

    n_max = max(nums)
    primes = [True] * (n_max + 1)
    primes[0], primes[1] = False, False

    for i in range(2, int(n_max**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n_max + 1, i):
                primes[j] = False

    maria_win, ben_win = 0, 0
    for n in nums:
        primes_count = sum(primes[:n+1])
        ben_win += primes_count % 2 == 0
        maria_win += primes_count % 2 == 1

    if maria_win == ben_win:
        return None
    return 'Maria' if maria_win > ben_win else 'Ben'
