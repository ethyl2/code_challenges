"""
https://www.codewars.com/kata/5390bac347d09b7da40006f6

Given a string, return a string in which each word is capitalized

Example:
Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
"""
import string


def to_jaden_case(string: str) -> str:
    """
    My implementation
    """
    return ' '.join([word.capitalize() for word in string.split()])


def to_jaden_case2(string_input: str) -> str:
    """
    Another person's version. string.capwords() is handy.
    """
    return string.capwords(string_input)


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
print(to_jaden_case2("How can mirrors be real if our eyes aren't real"))
