#!/bin/python3

'''
https://www.hackerrank.com/challenges/birthday-cake-candles/problem

Given an arr of heights of birthday candles, return the number of candles that have the highest height.

Note: the arr is not sorted.
If the arr was sorted, we could find the first index of the last value, and return len(arr) - first_index.
That would be more time efficient, we think.

sortedCandles = sorted(ar)
firstOccurrence = sortedCandles.index(sortedCandles[-1])
return len(ar) - firstOccurrence
'''

import math
import os
import random
import re
import sys


def birthdayCakeCandles(ar):
    lookup = {}
    max_height = None

    for num in ar:
        if num not in lookup:
            lookup[num] = 1
        else:
            lookup[num] += 1

        if max_height == None:
            max_height = num
        if num > max_height:
            max_height = num
    return lookup[max_height]


print(birthdayCakeCandles([4, 3, 2, 1, 4, 4]))  # < - 3
