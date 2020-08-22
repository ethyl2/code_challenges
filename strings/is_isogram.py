"""
From CS TL ProDev session 12 Jun 2020

Given a string, return whether it is an isogram (a word with no repeating letters, such as 'ambidextrously').
Ignore hypens or spaces.

(Return True or False)
"""
import re

# My version with O(n) time complexity, O(n) space


def is_isogram(my_string):
    lookup = set()
    my_string = my_string.lower()
    my_string = re.sub(r'[\s\-]', '', my_string)
    print(my_string)
    for letter in my_string:
        # and letter not in ('-', ' '): #If you take out line 15
        if letter in lookup:
            return False
        else:
            lookup.add(letter)
    return True

# Original version with O(n*n) time complexity, O(1) space


def is_isogram2(my_string):
    for i in range(len(my_string)):
        curr = my_string[i]
        if curr.isalpha():
            if curr in my_string[i+1:]:
                return False
    return True


def is_isogram3(string: str) -> bool:
    """
    https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
    A simpler version, which assumes that input has only letters.
    Ignore letter case.
    Assume an empty string is an isogram
    """
    cache = set()
    for char in string.lower():
        if char in cache:
            return False
        cache.add(char)
    return True


print(is_isogram('Amb idex--tr  ously'))
print(is_isogram2('Amb idex--tr  ously'))

print(is_isogram('butter'))
print(is_isogram2('butter'))

print(is_isogram3("Dermatoglyphics"))  # True
print(is_isogram3("aba"))  # false
print(is_isogram3("moOse"))  # false
