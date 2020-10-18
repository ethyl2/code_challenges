"""
https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python
Given 2 ints and an operator, return the result 
"""
def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))