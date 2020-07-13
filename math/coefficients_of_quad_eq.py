"""
https://www.codewars.com/kata/5d59576768ba810001f1f8d6/train/python

Given 2 roots, find a, b, c where ax^2 + bx + c = 0,
Given a = 1

Examples 
quadratic(1,2) = (1, -3, 2)
quadratic(0,1) = (1, -1, 0)

Given tip:
roots can be written as (x - x1) * (x - x2) = 0
"""


def quadratic(x1, x2):
    # b = (x1 + x2) * -1
    # c = x1 * x2
    # answer = (1, b, c)
    # return answer
    # return (1, b, c)
    return (1, (x1 + x2) * -1, x1 * x2)


print(quadratic(1, 2))
print(quadratic(0, 1))
