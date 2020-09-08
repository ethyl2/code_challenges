"""
https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python

Given a string, remove all spaces from that string, and return it.
"""
import re


def no_space(x):
    x = re.sub(r'[\s]', '', x)
    return x


def no_space2(x):
    x = x.replace(' ', '')
    return x


print(no_space2('8 j 8   mBliB8g  imjB8B8  jl  B') == '8j8mBliB8gimjB8B8jlB')
