"""
https://www.codewars.com/kata/550498447451fbbd7600041c/train/python

Given two lists of ints,
Return whether all elements in list b are squares of elements in list a.
"""
from typing import List


def comp(array1: List[int], array2: List[int]) -> bool:
    if not array1 or not array2:
        return False
    set1 = set([num*num for num in array1])
    # set2 = set(array2)
    # return set1.issubset(set2)
    for num in array2:
        if num not in set1:
            return False
    return True


def comp2(array1, array2):
    """
    This version is slightly more space efficient, because it only makes 1 set.
    """
    if not array2:
        return False
    set1 = set([num*num for num in array1])
    for num in array2:
        if num not in set1:
            return False
    return True


def comp3(array1, array2):
    """
    Another experiment
    """
    visited = set()
    if not array2 or not array1:
        return False
    set1 = set([num*num for num in array1])
    for num in array2:
        if num not in set1:
            return False
        visited.add(num)
    return len(visited) == len(set1)


def comp4(array1, array2):
    """
    Another experiment
    """
    if not array2 or not array1:
        return False

    array1.sort()
    array2.sort()
    array1 = [num**2 for num in array1]

    for i, num in enumerate(array1):
        if num != array2[i]:
            return False
    return True


a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

print(comp4(a, b))

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
b1 = [132, 14641, 20736, 361, 25921, 361, 20736, 361]

print(comp4(a1, b1))
