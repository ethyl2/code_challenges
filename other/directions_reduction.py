"""
https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python

Given an array of directions,
return an array that simplifies them:
    get rid of any adjacent pairs of opposite directions "NORTH", "SOUTH" for example,
    taking into account the pairs that result when adjacent pairs are taken out and new neighbors result.

Sample tests:
a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
test.assert_equals(dirReduc(a), ['WEST'])
u=["NORTH", "WEST", "SOUTH", "EAST"]
test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])
"""
from typing import List

opps = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'WEST': 'EAST', 'EAST': 'WEST'}


def dirReduc(arr: List[str]) -> List[str]:
    for i in range(len(arr)-2):
        # print(i)
        if opps[arr[i]] == arr[i+1]:
            # print('found a pair')
            # print("new arr to use:", arr[:i] + arr[i+2:])

            return dirReduc(arr[:i] + arr[i+2:])

    # print('at the end: ', arr)
    if len(arr) >= 2 and opps[arr[-2]] == arr[-1]:
        return arr[:-2]
    return arr


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST",
                "WEST", "NORTH", "WEST"]))  # ["WEST"]
# ["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))
print(dirReduc(["NORTH", "SOUTH", "EAST", "WEST"]))  # []
print(dirReduc(['NORTH', 'NORTH', 'WEST', 'EAST']))  # ['NORTH', 'NORTH']
