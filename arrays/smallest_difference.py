"""
From algo expert

Given 2 non-empty arrays of integers,
find the pair of integers (one from the first array, the other from the second) whose absolute difference is closest to zero.
Return an array with those numbers, with the number from the first array in the first position.

Example: [-1,5,10,20, 28, 3], [26,134, 135, 15, 17] -> [28, 26]
"""
from typing import List


def find_nums_with_abs_smallest_diff(array_one: List[int], array_two: List[int]) -> List[int]:
    """
    First approach. Naive. O(n*m) time complexity, O(1) space.
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


def find_nums_with_abs_smallest_diff2(array_one: List[int], array_two: List[int]) -> List[int]:
    """
    Second approach. 
    Sorts the arrays and then iterates through them. O(n log n + m log m) time.
    O(1) space.
    """
    array_one.sort()
    array_two.sort()
    pointer_one = 0
    pointer_two = 0
    output = [None, None]
    current_winner = float('inf')
    while pointer_one < len(array_one) and pointer_two < len(array_two):
        abs_diff = abs(array_one[pointer_one] - array_two[pointer_two])
        if abs_diff < current_winner:
            current_winner = abs_diff
            output[0] = array_one[pointer_one]
            output[1] = array_two[pointer_two]
        if array_one[pointer_one] < array_two[pointer_two]:
            # Move the pointer_one to a value that will be closer to the current value of the second array.
            pointer_one += 1
        else:
            # Move pointer_two to a value that will be closer to the current value of the first array.
            pointer_two += 1
    return output


if __name__ == "__main__":
    print(find_nums_with_abs_smallest_diff(
        [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
    print(find_nums_with_abs_smallest_diff2(
        [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
