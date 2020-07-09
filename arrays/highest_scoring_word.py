"""
https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/python

Given a string of words. All letters will be lowercase. All inputs will be valid.

Find the highest scoring word.

Each letter is equal to points, based on its position in alphabet a=1, b=2, c=3, etc.
If 2 words score the same, return the earliest word of the winners.

Sample tests:
test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
test.assert_equals(high('take me to semynak'), 'semynak')

"""


import string


def high(x):
    # Make lookup dictionary
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lookup = dict()
    for i in range(len(alphabet)):
        lookup[alphabet[i]] = i+1

    # Keep track of current winner
    winner = ''
    # Keep track of current highest score
    winning_score = 0

    for word in x.split(' '):
        score = sum([lookup[char] for char in word])
        if score > winning_score:
            winning_score = score
            winner = word
    return winner


'''
The ord() function returns an integer representing the Unicode character.
ord(‘a’) returns the integer 97

I can't find documentation for the time complexity of ord(), but if it is O(1), which it very
well might be, this second implementation would be more ideal than mine, because it doesn't need to allocate
time and space to make a lookup dictionary.
'''

# Another person's solution that uses ord(char) instead of lookup:


def high2(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


'''
"In Python3, ascii_lowercase is a pre-initialized string used as string constant. 
In Python, string ascii_lowercase will give the lowercase letters ‘abcdefghijklmnopqrstuvwxyz’."
https://www.geeksforgeeks.org/python-string-ascii_lowercase/
I'm thinking that this isn't as good at time complexity as my solution, because looking up c in
    string.ascii_lowercase is O(n), unlike when you use a dictionary, which is O(1).
'''
# Another person's solution that uses string.ascii_lowercase()


def high3(x):
    return max(x.split(), key=lambda k: sum(string.ascii_lowercase.index(c)+1 for c in k))


print(high3('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))
