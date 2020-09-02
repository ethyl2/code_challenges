"""
https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python

Given an int, return the next 'integral perfect square', which is an integer n such that sqrt(n) is also an int.
If the given int is not an integral perfect square, return -1.
"""


def find_next_square(sq: int) -> int:
    sqrt_of_sq = sq ** (1/2)
    if sqrt_of_sq % 1 != 0:
        return -1
    else:
        return int((sqrt_of_sq + 1) ** 2)


def find_next_square2(sq: int) -> int:
    """
    This version is just more compact.
    """
    sqrt_of_sq = sq ** (1/2)
    return -1 if sqrt_of_sq % 1 != 0 else int((sqrt_of_sq + 1) ** 2)


def find_next_square3(sq: int) -> int:
    """
    This version uses the .is_integer() method instead of %.
    """
    sqrt_of_sq = sq ** 0.5
    return int((sqrt_of_sq+1)**2) if sqrt_of_sq.is_integer() else -1


print(find_next_square3(4))  # 9
print(find_next_square3(121))  # 144
print(find_next_square3(625))  # 676
print(find_next_square3(114))  # -1
