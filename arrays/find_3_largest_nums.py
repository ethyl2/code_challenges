"""
from algo expert:

Given an array of ints,
return a sorted array of the 3 largest ints.

Include duplicates when applicable.
Don't sort the input array.

Examples:
array: [10,5,9,10,12]
output: [10,10,12]

array: [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
output: [18, 141, 541]
"""
from typing import List
from collections import deque


def find_3_largest_nums(arr: List) -> List:
    largest_nums = deque()
    largest_nums.append(arr[0])
    # Iterate through arr
    # If current num is greater than largest_nums[0], need to add it
    # And potentially kick out largest_nums[0] if the size is then greater than 3.
    #  Need to deal with duplicates, too.
    for i in range(1, len(arr)):

        # Add a number if it is larger than the smallest largest number
        if arr[i] > largest_nums[0]:
            largest_nums.append(arr[i])
            # Check to make sure it is in the right place
            if arr[i] < largest_nums[1]:
                largest_nums[1], largest_nums[2] = largest_nums[2], largest_nums[1]
            # Eject the smallest if at capacity
            if len(largest_nums) > 3:
                largest_nums.popleft()

        # Dealing with duplicates. Add a number if it is the same as the smallest largest number
        #   and the largest_nums needs another value.
        elif arr[i] == largest_nums[0]:
            if len(largest_nums) < 3:
                largest_nums.appendleft(arr[i])

        # Populate the largest_nums if it needs more values.
        elif len(largest_nums) < 3:
            largest_nums.appendleft(arr[i])

        # Check to make sure the first 2 nums are in the right place
        if largest_nums[0] > largest_nums[1]:
            largest_nums[0], largest_nums[1] = largest_nums[1], largest_nums[0]
    return list(largest_nums)


print(find_3_largest_nums([10, 5, 9, 10, 12]))
print(find_3_largest_nums([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
