"""
From CS TL ProDev session 12 Jun 2020

Given a string, return whether it is a pangram (contains all of the letters of the alphabet, at least once)
The string will only be ASCII chars.
"""
import re


def is_pangram(my_string):
    letter_set = set()
    my_string = re.sub(r"[\-\s]", "", my_string)
    for letter in my_string.lower():
        letter_set.add(letter)
    return len(letter_set) == 26


print(is_pangram("Two driven jocks help fax my big quiz"))
print(is_pangram("Pack my --box with five dozen liquor jugs"))
print(is_pangram("Pack my ball with five dozen liquor jugs"))
