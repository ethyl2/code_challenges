"""
https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python

Given a volume m, return how many cubes you need to use to get to that volume.
The cube at the bottom will have a volume of n^3, the cube above will have the volume of (n-1)^3, etc until the top
which will have volume of 1^3.
Return -1 if n doesn't exist.

find_nb(1071225) -> 45
find_nb(91716553919377) -> -1

My approach: think of it upside down. start with the 1^3 layer 
and build until the current volume is m (in which case, return n), or exceeds m (return -1).
"""


def find_nb(m):
    current_volume = 0
    n = 1
    while current_volume < m:
        current_volume += n**3
        if current_volume == m:
            return n
        n += 1

    return -1


print(find_nb(1071225))  # 45
print(find_nb(4183059834009))  # 2022
print(find_nb(24723578342962))  # -1
