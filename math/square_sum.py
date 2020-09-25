"""
https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
Given a list of ints, return the sum of all of their squares.
"""
from typing import List


def square_sum(numbers: List) -> int:
    return sum([number**2 for number in numbers])


print(square_sum([1, 2, 2]))  # 9
