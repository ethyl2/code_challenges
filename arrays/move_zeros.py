"""
https://www.codewars.com/kata/52597aa56021e91c93000cb0/python
Given an array (probably with different types of values inside), move all of the zeros to the end,
keeping the order of the rest.

Example: 
move_zeros([false,1,0,1,2,0,1,3,"a"])

# returns[false,1,1,2,1,3,"a",0,0]
"""


def move_zeros(array):
    num_zeros = 0
    output = []
    for item in array:
        if item == False and type(item) == bool:
            output.append(False)
        elif item == 0:
            num_zeros += 1
        else:
            output.append(item)
    output.extend([0] * num_zeros)
    return(output)

# My 2nd approach, in-place:


def move_zeros2(array):
    stop = len(array) - 1
    pointer = 0
    while pointer < stop:
        if array[pointer] == False and type(array[pointer]) == bool:
            pointer += 1
        elif array[pointer] == 0:
            array.append(0)
            del array[pointer]
            stop -= 1
        else:
            pointer += 1
    return array


def move_zeros3(arr):
    l = [i for i in arr if isinstance(i, bool) or i != 0]
    return l+[0]*(len(arr)-len(l))


print(move_zeros2([False, 1, 0, 1, 2, 0, 1, 3, "a"]))
