"""
https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

Given a non-empty string consisting of words, return the length of the shortest word(s).

Example: find_short("bitcoin take over the world maybe who knows perhaps") -> 3
"""


def find_short(s: str) -> int:
    return min(len(word) for word in s.split(' '))


print(find_short("bitcoin take over the world maybe who knows perhaps"))
