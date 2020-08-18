"""
https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
Given an int,
return an new int that is has the square of each digit of input squared and then displayed together.

Example: 9119 -> 811181
"""


def square_digits(num):
    output = ''
    for char in str(num):
        output += str(int(char)**2)
    return int(output)

# My version with list comprehension


def square_digits2(num):
    return int(''.join([str(int(char)**2) for char in str(num)]))


print(square_digits2(9119))
