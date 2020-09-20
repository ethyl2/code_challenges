"""
https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
Given int, return array of digits reversed.
"""


def digitize(n):
    return list(reversed([int(digit) for digit in str(n)]))
