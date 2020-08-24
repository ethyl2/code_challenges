"""
https://www.codewars.com/kata/5390bac347d09b7da40006f6

Given a string, return a string in which each word is capitalized

Example:
Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
"""


def to_jaden_case(string: str) -> str:
    return ' '.join([word.capitalize() for word in string.split()])


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
