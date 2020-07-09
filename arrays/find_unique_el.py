"""
https://www.codewars.com/kata/585d7d5adb20cf33cb000235/python

Given an array with at least 3 numbers. All are equal except one. Size could be very large.

Return the unique number

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

"""

# First approach. Time O(2n) -> O(n) Space O(n)


def find_uniq(arr):
    lookup = dict()
    for num in arr:
        if num in lookup:
            lookup[num] += 1
        else:
            lookup[num] = 1
    for entry in lookup.items():
        if entry[1] == 1:
            return entry[0]

# 2nd approach. Time O(n) Space O(n)


def find_uniq2(arr):
    lookup = set([arr[0]])
    current_winner = [arr[0]]
    for num in arr:
        if num != current_winner and num not in lookup:
            current_winner.append(num)
            lookup.add(num)
        elif len(current_winner) > 1 and num == current_winner[-1]:
            current_winner.pop()
    return current_winner[-1]


# Their first suggested solution:
def find_uniq3(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


print(find_uniq3([1, 1, 1, 2, 1, 1]))
print(find_uniq3([0, 1, 1]))
