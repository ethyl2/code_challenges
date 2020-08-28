"""
https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

Given a list of non-negative ints and strings, returna new list with strings filtered out.

filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""

from typing import List


def filter_list(l: List[int or str]):
    return [element for element in l if type(element) == int]


print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1, 2, 'a', 'b']) == [1, 2])

print(filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15])
print(filter_list([1, 'a', 'b', 0, 15]))
print(filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123])
print(filter_list([1, 2, 'aasf', '1', '123', 123]))
