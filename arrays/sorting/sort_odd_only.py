"""
https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
Given an array of ints,
return the array where all of the odd nums are sorted, but even numbers are in their original places.
Keep 0 in its place.

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

My approach is in-place, where the returned array is the same array as the input array. Space complexity 0(1)
Time O(n)

After submitting my solution, other solutions were displayed that are more concise, but have added space complexity.
They are not done in-place. Scroll down for my implementation that is similar to those.
"""
from typing import List


def sort_array_with_print_statements(source_array: List[int]) -> List[int]:
    made_switch = True
    last_odd_index = None
    while made_switch == True:
        made_switch = False
        for i in range(len(source_array)):

            if source_array[i] % 2 == 1:
                # if not last_odd_index:
                if not type(last_odd_index) == int:

                    last_odd_index = i
                    print('no last_odd_index, so now it is ', last_odd_index)

                print('comparing source_array[i]: ', source_array[i],
                      ' with source_array[last_odd_index]: ', source_array[last_odd_index], ' at index ', last_odd_index)
                if source_array[i] < source_array[last_odd_index]:
                    print('found nums to switch: ',
                          source_array[i], source_array[last_odd_index])
                    source_array[i], source_array[last_odd_index] = source_array[last_odd_index], source_array[i]
                    made_switch = True

                last_odd_index = i
                print(source_array)
                print('now last_odd_index is ', last_odd_index)
        last_odd_index = None

    return source_array


def sort_array(source_array: List[int]) -> List[int]:
    made_switch = True
    last_odd_index = None
    while made_switch == True:
        made_switch = False
        for i in range(len(source_array)):
            if source_array[i] % 2 == 1:
                if not type(last_odd_index) == int:
                    last_odd_index = i
                if source_array[i] < source_array[last_odd_index]:
                    source_array[i], source_array[last_odd_index] = source_array[last_odd_index], source_array[i]
                    made_switch = True
                last_odd_index = i
        last_odd_index = None
    return source_array


def sort_array_concise(source_array: List[int]) -> List[int]:
    odds = sorted([num for num in source_array if num % 2 == 1], reverse=True)
    return [num if num % 2 == 0 else odds.pop() for num in source_array]


# print(sort_array([5, 3, 2, 8, 1, 4]))
result = sort_array([1, 111, 11, 11, 2, 1, 5, 0])
print(result)
print(result == [1, 1, 5, 11, 2, 11, 111, 0])

result2 = sort_array_concise([1, 111, 11, 11, 2, 1, 5, 0])
print(result2)
print(result2 == [1, 1, 5, 11, 2, 11, 111, 0])
