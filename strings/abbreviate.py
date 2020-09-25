"""
https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

Given a string of two names with a space in between, return a string in the format F.L.
"""


def abbrev_name(name):
    [first, last] = name.split(' ')
    return f"{first[0].upper()}.{last[0].upper()}"


print(abbrev_name("First Last"))
