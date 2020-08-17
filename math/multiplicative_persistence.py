"""
https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

Given a positive int, return its multiplicative persistence,
which is the number of times you must multiply its digits until you reacha single digit.

Examples:
39 -> 3 b/c 3*9 = 27, 2*7=14, 1*4=4
4 -> 0 b/c 4 is already a one-digit number
"""
import functools


def persistence(n):
    count = 0
    if n < 10:
        return count
    while n >= 10:
        n = functools.reduce(
            lambda a, b: a*b, [int(digit) for digit in [char for char in str(n)]])
        count += 1
    return count


print(persistence(39))
print(persistence(4))
print(persistence(999))
