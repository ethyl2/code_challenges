"""
https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python

Given a string of digits, return a string where any digit below 5 is '0' and others are '1'
"""
import string

# My solution


def fake_bin(x):
    return ''.join(['0' if int(num) < 5 else '1' for num in x])

# Another person's solution:


def fake_bin2(x):
    return x.translate(string.maketrans('0123456789', '0000011111'))


print(fake_bin("45385593107843568"))  # "01011110001100111"
print(fake_bin2("45385593107843568"))  # "01011110001100111"
