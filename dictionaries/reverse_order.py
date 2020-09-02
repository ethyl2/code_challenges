"""
Stretch:
Given a hashmap where the keys are integers, 
print out all of the values of the hashmap in reverse order, ordered by the keys.
For example, given the following hashmap:
{
  14: "vs code",
  3: "window",
  9: "alloc",
  26: "views",
  4: "bottle",
  15: "inbox",
  79: "widescreen",
  16: "coffee",
  19: "tissue",
}
The expected output is:
widescreen
views
tissue
coffee
inbox
vs code
alloc
bottle
window
since "widescreen" has the largest integer key, "views" has the second largest, etc.
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""
from typing import Dict, List


def print_reversed1(hm: Dict) -> None:
    """
    O(n) time, O(n) space
    """
    hm_list = list(hm.items())
    hm_list.sort(key=lambda x: -x[0])
    for key, value in hm_list:
        print(value)


def print_reversed(hm: Dict) -> None:
    '''
    Similar to first version, but combines 2 lines into one.
    Using sorted() makes another copy, but overall still O(n) space.
    O(n) time, O(n) space
    '''
    hm_list = sorted(list(hm.items()), key=lambda x: -x[0])

    for key, value in hm_list:
        print(value)


hm1 = {
    14: "vs code",
    3: "window",
    9: "alloc",
    26: "views",
    4: "bottle",
    15: "inbox",
    79: "widescreen",
    16: "coffee",
    19: "tissue",
}

print_reversed(hm1)

"""
Here's the easier problem:
Given the following array of values, print out all the elements in reverse order, with each element on a new line.
For example, given the list
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
Your output should be
0
1
2
3
4
5
6
7
8
9
10
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process 
"""


def print_reversed_list(arr: List[int]) -> None:
    """
    O(n) time, O(n) space
    """
    for num in reversed(arr):
        print(num)


def print_reversed_list2(arr: List[int]) -> None:
    """
    O(n) time, O(1) space
    """
    for i in range(len(arr)-1, -1, -1):
        print(arr[i])


def print_reversed_list3(arr: List[int]) -> None:
    """
    O(n) time, O(n) space
    """
    for num in arr[::-1]:
        print(num)


arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print_reversed_list3(arr1)
