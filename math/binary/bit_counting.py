"""
https://www.codewars.com/kata/526571aae218b8ee490006f4

Given a non-neg int, return num of bits that are equal to 1 in the binary representation of that number

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""


def count_bits(n):
    return [char for char in str(bin(n))][2:].count('1')


print(count_bits(1234))
