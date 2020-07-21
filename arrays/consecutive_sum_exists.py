'''
From Kapil Sharma's lecture 07-21-2020
Given array A, which consists of non-negative elements, find if consecutive elements in array
    will add up to the given value T.
Return boolean.

Examples:
A = [4,6,1,2,7,9]

T = 0 # False
T = 100 # False
T  = 9 # True because 6 + 1 + 2 = 9

Note: The length of the consecutive numbers could be 1 - len(A).

Use a sliding window approach.
Two pointers: left_index and right_index.
Gradually increment right_index until the total is equal to or greater than T.
At that point, if the total == T, return True.
    Otherwise, kick out the value at the left_index and increment the left_index.
Return False if the left_index has made it all the way across the array without a return.
'''


def consecutive_sum_exists(A, T):
    # Base cases
    if T < 0 or A is None or T is None:
        return False

    total = 0
    right_index = 0

    for left_index in range(len(A)):
        while (right_index < len(A) and total < T):
            total += A[right_index]
            right_index += 1
        # Second part of line below takes care of false positives that otherwise would happen when T is 0,
        #   but no 0s are present in the array.
        if total == T and T != 0:
            return True
        # Only return True when T = 0 when there actually is a 0 in the array.
        elif T == 0 and A[left_index] == 0:
            return True
        # Eliminate the value at left_index because it should be excluded when the window moves along.
        total -= A[left_index]
    return False


print(consecutive_sum_exists([4, 6, 1, 2, 7, 9], 9))
print(consecutive_sum_exists([4, 6, 1, 2, 7, 9], 100))
print(consecutive_sum_exists([4, 6, 1, 2, 7, 9], 0))
print(consecutive_sum_exists([0, 4, 6, 1, 2, 7, 9], 0))
print(consecutive_sum_exists([4, 6, 1, 0, 2, 7, 9], 0))
