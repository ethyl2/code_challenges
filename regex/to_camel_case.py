"""
https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
Given a string with words seperated by dashes or underscores, 
return the string in camel casing -- BUT with the first word capitalized if it was originally.

to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

"""
import re


def to_camel_case(text: str) -> str:
    words = re.split('[\-\_]', text)
    return words[0] + ''.join(words[i].capitalize() for i in range(1, len(words)))


print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))
