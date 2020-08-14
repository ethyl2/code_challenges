"""
From Sean Chen Lecture 08-14-2020

Given a sorted array that is broken up at some rotation point, and a target, find the target.
The rotation point is the smallest value.

arr = [3,5,7,9,0,1,2] target = 1  -> 5  Note: The rotation point is the value 0 at index 4.


"""


def shifted_binary_search(arr, target):
    if len(arr) < 1:
        return -1

    rp = find_rotation_point(arr)
    left = binary_search(arr, target, 0, rp - 1)
    right = binary_search(arr, target, rp, len(arr) - 1)
    if left != -1:
        return left
    if right != -1:
        return right
    return -1


def binary_search(arr, target, left, right):
    if right >= left:
        mid = left + (right-left) // 2
    else:
        return -1

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid-1)
    else:
        return binary_search(arr, target, mid+1, right)


def find_rotation_point(arr):
    left = 0
    right = len(arr) - 1

    if left + 1 == right:
        return right

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[0]:
            # If arr[mid] is greater than the first value, the rp is not on the left side
            left = mid
        else:
            # The rp must be somewhere in the right side
            right = mid

        # Now, once the floor and the ceiling are adjacent, we've found the rp!
        if left + 1 == right:
            return right
    return right


# print(shifted_binary_search([3, 5, 7, 9, 0, 1, 2], 1))
# print(find_rotation_point([3, 5, 7, 9, 0, 1, 2]))
# print(binary_search([1, 3, 5, 6], 1, 0, 3))
# print(shifted_binary_search([1, 2, 3, 4], 3))
# print(shifted_binary_search([], 5))
# print(shifted_binary_search([1], 1))
print(shifted_binary_search([3, 1], 1))
print(find_rotation_point([3, 1]))
