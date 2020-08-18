"""
https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

Given a string, return a string that consists of the original string, but with vowels (not y) removed.

Example:
"This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!"
"""


def disemvowel(string: str) -> str:
    vowels = set('aeiou')
    output = ''
    for char in string:
        if char.lower() not in vowels:
            output += char
    return output

# My second version that is more condensed.


def disemvowel2(string: str) -> str:
    vowels = set('aeiou')
    return ''.join(char for char in string if char.lower() not in vowels)


print(disemvowel2("This website is for losers LOL!"))
