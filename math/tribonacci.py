"""
https://www.codewars.com/kata/556deca17c58da83c00002db/train/python

Given a signature list of 3 integers, and an integer n, return the first n elements of a fibonacci sequence in which
you sum the last 3 numbers (instead of 2) to get the next element.

[1,1,1], n=7 -> [1, 1 ,1, 3, 5, 9, 17]
[0,0,1], n=8 -> [0, 0, 1, 1, 2, 4, 7, 13]
"""

from typing import List, Dict


def tribonacci(signature: List[int], n: int) -> List[int]:
    output = []
    cache = {}
    for i in range(n):
        if i not in cache:
            cache[i] = calculate_tribonacci(signature, i, cache)
        output.append(cache[i])
    return output


def calculate_tribonacci(signature: List[int], n: int, cache: Dict) -> int:
    if n < 3:
        return signature[n]
    else:
        if n not in cache:
            cache[n] = calculate_tribonacci(signature, n-1, cache) + calculate_tribonacci(
                signature, n-2, cache) + calculate_tribonacci(signature, n-3, cache)
        return cache[n]


print(tribonacci([1, 1, 1], 7))

# Another person's concise version:


def tribonacci2(signature, n):
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    return res


print(tribonacci2([1, 1, 1], 7))
