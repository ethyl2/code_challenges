"""
https://www.codewars.com/kata/558fc85d8fd1938afb000014
Given an array of at least 4 positive ints, reutrn the sum of the lowest 2.

Example:
[19, 5, 42, 2, 77], the output should be 7.
"""
from typing import List


def sum_two_smallest_numbers(numbers: List[int]) -> int:
    '''
    First approach. Not the most efficient, time-wise, b/c of sorting. O(n log n).
    Space O(n) b/c I used sorted(), which makes a copy.
    But look, it's all in one line! :-)
    '''
    return sum(sorted(numbers)[:2])


def sum_two_smallest_numbers2(numbers: List[int]) -> int:
    '''
    Second approach. Not the most efficient, time-wise, b/c of sorting. O(n log n).
    Space O(1) b/c I used sort(), which sorts in place. And the substring used is always of length 2.
    '''
    numbers.sort()
    return sum(numbers[:2])


def sum_two_smallest_numbers3(numbers: List[int]) -> int:
    '''
    Third approach. More efficient, time-wise, b/c it doesn't use sorting. O(n).
    Space O(1).
    '''
    smallest, smaller = min(numbers[:2]), max(numbers[:2])

    for i in range(2, len(numbers) - 1):
        if numbers[i] < smallest:
            smaller = smallest
            smallest = numbers[i]
        elif numbers[i] < smaller:
            smaller = numbers[i]
    return sum([smaller, smallest])


print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))
print(sum_two_smallest_numbers2([19, 5, 42, 2, 77]))
print(sum_two_smallest_numbers3([19, 5, 42, 2, 77]))

print(sum_two_smallest_numbers3([5, 8, 12, 18, 22]))  # 13
print(sum_two_smallest_numbers3([7, 15, 12, 18, 22]))  # 19
print(sum_two_smallest_numbers3([25, 42, 12, 18, 22]))  # 30
