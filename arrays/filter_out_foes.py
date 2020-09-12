"""
https://www.codewars.com/kata/55b42574ff091733d900002f/train/python

Given a list of strings, return a list, in the same order, of strings that are of length 4.

Example: friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
"""

from typing import List


def friend(x: List[str]) -> List[str]:
    return [name for name in x if len(name) == 4]


print(friend(["Ryan", "Kieran", "Mark"]))
