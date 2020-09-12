"""
https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python

Given an array of consecutive (increasing) letters, return the missing letter. 

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Examples:
['a','b','c','d','f'] -> 'e' 
['O','Q','R','S'] -> 'P'

"""
from typing import List


def find_missing_letter(chars: List[str]) -> str:
    current_ord = ord(chars[0])
    for i in range(1, len(chars)):
        if ord(chars[i]) != current_ord + 1:
            return chr(current_ord + 1)
        current_ord += 1
    return


print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))
print(find_missing_letter(['O', 'Q', 'R', 'S']))
