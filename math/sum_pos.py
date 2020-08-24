"""
https://www.codewars.com/kata/5715eaedb436cf5606000381

Given an array of nums, return sum of pos nums. Return 0 if no pos nums.
"""
from typing import List


def positive_sum(arr: List[int]) -> int:
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return total


def positive_sum2(arr: List[int]) -> int:
    return sum([num for num in arr if num > 0])


print(positive_sum([1, -4, 7, 12]))
print(positive_sum([]), 0)
print(positive_sum([-1, 2, 3, 4, -5]))  # 9

print(positive_sum2([1, -4, 7, 12]))
print(positive_sum2([]), 0)
print(positive_sum2([-1, 2, 3, 4, -5]))  # 9
