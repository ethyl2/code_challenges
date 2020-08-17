"""
https://www.codewars.com/kata/541c8630095125aba6000c00

Given an int, return its 'digital root'

A digital root is the 'recursive sum of all the digits in a number'.
You calculate it by
    1. Adding the digits of the int.
    2. If the result has more than one digit,
        call the function again (until reach base case: when the result has one digit)
"""
from typing import List


def digital_root(n: int) -> int:
    if n-10 < 0:
        return n
    else:
        # calculate new sum of digits
        # call function on that sum
        return digital_root(sum([int(digit) for digit in [char for char in str(n)]]))


print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
