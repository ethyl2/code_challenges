"""
https://www.codewars.com/kata/54e6533c92449cc251001667

Given a sequence: a string or a list, 
return a list in which only one instance is present of repeated elements next to each other.

Examples: 
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""
from typing import List


def unique_in_order(iterable: str or List):
    output = [iterable[0]]
    for i in range(1, len(iterable)):
        if iterable[i] != iterable[i-1]:
            output.append(iterable[i])
    return output


def unique_in_order2(iterable: str or List):
    if len(iterable) == 0:
        return []
    output = [iterable[0]]
    output.extend([iterable[i] for i in range(1, len(iterable))
                   if iterable[i] != iterable[i-1]])
    return output


print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))

print(unique_in_order2('AAAABBBCCDAABBB'))
print(unique_in_order2('ABBCcAD'))
print(unique_in_order2([1, 2, 2, 3, 3]))
