"""
https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python
given 2 ints, return their sum in binary.
Conversion can be done before or after the addition.
The binary number returned should be a string.
"""


def add_binary(a: int, b: int) -> str:
    return str(bin(a+b))[2:]


def add_binary2(a: int, b: int) -> str:
    return '{0:b}'.format(a+b)


def add_binary3(a: int, b: int) -> str:
    return format(a+b, 'b')


print(add_binary3(1, 1))
