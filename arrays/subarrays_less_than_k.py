"""
From Kapil Sharma's lecture 7-28-2020
Given an array of non-negative numbers and non-negative int k, find num of subarrays with their sum less than k.

Subarrays are contiguous elements.

Examples:
arr = [2,5,6], k= 10 -> Return 4.
Subarrays are [2], [5], [6], [2,5]

arr = [1,11,2,3,15], k=10 -> Return 4.
Subarrays are [1], [2], [3], [2,3]
"""

# First version has time complexity of O(n^2) and space O(1)


def countSubsLessThanK(arr, k):
    # Edge cases
    if arr == None or len(arr) == 0 or k == 0:
        return 0

    # subarrays = []  # For testing purposes
    count = 0
    total = 0

    for i in range(len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
            if total < k:
                count += 1
                # subarrays.append(arr[i:j+1])  # For testing purposes
            else:
                break
    # print(subarrays)  # For testing purposes
    return count


# print(countSubsLessThanK([2, 5, 6], 10))

# This version is more time-efficient: O(n)
def countSubsLessThanK2(arr, k):
    # Edge cases
    if arr == None or len(arr) == 0 or k == 0:
        return 0

    start = 0
    end = 0
    count = 0
    total = arr[0]
    # subarrays = set() # For testing purposes

    while start < len(arr) and end < len(arr):
        if total < k:
            end += 1
            if end >= start:
                count += (end-start)
                # subarrays.add(tuple([arr[start]]))
                # subarrays.add(tuple([arr[end-1]]))
                # if end-start > 1:
                #     for i in range(start, end):
                #         subarray = arr[start: start+i+1]
                #         subarrays.add(tuple(subarray))
            if end < len(arr):
                total += arr[end]
        else:
            total -= arr[start]
            start += 1
    # print(subarrays)
    return count


print(countSubsLessThanK2([2, 5, 6], 10))
