"""
https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python
Given a string, return its reverse
"""


def solution(string):
    return ''.join(reversed([char for char in string]))


def solution2(string):
    return string[::-1]


print(solution2('world'))
