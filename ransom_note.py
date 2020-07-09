"""
https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him 
through his handwriting. He found a magazine and wants to know if he can cut out whole words from it 
and use them to create an untraceable replica of his ransom note. 
The words in his note are case-sensitive and he must use only whole words available in the magazine. 
He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, 
print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". 
The magazine has all the right words, but there's a case mismatch. The answer is No.

checkMagazine has the following parameters:

magazine: an array of strings, each a word in the magazine
note: an array of strings, each a word in the ransom note

give me one grand today night
give one grand today
-> Yes

two times three is not four
two times two is four
-> No (because 'two' only occurs once in the magazine)
"""
import math
import os
import random
import re
import sys


def checkMagazine(magazine, note):
    # Make a magazine dict, with each word being a key,
    # and the value is how many times the word appears in the magazine.

    # Then loop thru the note and print "No" if word is not in dict or value of dict[word] is zero. And return
    #   Otherwise, decrement value of dict[word]

    # At end, print "Yes"
    # print(magazine)
    # print(note)

    magazine_dict = dict()

    for word in magazine:
        if word in magazine_dict:
            magazine_dict[word] = magazine_dict[word] + 1
        else:
            magazine_dict[word] = 1
    # print(magazine_dict)

    for word in note:
        if word not in magazine_dict or magazine_dict[word] == 0:
            print("No")
            return
        else:
            magazine_dict[word] = magazine_dict[word] - 1
    print("Yes")


magazine1 = "ive got a lovely bunch of coconuts".split(" ")
note1 = "ive got some coconuts".split(" ")
checkMagazine(magazine1, note1)
