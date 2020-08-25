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


def find_outlier2(integers: List[int]) -> int:
    odds = [num for num in integers if num % 2 == 1]
    evens = [num for num in integers if num % 2 == 0]
    return odds[0] if len(odds) == 1 else evens[0]


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))

print(find_outlier2([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier2([160, 3, 1719, 19, 11, 13, -21]))


'''
https://www.codewars.com/kata/552c028c030765286c00007d/train/python
This problem is very similar to above, except that it returns the index + 1, instead of the value.
Also, the input is a string, not an array

Example: iq_test("2 4 7 8 10") -> 3
'''


def iq_test(numbers: str) -> int:
    numbers_list = numbers.split()
    num_first_three_even = 0
    for i in range(3):
        if int(numbers_list[i]) % 2 == 0:
            num_first_three_even += 1
    isEven = num_first_three_even >= 2

    for i, num in enumerate(numbers_list):
        if isEven:
            if int(num) % 2 == 1:
                return i+1
        if not isEven:
            if int(num) % 2 == 0:
                return i+1


print(iq_test("2 4 7 8 10"))
