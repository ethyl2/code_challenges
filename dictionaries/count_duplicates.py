"""
https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
Given a string of uppercase and/or lowercase chars and digits, return count of chars & digits that occur more than once. 
Either upper/lower case counts toward a count.

Example:
'abcdef' -> 0
'aaBb' -> 2
'aA11' -> 2
"""


def duplicate_count(text: str) -> int:
    char_set = set()
    duplicates_set = set()
    for char in text:
        char = char.lower()
        if char in char_set:
            duplicates_set.add(char)
        char_set.add(char)
    return len(duplicates_set)


print(duplicate_count('abcdef'))
print(duplicate_count('aaBb'))
print(duplicate_count('aA11'))
