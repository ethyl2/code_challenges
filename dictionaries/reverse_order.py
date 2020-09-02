"""Given a hashmap where the keys are integers, 
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
from typing import Dict


def print_reversed1(hm: Dict) -> None:
    hm_list = list(hm.items())
    hm_list.sort(key=lambda x: -x[0])
    for key, value in hm_list:
        print(value)


def print_reversed(hm: Dict) -> None:
    '''
    Similar to first version, but combines 2 lines into one.
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
