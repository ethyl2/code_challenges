"""
https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python

Given an array of 1s and 0s, return the equivalent binary value to an integer.

binary_array_to_number([0,0,0,1]), 1
binary_array_to_number([0,0,1,0]), 2
binary_array_to_number([1,1,1,1]), 15
binary_array_to_number([0,1,1,0]), 6
"""
from typing import List


def binary_array_to_number(arr: List[int]):
    return int('0b' + ''.join([str(num) for num in arr]), 2)


print(binary_array_to_number([1, 1, 1, 1]))
