"""
https://www.codewars.com/kata/58ca658cc0d6401f2700045f/train/python
Given 2 ints. Return a list of mults of int1, named integer, up to int2 called limit.
If limit is a mult of int1, it should be included.

Both ints are positive, >0. Limit > int1.

Try to do it in 1 loc.

Examples:
find_multiples(5, 25) -> [5, 10, 15, 20, 25]
find_multiples(1, 2) ->  [1, 2]
find_multiples(2,6) -> [2,4,6]
"""

# Mine


def find_multiples(integer, limit):
    return [integer*i for i in range(1, (limit//integer) + 1)]

# Another person's:


def find_multiples2(integer, limit):
    return list(range(integer, limit + 1, integer))


print(find_multiples2(5, 25))
print(find_multiples2(1, 2))
print(find_multiples2(2, 6))
print(find_multiples2(3, 17))  # [3,6,9,12,15]
