"""
https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python

Given a positive int n_floors, return an array of strings that represent a tower of n_floors floors.
The top tower is '*' with the appropriate spacing and each floor following increases the number of *s by 2.

Example: n_floors = 3
[
  '  *  ',
  ' *** ',
  '*****'
]

n_floors = 6
[
  '     *     ',
  '    ***    ',
  '   *****   ',
  '  *******  ',
  ' ********* ',
  '***********'
]
"""
from typing import List


def tower_builder(n_floors: int) -> List[str]:
    num_stars = []
    stars = 1
    for i in range(n_floors):
        num_stars.append(stars)
        stars += 2
    max_stars = num_stars[-1]
    output = []
    for num in num_stars:
        output.append(('*' * num).center(max_stars))
    for line in output:
        print(line)
    return output


def tower_builder2(n_floors: int) -> List[str]:
    max_stars = (n_floors*2) - 1
    output = []
    for i in range(1, n_floors + 1):
        output.append(('*' * (i * 2 - 1)).center(max_stars))

    for line in output:
        print(line)
    return output


print(tower_builder2(3))
print(tower_builder2(8))
