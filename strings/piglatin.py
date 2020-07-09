"""
https://www.codewars.com/kata/520b9d2ad5c005041100000f/python

Given a string, move the first letter of each word to the end of it, and then add 'ay' to the end of the world.
Leave punctuation marks untouched.

Examples:
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


import string
import re

# First version uses my custom punctuation set

# This is the only one that checks for punctuation that is right next to a word, like 'end.' and deals with it.
# It didn't seem needed to get the tests to pass, so I didn't implement that case in the other versions.


def pig_it(text):
    punctuation = {'.', ',', '!', '?'}
    piggy_words = []
    for word in text.split(' '):
        if word in punctuation:
            piggy_words.append(word)
        elif word[-1] in punctuation:
            piggy_words.append(word[1:-1] + word[0] + 'ay' + word[-1])
        else:
            piggy_words.append(word[1:] + word[0] + 'ay')
    piggy_string = ' '.join(piggy_words)
    return piggy_string

# Second version uses re to check for punctuation


def pig_it2(text):
    piggy_words = []
    for word in text.split(' '):
        if re.match('\W', word):
            piggy_words.append(word)
        else:
            piggy_words.append(word[1:] + word[0] + 'ay')
    return ' '.join(piggy_words)

# Third version uses string.punctuation for punctuation check


def pig_it3(text):
    piggy_words = []
    for word in text.split(' '):
        if word in string.punctuation:
            piggy_words.append(word)
        else:
            piggy_words.append(word[1:] + word[0] + 'ay')
    return ' '.join(piggy_words)

# My fourth version is like the 3rd version, but puts it into a list comprehension


def pig_it4(text):
    return ' '.join([word if word in string.punctuation else word[1:] + word[0] + 'ay' for word in text.split(' ')])

# And here's fifth version that uses .isalpha() to check for punctuation:


def pig_it5(text):
    return ' '.join([word[1:] + word[0] + 'ay' if word.isalpha() else word for word in text.split(' ')])


print(pig_it('Thomas is so crazy and loves to eat sushi.'))
print(pig_it2('Hello world !'))
print(pig_it3('Pig latin is cool !'))
print(pig_it4('Pig latin is cool !'))
print(pig_it5('Pig latin is cool !'))
