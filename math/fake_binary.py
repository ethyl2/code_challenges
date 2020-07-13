"""
https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python

Given a string of digits, return a string where any digit below 5 is '0' and others are '1'
"""
import string

# My solution


def fake_bin(x):
    return ''.join(['0' if int(num) < 5 else '1' for num in x])


print(fake_bin("45385593107843568"))  # "01011110001100111"
