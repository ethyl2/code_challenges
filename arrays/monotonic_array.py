"""
From algo expert:

Given an array.
Return whether it is monotonic, which means that it gets bigger 
(or adajenct values are the same) throughout, or gets smaller (or adajenct values are the same) throughout.

Example:
arr=[-1,-5,-10,-1100, -1101, -1102, -9001]
True
"""
from typing import List

# My first version determines the direction at the very first. That is used for the check during the iteration.


def is_monotonic(arr: List):
    is_increasing = arr[0] < arr[-1]
    current = 1
    while current < len(arr):
        if (arr[current] >= arr[current-1] and is_increasing) or (arr[current] <= arr[current-1] and not is_increasing):
            current += 1
        else:
            return False
    return True

# This second version uses 2 boolean values. During the iteration, if they are ever both true, we return False.


def is_monotonic2(arr: List):
    is_increasing = False
    is_decreasing = False

    for current in range(1, len(arr)):
        if arr[current] > arr[current-1]:
            is_increasing = True
        elif arr[current] < arr[current-1]:
            is_decreasing = True
        if is_increasing and is_decreasing:
            return False

    return True


print(is_monotonic([-1, -5, -10, -1100, -1101, -1102, -9001]))
print(is_monotonic([-1, -5, -10, 90, -1101, -1102, -9001]))
print(is_monotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
print(is_monotonic([1, 3, 5, 55, 678]))
print(is_monotonic([1, 3, -5, 55, 678]))
print(is_monotonic([1, 3, 3, 55, 678]))

'''
True
False
True
True
False
True
'''
