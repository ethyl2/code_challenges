"""
https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

Given a string of letters (which can be a-z), return a string consisting of the number of times the characters are greater than m, followed
by '/' and then the length of the string.

s="aaabbbbhaijjjm"
error_printer(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
error_printer(s) => "8/22"
"""


from re import sub


def printer_error(s: str):
    return ''.join([str(len([char for char in s if char > 'm'])), '/', str(len(s))])


s1 = "aaabbbbhaijjjm"
print(printer_error(s1))

s2 = "aaaxbbbbyyhwawiwjjjwwm"
print(printer_error(s2))

s3 = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print(printer_error(s3))  # "3/56"


def printer_error2(s):
    '''
    This version uses re.sub and format(), but still O(n) time like the one above.
    '''
    return "{}/{}".format(len(sub("[a-m]", '', s)), len(s))
