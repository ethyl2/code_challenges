"""
https://www.codewars.com/kata/54d81488b981293527000c8f/train/python

Given an array of ints and a sum, return the 1st 2 values (starting from the left) that add up to form the sum.
Return None is no pairs can sum up to the sum.

The trickiest part of this is determining how to get the winner between 2 pairs, in which one pair's first value has a
lower index, but the other pair's second value has a lower index. The one with the lower second index should win.

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
"""
from typing import List


def sum_pairs(ints: List[int], s: int):
    ints_set = set(ints)
    winning_pairs = []
    for num in ints:
        if s-num in ints_set and num != s-num:
            winning_pairs.append([num, s-num])
        elif s-num in ints_set and num == s-num and ints.count(num) > 1:
            winning_pairs.append([num, s-num])

    if len(winning_pairs) == 0:
        return None
    winner = min(
        winning_pairs, key=lambda x: find_rightmost_index(ints, x[0], x[1]))

    # winner.sort(key=lambda x: ints.index(x))
    return winner


def sum_pairs1(ints, s):
    ints_set = set(ints)
    for num in ints:
        if s-num in ints_set:
            # print('For num ', num, ' Found one! ', s-num)
            return [num, s-num]
    return None


def find_rightmost_index(arr: List[int], num1, num2):
    indices1 = [index for index, el in enumerate(arr) if el == num1]
    indices2 = [index for index, el in enumerate(arr) if el == num2]
    indices1.extend(indices2)
    return max(indices1)


def find_rightmost_index2(arr, num):
    return max([index for index, el in enumerate(arr) if el == num])


l1 = [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [20, -13, 40]
l4 = [1, 2, 3, 4, 1, 0]
l5 = [10, 5, 2, 3, 7, 5]
l6 = [4, -2, 3, 3, 4]
l7 = [0, 2, 0]
l8 = [5, 9, 13, -3]

# print(find_rightmost_index(l7, 0, 2))
# print(find_rightmost_index(l5, 5, 5))
# print(find_rightmost_index(l5, 1, 7))

# print(sum_pairs(l1, 8))
# print(sum_pairs(l1, 8) == [1, 7])

print(sum_pairs(l5, 10))
# print(sum_pairs(l5, 10) == [3, 7])
# [10, 5, 2, 3, 7, 5]

# print(sum_pairs1([1, -2, 3, 0, -6, 1], -6))  # [0, -6]

# print(sum_pairs(l4, 2))
#

# print(sum_pairs1([1, 2, 3, 4, 1, 0], 2))  # [1,1]
