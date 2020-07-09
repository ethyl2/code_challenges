"""
https://www.hackerrank.com/challenges/max-array-sum/problem?isFullScreen=true

Given: a arr of ints

Find subset of non-adjacent els with the max sum.
Return that sum.

Example: arr = [-2, 1,3,-4,5]

possible subsets:
Subset      Sum
[-2, 3, 5]   6
[-2, 3]      1
[-2, -4]    -6
[-2, 5]      3
[1, -4]     -3
[1, 5]       6
[3, 5]       8

Return 8
"""
# Find all valid subsets
# Implement a var max_sum that is updated as a higher sum is found.


def maxSubsetSum(arr):
    if len(arr) == 1:
        return arr[0]

    subsets = []
    max_sum = arr[0]
    # Loop through the arr, incrementing the space between numbers each time, until space is len(arr) -1
    for i in range(len(arr)):

        # print("Now starting at index " + str(i))
        for j in range(2, len(arr)):
            new_subset = [arr[i]]
            next_index = i + j
            while next_index < len(arr):
                new_subset.append(arr[next_index])
                next_index += j
            subset_sum = sum(new_subset)
            # print(subset_sum)
            if subset_sum > max_sum:
                max_sum = subset_sum
            subsets.append(new_subset)
    # print(subsets)
    print(max_sum)
    return(max_sum)

# This solution is based off of Andrew Richardson's code, from the endorsement_unit_technical_coaching channel


def maxSubsetSum_faster(arr):
    length = len(arr)
    if length == 1:
        return arr[0]

    max_sums_lookup = [None] * length

    max_sums_lookup[0] = arr[0]
    max_sums_lookup[1] = max(arr[0], arr[1])

    for i in range(2, length):
        # Progressively look to see which is the largest,
        # 1. the sum before i (without adding the value at i because of adjacency)
        # 2. the sum from 2 before i with value at i added to it
        # 3. or the value at i by itself
        # Store the winner
        max_sums_lookup[i] = max(max_sums_lookup[i-1],
                                 arr[i] + max_sums_lookup[i-2], arr[i])

    # The largest will be the very last entry.
    print(max_sums_lookup[-1])
    return max_sums_lookup[-1]


def maxSubsetSum_faster2(arr):
    length = len(arr)
    if length == 1:
        return arr[0]

    two_away = arr[0]
    one_away = max(arr[0], arr[1])
    # winner = 0

    for i in range(2, length):
        # Progressively look to see which is the largest,
        # 1. the sum before i (without adding the value at i because of adjacency)
        # 2. the sum from 2 before i with value at i added to it
        # 3. or the value at i by itself
        # Store the winner
        winner = max(one_away, two_away + arr[i], arr[i])
        two_away = one_away
        one_away = winner

    # The largest will be the very last entry.
    print(winner)
    return winner


'''
maxSubsetSum([-2, 1, 3, -4, 5])
maxSubsetSum([3, 5, -7, 8, 10])
maxSubsetSum([3, 7, 4, 6, 5])  # 13
maxSubsetSum([2, 1, 5, 8, 4])  # 11


maxSubsetSum_faster([-2, 1, 3, -4, 5])
maxSubsetSum_faster([3, 5, -7, 8, 10])
maxSubsetSum_faster([3, 7, 4, 6, 5])  # 13
maxSubsetSum_faster([2, 1, 5, 8, 4])  # 11
'''

maxSubsetSum_faster2([-2, 1, 3, -4, 5])
maxSubsetSum_faster2([3, 5, -7, 8, 10])
maxSubsetSum_faster2([3, 7, 4, 6, 5])  # 13
maxSubsetSum_faster2([2, 1, 5, 8, 4])  # 11
