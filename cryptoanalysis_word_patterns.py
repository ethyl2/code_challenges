"""
https://www.codewars.com/kata/5f3142b3a28d9b002ef58f5e

Return the word pattern for a given word.
All words provided will be non-empty strings of alphabetic characters only, i.e. matching the regex "[a-zA-Z]+".

example, the word "hello" would become "0.1.2.2.3"

A word pattern is a description of the patterns of letters occurring in a word,
where each letter is given an integer code in order of appearance.
So the first letter is given the code 0, and second is then assigned 1
if it is different to the first letter or 0 otherwise, and so on.
"""


from collections import defaultdict


def word_pattern(word: str) -> str:
    output = ''
    lookup = {}
    current_num = 0
    for character in word:
        char = character.lower()
        if char in lookup:
            output += str(lookup[char]) + '.'
        else:
            lookup[char] = current_num
            output += str(current_num) + '.'
            current_num += 1
    return output[:-1]


print(word_pattern('hello'))
result2 = word_pattern("Hippopotomonstrosesquippedaliophobia")
answer2 = "0.1.2.2.3.2.3.4.3.5.3.6.7.4.8.3.7.9.7.10.11.1.2.2.9.12.13.14.1.3.2.0.3.15.1.13"
print(result2 == answer2)

# Another person's implementation:
'''
A defaultdict works exactly like a normal dict, but it is initialized with a function (“default factory”) 
that takes no arguments and provides the default value for a nonexistent key.

A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.

Here, the defaultdict will provide a value that is the current length of the dictionary,
as the default value. So it starts at 0 and increments by 1 each time a new entry is added. Perfect!
'''


def word_pattern2(s):
    d = defaultdict(lambda: str(len(d)))
    return '.'.join(d[c] for c in s.lower())


print(word_pattern2('hello'))

# Making the solution above a bit less concise, to make sure I understand it.


def word_pattern3(s):
    d = defaultdict(lambda: str(len(d)))
    output = ''
    for char in s:
        output += d[char] + '.'
    return output[:-1]


print(word_pattern3('hello'))
