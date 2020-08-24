"""
https://www.codewars.com/kata/525f50e3b73515a6db000b83

Given an array of 10 ints, return a string with format of a phone num.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
"""


def create_phone_number(n):
    # return "({0}{1}{2}) {3}{4}{5}-{6}{7}{8}{9}".format(*n)
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
