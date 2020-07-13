"""
https://www.codewars.com/kata/5545f109004975ea66000086/train/python
make a function that checks if number n is divisible by x and y. All inputs are positive, non-zero digits.

Examples:
n = 3, x = 1, y = 3 => true because 3 is divisible by 1 and 3
n = 12, x = 2, y = 6 => true because 12 is divisible by 2 and 6
n = 100, x = 5, y = 3 => false because 100 is not divisible by 3
n = 12, x = 7, y = 5 => false because 12 is neither divisible by 7 nor 5
"""


def is_divisible(n, x, y):
    return not n % x and not n % y


print(is_divisible(3, 1, 3))  # True
print(is_divisible(12, 2, 6))  # True
print(is_divisible(100, 5, 3))  # False
print(is_divisible(12, 7, 5))  # False
