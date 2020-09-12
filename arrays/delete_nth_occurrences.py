"""
https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python

Given a list and and int N, create a new list that contains each number of list at most N times without reordering.

Examples:
delete_nth ([1,1,1,1],2) # return [1,1]

delete_nth ([20,37,20,21],1) # return [20,37,21]
"""
from typing import List


def delete_nth(order: List[int], max_e: int) -> List[int]:
    """
    O(n) time
    O(n) space
    """
    lookup = dict()
    output = []
    for num in order:
        if num not in lookup:
            output.append(num)
            lookup[num] = 1
        elif lookup[num] < max_e:
            output.append(num)
            lookup[num] += 1
    return output


def delete_nth2(order, max_e):
    """
    O(n) time -- but less efficient than above b/c of multiple calls to .count()
    O(1) space though
    """
    output = []
    for num in order:
        if output.count(num) < max_e:
            output.append(num)
    return output


print(delete_nth2([1, 1, 1, 1], 2))
print(delete_nth2([20, 37, 20, 21], 1))
