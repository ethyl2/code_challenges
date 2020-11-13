"""
https://www.codewars.com/kata/57f781872e3d8ca2a000007e/train/python

Given a list, return a list in which each of the values of the input list is doubled.
Use map()
"""


def maps(a):
    return list(map(lambda x: x*2, a))


print(maps([1, 2, 3]))
