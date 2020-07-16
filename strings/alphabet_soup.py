"""
https://edabit.com/challenge/4Agr8CTY7x2rAhh5n
Given a string w/o numbers and punctuation, a single word, return a string with letters in alphabetical order.
"""


def alphabet_soup(txt):
    # First version
    # return ''.join(sorted([char for char in txt]))
    # Second version
    return ''.join(sorted(txt))


print(alphabet_soup('cheese'))
