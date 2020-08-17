"""
https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

Given an int,
Return the sum off multiplying all of the ints below that int that are a multiple of 3 or 5.
Note: if a number is a multiple of both 3 and 5, only count it once.

Example: 10 -> 23 because 3+5+6+9
"""

# My first solution. A little faster than the second because only iterates once. O(n).
# O(1) space


def solution(number: int) -> int:
    output = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            output += i
    return output


print(solution(10))

# My second solution is similar to the first, except uses a list comprehension.
# O(n) time, but does 2 loops: once to create arr and then again to find its sum.
# O(1) space, technically, because I never assign the arr to a variable -- HOWEVER, it is made, so maybe it would be O(n) space?!


def solution2(number: int) -> int:
    return sum([i for i in range(1, number) if i % 3 == 0 or i % 5 == 0])


print(solution2(10))
