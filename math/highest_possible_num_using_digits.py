"""
https://www.codewars.com/kata/5467e4d82edf8bbf40000155

Given a non-negative int,
return an int that consists of the output's digits arranged in descending order (which creates the highest possible number)

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""


def descending_order(num: int) -> int:
    digits = [digit for digit in str(num)]
    digits.sort(key=lambda x: int(x), reverse=True)
    return int(''.join(digits))


def descending_order2(num: int) -> int:
    return int(''.join(sorted([digit for digit in str(num)], key=lambda x: int(x), reverse=True)))


print(descending_order2(24))
