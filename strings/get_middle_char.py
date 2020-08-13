"""
https://www.codewars.com/kata/56747fd5cb988479af000028

Given a string, return the middle char if the string length is odd; return the middle 2 chars if even.

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
"""


def get_middle(s):
    if len(s) % 2 != 0:
        return s[len(s)//2]
    return s[(len(s)//2)-1: (len(s)//2) + 1]


# print(get_middle('test'))

# Same as above, but with a list comprehension
def get_middle2(s):
    return s[len(s)//2] if len(s) % 2 != 0 else s[(len(s)//2)-1: (len(s)//2) + 1]


print(get_middle2('tes'))
