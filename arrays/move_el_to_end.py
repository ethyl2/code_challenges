"""
From algo expert
Given an array of ints, and an int,
move all instances of that int to the end of the array, in place.
The order of the elements that aren't the int does not matter.

[2,1,2,2,2,3,4,2], 2 -> [1,3,4,2,2,2,2,2]
"""
from typing import List


def move_el_to_end(arr: List, num: int) -> None:
    # Deal with edge cases.
    if arr.count(num) == len(arr) or arr.count(num) == 0:
        return

    left = 0
    right = len(arr) - 1

    # Move the left and right pointers until the left is at the desired value
    # and right is not that value.
    while arr[left] != num:
        left += 1

    while arr[right] == num:
        right -= 1

    # Now loop until pointers cross.

    while right > left:
        # Swap the values
        arr[left], arr[right] = arr[right], arr[left]

        # Move the pointers to the desired positions
        while arr[left] != num:
            left += 1
        while arr[right] == num:
            right -= 1
    return None


arr1 = [2, 1, 2, 2, 2, 3, 4, 2]
move_el_to_end(arr1, 2)
print(arr1)

arr2 = [1, 1, 1, 1]
move_el_to_end(arr2, 1)
print(arr2)

arr3 = []
move_el_to_end(arr3, 1)
print(arr3)

arr4 = [4, 3, 2, 1]
move_el_to_end(arr4, 7)
print(arr4)

arr5 = [1, 3, 4, 2, 2, 2, 2, 2]
move_el_to_end(arr5, 2)
print(arr5)
