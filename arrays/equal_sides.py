"""
https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

Given an array, return the index where the sum of the integers to the left of that index is equal to the sum of the integers
to the right of that index.

Return -1 if that index does not exist.

Examples:
[1,2,3,4,3,2,1] -> 3
[1,100,50,-51,1,1] -> 1
[20,10,-80, 10, 10 ,15, 35] -> 0
"""
from typing import List


def find_even_index(arr: List[int]) -> int:
    # Iterate through list, comparing the sums of the left and right sides.
    #   Return the current index if the sums are equal.
    left_sum = 0
    right_sum = sum(arr[1:])
    if left_sum == right_sum:
        return 0
    for i in range(0, len(arr) - 1):
        # print(f'{i = }, {left_sum = }, {right_sum = }')
        if left_sum == right_sum:
            return i

        # adjust the sums
        left_sum += arr[i]
        right_sum -= arr[i+1]

    # last check at the last element
    if left_sum == 0:
        return i+1

    return -1


# print(find_even_index([1, 2, 1])) # 1
# print(find_even_index([1, 2, 3, 4, 3, 2, 1])) # 3
# print(find_even_index([1, 100, 50, -51, 1, 1])) # 1
# print(find_even_index([20, 10, -80, 10, 10, 15, 35])) # 0
# print(find_even_index([1, 2, 3, 4, 5, 6]))  # -1
# print(find_even_index([20, 10, 30, 10, 10, 15, 35]))  # 3
print(find_even_index([10, -80, 10, 10, 15, 35, 20]))  # 6
