"""
https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q

Given array a
contains nums in range from 1 to len(a)

Find the first duplicate num for which the 2nd occurrence has the minimal index.
If no duplicates, return -1

Example: a = [2,1,3,5,3,2] <- 3

"""


def first_duplicate(a):
    # Initialize lookup table
    # Loop thru a,
    #   If a[i] in lookup table, return a[i]
    #   Else, add a[i] to lookup table

    lookup = {}
    for num in a:
        if num in lookup:
            return num
        else:
            lookup[num] = 1
    return -1


print(first_duplicate([2, 1, 3, 5, 3, 2]))
