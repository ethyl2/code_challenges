"""
https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python
Given an int, return the sum of every number from 1 to the given int.
The int will always be a positive integer greater than 0.

Examples:
summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
"""


def summation(num):
    return sum([n for n in range(1, num+1)])


def summation2(num):
    return sum(range(num + 1))


def summation3(num):
    return (1+num) * num // 2


print(summation3(2))
print(summation3(8))
