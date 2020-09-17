"""
from algo expert

Given an array of unique integers, return an array of all permutations of those integers in no particular order.

If input array is empty, return an empty array.

Example:
[1,2,3] -> [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
"""
from typing import List


def get_permutations(arr: List[int]) -> List[int]:

    # base case
    if len(arr) == 0:
        return []

    permutations = []
    permutations_helper(arr, [], permutations)
    return permutations


def permutations_helper(arr: List[int], current_permutation: List[int], permutations: List[int]) -> None:
    print('arr: ', arr,
          ' current_permutation: ', current_permutation)

    if len(arr) == 0:
        print('\tTime to add ', current_permutation, '\n')
        permutations.append(current_permutation)

    for i in range(len(arr)):
        arr_without_i = arr[:i] + arr[i+1:]
        new_permutation = current_permutation + [arr[i]]
        permutations_helper(arr_without_i, new_permutation, permutations)


print(get_permutations([1, 2, 3]))
