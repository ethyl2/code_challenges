"""
https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

Figure out how to make a function that outputs like the examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

"""


def accum(s):
    output = []
    for i in range(len(s)):
        output.append((s[i]*(i+1)).capitalize())
    return '-'.join(output)


print(accum("abcd"))
print(accum("RqaEzty"))
print(accum("cwAt"))

# This version is the same, except it uses a list comprehension


def accum2(s):
    return '-'.join((s[i]*(i+1)).capitalize() for i in range(len(s)))


print(accum2("abcd"))
print(accum2("RqaEzty"))
print(accum2("cwAt"))
