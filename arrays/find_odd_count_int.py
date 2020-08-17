"""
https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

Given: an array of ints
Return the int that occurs an odd num of times (There will always only be one.)
"""
from typing import List

# My implementation. O(n) space, where n is the length of the seq, actually a less than n, because of the duplicates, but simplifies to n.
# O(n) time. O(2n) simplifies to O(n).


def find_it(seq: List) -> int:
    cache = {}
    for num in seq:
        if num in cache:
            cache[num] += 1
        else:
            cache[num] = 1

    return [key for key, value in cache.items() if value % 2 == 1][0]


print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))

# Another person's implementation. This one uses less memory O(1), but might be less time efficient, because has to loop through entire sequence for each
# number in the worst case. O(n^2), where n is the length of seq.


def find_it2(seq: List) -> int:
    for num in seq:
        if seq.count(num) % 2 == 1:
            return num


print(find_it2([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
