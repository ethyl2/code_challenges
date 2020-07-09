"""
https://app.codesignal.com/interview-practice/task/uX5iLwhc6L5ckSyNC/description
Given string s of small Eng chars

Find 1st inst of non-repeating char

If none, return _

s = "abacabad" <- c because while both c and d don't repeat, c appears first
"""


def first_not_repeating_char(s):
    # Initialize lookup dict
    # Loop thru s to create all entries in dict
    # Loop thru again to find first char that doesn't have a value in dict of 2 or more
    # If found, return that char
    # At end, return _

    lookup = {}
    for char in s:
        if char in lookup:
            lookup[char] += 1
        else:
            lookup[char] = 1
    for char in s:
        if lookup[char] == 1:
            return char
    return '_'


print(first_not_repeating_char("abacabad"))
