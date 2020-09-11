"""
https://www.codewars.com/kata/56606694ec01347ce800001b/train/python

Given 3 ints, return whether a triangle can be built with the sides of those lengths.

"Determining if three side lengths can make a triangle: 
All you have to do is use the Triangle Inequality Theorem, 
which states that the sum of two side lengths of a triangle is always greater than the third side. 
If this is true for all three combinations of added side lengths, then you will have a triangle."
"""


def is_triangle(a, b, c):
    return a < (b+c) and b < (a+c) and c < (a+b)


print(is_triangle(1, 2, 2))  # True
print(is_triangle(7, 2, 2))  # False
