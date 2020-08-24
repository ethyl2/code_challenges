"""
https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

Given 2 arrays, return an array in which all of the instances of values present in the 2nd list are removed from the first list.

Examples:
array_diff([1,2],[1]) == [2]
array_diff([1,2,2,2,3],[2]) == [1,3]
array_diff([], [1,2]) -> []
"""
from typing import List


def array_diff(a: List[int], b: List[int]):
    set_a = set(a)
    set_b = set(b)
    set_a.symmetric_difference_update(set_b)
    return list(filter(lambda x: x in set_a, a))


print(array_diff([1, 2], [1]))
print(array_diff([1, 2, 2, 2, 3], [2]))
print(array_diff([], [1, 2]))
print(array_diff([1, 2, 2], [1]))
print(array_diff([1, 2, 2], [0]))
