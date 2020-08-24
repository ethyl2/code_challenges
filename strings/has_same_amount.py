"""
https://www.codewars.com/kata/55908aad6620c066bc00002a

Given a string, return whether it has the same amount of x's and o's.
Looks like upper or lower case are both valid towards count.

Examples:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true # when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""
import re


def xo(s: str) -> bool:
    return len(re.findall(r'[oO]', s)) == len(re.findall(r'[xX]', s))


def xo2(s: str) -> bool:
    # Another version that doesn't use re
    s = s.lower()
    return s.count('o') == s.count('x')


print(xo("ooxx"))
print(xo("xooxx"))
print(xo("ooxXm"))
print(xo("zpzpzpp"))

print('\n')

print(xo2("ooxx"))
print(xo2("xooxx"))
print(xo2("ooxXm"))
print(xo2("zpzpzpp"))
