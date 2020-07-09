"""
https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python

A Narcissistic Number is a number which is the sum of its own digits, 
each raised to the power of the number of digits in a given base. 
Examples:
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
"""


def narcissistic(value):
    total = 0
    power = len(str(value))
    for num in str(value):
        total += (int(num) ** power)
    return total == value


def narcissistic2(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))


print(narcissistic(153))
print(narcissistic(1634))
print(narcissistic(1992))
