"""
https://www.codewars.com/kata/5656b6906de340bd1b0000ac/python


Given 2 strings. (Note: they aren't sorted).
Return a new sorted string, the longest possible, 
containing distinct letters (each taken once, from the 1st or 2nd string)

Examples: 

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""


def longest(s1, s2):
    s1_list = set(s1)
    if s1 == s2:
        return ''.join(sorted(s1_list))

    s1_list.update(s2)
    return ''.join(sorted(s1_list))


def longest2(a1, a2):
    return "".join(sorted(set(a1 + a2)))


print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))
a = "abcdefghijklmnopqrstuvwxyz"
print(longest(a, a))  # -> "abcdefghijklmnopqrstuvwxyz"
