"""
https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python
Given a array of directions: 'n', 's', 'e', or 'w',
and given that each direction represents one city block that takes 1 min to complete,
Return whether the walk would take 10 minutes AND get you back to your starting point.

['n','s','n','s','n','s','n','s','n','s'] should return True
['w','e','w','e','w','e','w','e','w','e','w','e'] should return False
['w'] should return False
['n','n','n','s','n','s','n','s','n','s'] should return False

"""
from typing import List


def is_valid_walk(walk: List[str]) -> bool:
    if len(walk) != 10:
        return False
    x = 0
    y = 0
    for direction in walk:
        if direction == 'n':
            y -= 1
        elif direction == 's':
            y += 1
        elif direction == 'e':
            x += 1
        else:
            x -= 1
    return (x == 0 and y == 0)


print(is_valid_walk(
    ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))  # True
print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e',
                     'w', 'e', 'w', 'e', 'w', 'e']))  # False
print(is_valid_walk(['w']))  # False
print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
