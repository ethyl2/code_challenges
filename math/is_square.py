"""
https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
Given an int, return whether it is a 'square number' = it is the product of some integer with itself

Examples:
-1 -> False
0 -> True
3 -> False
4 -> True
"""
import math

# My first version


def is_square(n: int) -> bool:
    if n < 0:
        return False
    return math.sqrt(n) == int(math.sqrt(n))

# My second, more condensed version


def is_square2(n: int) -> bool:
    return math.sqrt(n) == int(math.sqrt(n)) if n >= 0 else False

# Another person's version. I like how it doesn't need to import math. Uses n**0.5 instead. And uses modulo.


def is_square3(n: int) -> bool:
    return n >= 0 and (n**0.5) % 1 == 0


print(is_square(3))
print(is_square(4))
print(is_square(0))
