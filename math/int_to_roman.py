"""
https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python

Given a positive integer, return a string of the Roman numeral representation of that number.

solution(1000) # should return 'M'
"""


def solution(n: int) -> str:
    lookup = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
    output = ''
    if n >= 1000:
        num_ms = n // 1000
        output += lookup[1000] * num_ms
        n = n % 1000
    if n >= 900:
        output += lookup[100] + lookup[1000]
        n -= 900
    if n >= 500:
        output += lookup[500]
        n -= 500
    if n >= 400:
        output += lookup[100] + lookup[500]
        n -= 400

    if n >= 100:
        num_ms = n // 100
        output += lookup[100] * num_ms
        n = n % 100
    if n >= 90:
        output += lookup[10] + lookup[100]
        n -= 90
    if n >= 50:
        output += lookup[50]
        n -= 50
    if n >= 40:
        output += lookup[10] + lookup[50]
        n -= 40

    if n >= 10:
        num_ms = n // 10
        output += lookup[10] * num_ms
        n = n % 10
    if n >= 9:
        output += lookup[1] + lookup[10]
        n -= 9
    if n >= 5:
        output += lookup[5]
        n -= 5
    if n >= 4:
        output += lookup[1] + lookup[5]
        n -= 4

    if n >= 1:
        output += lookup[1] * n

    # print(output)
    # print(n)
    return output


def solution2(n: int) -> str:
    """
    another person's implementation. More concise. Uses more keys than I did, but that pays off.
    """
    roman_numerals = {1000: 'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
                      }
    roman_string = ''
    for key in sorted(roman_numerals.keys(), reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string


print(solution(14))
