"""
https://www.codewars.com/kata/55f2b110f61eb01779000053

Given 2 ints, not ordered, can be pos or neg.
Return the sum of all nums between them, including them.
If the 2 nums are the same, return one of them.

Examples:
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
"""


def get_sum(a: int, b: int) -> int:
    if a == b:
        return a
    small = min(a, b)
    large = max(a, b)
    return sum([i for i in range(small, large+1)])


def get_sum2(a: int, b: int) -> int:
    """
    My second version, that is just a more concise version of the first one.
    """
    return a if a == b else sum([i for i in range(min(a, b), max(a, b)+1)])


def get_sum3(a: int, b: int) -> int:
    """
    My third version, that is just an even more concise version of the first one.
    """
    return sum([i for i in range(min(a, b), max(a, b)+1)])


print(get_sum3(1, 0))
