"""
https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python
Given an int representing a year, return an int representing the century it is in.

The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.

Examples:
centuryFromYear(1705)  returns (18)
centuryFromYear(1900)  returns (19)
centuryFromYear(1601)  returns (17)
centuryFromYear(2000)  returns (20)
"""


def century(year: int) -> int:
    century = year // 100
    return century if year % 100 == 0 else century + 1


def century2(year: int) -> int:
    return (year + 99) // 100


print(century2(1705))
print(century(1900))
print(century(1601))
print(century2(2000))
print(century(1))  # 1
print(century(356))  # 4
print(century2(89))  # 1
