"""
From algo expert:

Given 2 non-empty arrays of integers,
determine whether 2nd array is a subsequence of the 1st one. 
Subsequence = a set of numbers in the same order as they appear in the array, though not necessarily adjacent in the array.

Example:
array: [1,2,3,4]
subsequence: [1,3,4]
True

array: [5,1,22,25,6,-1,8,10]
subsequence: [1,6,-1,10]
True

Note: a single number in an array and the array itself are valid subsequences of the array.
"""
from typing import List


def is_subsequence(sub: List, arr: List) -> bool:
    sub_index = 0
    arr_index = 0
    while sub_index < len(sub) and arr_index < len(arr):
        if arr[arr_index] == sub[sub_index]:
            sub_index += 1
        arr_index += 1
    if sub_index == len(sub):
        return True
    return False


print(is_subsequence([1, 3, 4], [1, 2, 3, 4]))
print(is_subsequence([1, 4, 3], [1, 2, 3, 4]))
print(is_subsequence([1, 3, 4], [1, 2, 3, 4, 5, 6]))
print(is_subsequence([1, 3, 4, 5], [1, 2, 3, 4]))
print(is_subsequence([1, 6, -1, 10],  [5, 1, 22, 25, 6, -1, 8, 10]))


def recursive_is_subsequence(sub, arr):
    if len(sub) == 0:
        return True
    elif len(arr) == 0:
        return False
    elif arr[0] == sub[0]:
        return recursive_is_subsequence(sub[1:], arr[1:])
    return recursive_is_subsequence(sub, arr[1:])


# print(recursive_is_subsequence([1, 3, 4], [1, 2, 3, 4]))
# print(recursive_is_subsequence([1, 4, 3], [1, 2, 3, 4]))
# print(recursive_is_subsequence([1, 3, 4], [1, 2, 3, 4, 5, 6]))
# print(recursive_is_subsequence([1, 3, 4, 5], [1, 2, 3, 4]))
# print(recursive_is_subsequence([1, 6, -1, 10],  [5, 1, 22, 25, 6, -1, 8, 10]))
