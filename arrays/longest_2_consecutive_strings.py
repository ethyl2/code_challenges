"""
https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

Given an array of strings, find the longest string consisting of k consecutive strings in the array.

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
"""
from typing import List


def longest_consec(strarr: List[str], k: int) -> int:
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ''
    longest_string = ''.join(strarr[:k])
    longest_length = len(longest_string)
    for i in range(1, len(strarr) - k + 1):
        newest_string = ''.join(strarr[i:i+k])
        if len(newest_string) > longest_length:
            longest_string = newest_string
            longest_length = len(longest_string)
    return longest_string


print(longest_consec(["zone", "abigail", "theta",
                      "form", "libe", "zas", "theta", "abigail"], 2))
