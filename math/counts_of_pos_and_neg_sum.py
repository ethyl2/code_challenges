"""
https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
Given an array of ints, return array where 1st el is the count of positives, the 2nd el is sum of negatives.
"""


def count_positives_sum_negatives(arr):
    return [len([num for num in arr if num > 0]), sum([num for num in arr if num < 0])] if arr else arr


def count_positives_sum_negatives2(arr):
    """
    More space efficient, but not as concise as above
    """
    if not arr:
        return arr

    count = 0
    total = 0
    for num in arr:
        if num > 0:
            count += 1
        else:
            total += num
    return [count, total]
