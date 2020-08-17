"""
https://www.codewars.com/kata/5526fc09a1bbd946250002dc

Given an array of ints, with length >= 3,
Return the 'outlier' int, which is the only odd number if the rest are even, and the only even number if the rest are odd.

Examples:
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""
from typing import List


def find_outlier(integers: List) -> int:
    num_first_three_even = 0
    for i in range(3):
        if integers[i] % 2 == 0:
            num_first_three_even += 1
    isEven = num_first_three_even >= 2

    for num in integers:
        if isEven:
            if num % 2 == 1:
                return num
        if not isEven:
            if num % 2 == 0:
                return num


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
