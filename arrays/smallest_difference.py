"""
From algo expert

Given non-empty arrays of integers,
find the pair whose absolute difference is closest to zero.
Return an array with those numbers, with the number from the first array in the first position.

Example: [-1,5,10,20, 28, 3], [26,134, 135, 15, 17] -> [28, 26]
"""
from typing import List


def find_nums_with_abs_smallest_diff(array_one: List[int], array_two: List[int]) -> List[int]:
    """
    First approach. Brute-force style. O(n*m) time complexity, O(1) space.
    """
    output = [None, None]
    current_winner = float('inf')
    for num1 in array_one:
        for num2 in array_two:
            abs_diff = abs(num1 - num2)
            if abs_diff < current_winner:
                current_winner = abs_diff
                output[0] = num1
                output[1] = num2
    return output


print(find_nums_with_abs_smallest_diff(
    [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
