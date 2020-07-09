"""
from hackerrank

Given: non-empty arr of distinct integers
And a target int

Find all triplets in arr that sum up to target sum

Return a 2D arr of all these triplets
With each inner arr sorted in ascending order
And triplets ordered in ascending order by first triplet el
secondary: smallest 2nd el
tertiary: smallest third el

If no triplets, return empty arr

Example:
[12, 3, 1, 2, -6, 5, -8, 6], 0
Return [[-8,2,6], [-8, 3, 5], [-6,1,5]]
"""
# My Initial Plan:
# Generate all triplets
# Check to see if their sum is target
# If so, add to output_arr
# Sort output arr

from itertools import combinations

# Here is my first approach. O(n^3) time. O(n^3) space, too, most likely.


def threeNumberSum_initial(arr, target):
    # Generate triplets:
    triplets = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                # print("i, j, k: " + str(arr[i]) +
                #      " " + str(arr[j]) + " " + str(arr[k]))
                triplets.append([arr[i], arr[j], arr[k]])

    # Now, find winning triplets -- the ones that sum up to the target:
    winners = []
    for triplet in triplets:
        total = triplet[0] + triplet[1] + triplet[2]
        if total == target:
            # print('Found one!')
            triplet.sort()
            winners.append(triplet)
    winners.sort()
    return winners

# This second approach uses combinations from itertools, in case it is faster.
# Probably still time O(n^3), though probably more optimized under the hood.


def threeNumberSum_second(arr, target):
    # First, generate triplets.
    combos = combinations(arr, 3)
    triplets = [list(combo) for combo in combos]

    # Now, find winning triplets -- the ones that sum up to the target:
    winners = []
    for triplet in triplets:
        total = triplet[0] + triplet[1] + triplet[2]
        if total == target:
            # print('Found one!')
            triplet.sort()
            winners.append(triplet)
    winners.sort()
    return winners

# Here is my submitted solution, which makes doubles instead of triplets initially.
# So the time complexity would be probably around O(n^2)


def threeNumberSum(arr, target):
    # Try out doubles, to see if it's faster:
    double_combos = combinations(arr, 2)
    doubles = [combo for combo in double_combos]
    # print(doubles)

    # Generate lookup table to figure out later what is needed to reach target with each double.

    # An entry in lookup might look like this: 10: [(2,8), (3,7), (1,9)]
    # The sum is the key.
    # The value is an array of the doubles that sum up to the key.

    lookup = {}
    for double in doubles:
        # print(double[0] + double[1])

        if (double[0] + double[1]) not in lookup:
            lookup[double[0] + double[1]] = [double]
        else:
            lookup[double[0] + double[1]].append(double)

    # print(lookup)

    # Loop thru arr to see if the key of target - num exists in the dictionary. num is the current number.
    # If so, make a triplet with each of the values for that key with num
    #   if num != either of the numbers in a value's double
    #   (to eliminate duplicated numbers -- we can't use the same number in the array twice or more in one triplet.)
    my_triplets = []
    for num in arr:
        if (target - num) in lookup:
            for double in lookup[target - num]:
                if num != double[0] and num != double[1]:
                    triplet = [num, double[0], double[1]]
                    triplet.sort()
                    if triplet not in my_triplets:
                        my_triplets.append(triplet)
    my_triplets.sort()
    return my_triplets

# This version tries out an idea from the interviewer, in which the arr is sorted first,
# so my return array doesn't need to be sorted later.
# The sort() is still needed to sort the numbers inside the triplets, though,
#   to eliminate duplicate triplets and to ensure that the numbers inside the triplet are sorted.

# My way (sorting later), might be faster, because the length of the winning triplets array might very well be less
# than the length of the arr.


def threeNumberSum_sort_first(arr, target):
    arr.sort()
    double_combos = combinations(arr, 2)
    doubles = [combo for combo in double_combos]

    lookup = {}
    for double in doubles:

        if (double[0] + double[1]) not in lookup:
            lookup[double[0] + double[1]] = [double]
        else:
            lookup[double[0] + double[1]].append(double)

    my_triplets = []
    for num in arr:
        if (target - num) in lookup:
            for double in lookup[target - num]:
                if num != double[0] and num != double[1]:
                    triplet = [num, double[0], double[1]]
                    triplet.sort()  # Still needed to eliminate duplicate triplets and to return the numbers sorted
                    if triplet not in my_triplets:
                        my_triplets.append(triplet)

    return my_triplets


# Tests:

print(threeNumberSum_initial([12, 3, 1, 2, -6, 5, -8, 6], 0))
print(threeNumberSum_second([12, 3, 1, 2, -6, 5, -8, 6], 0))
print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
print(threeNumberSum_sort_first([12, 3, 1, 2, -6, 5, -8, 6], 0))
# All should return [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
