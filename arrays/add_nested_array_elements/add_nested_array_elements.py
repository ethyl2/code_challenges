"""
https://github.com/Py-Lambdas/code-challenges/blob/master/200_digging_deeper/add/README.md
Write a function that accepts 2 nested lists of numbers 
and returns 1 nested list with each of the corresponding numbers in the 2 lists added together.
Only use the standard library.

Example:
>>> matrix1 = [[1, -2], [-3, 4]]
>>> matrix2 = [[2, -1], [0, -1]]
>>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]

Note: Python’s zip function allows us to loop over multiple lists at the same time:

colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for color, ratio in zip(colors, ratios):
    print("{}% {}".format(ratio * 100, color))
    
The zip function takes multiple lists 
and returns an iterable that provides a tuple of the corresponding elements of each list as we loop over it.
(source: https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/)

Also helpful on tuple unpacking: https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/

"""


def add1(arr1, arr2):
    """
    This version is hard-coded to accept 2 arrays only.
    """
    output = []
    for inner_list1, inner_list2 in zip(arr1, arr2):
        inner_output = []
        for num1, num2 in zip(inner_list1, inner_list2):
            inner_output.append(num1 + num2)
        output.append(inner_output)
    return output


def add2(arr1, arr2):
    """
    This version uses deep unpacking.
    Still hardcoded to accept only 2 arrays.
    """
    output = []
    for (num1, num2), (num3, num4) in zip(arr1, arr2):
        output.append([num1 + num3, num2 + num4])
    return output


def add3(*arrs):
    """
    This version passes the first bonus test:
    it takes any number of arrays.
    """
    output = []
    for inner_lists in zip(*arrs):
        inner_output = []
        for nums in zip(*inner_lists):
            inner_output.append(sum(nums))
        output.append(inner_output)
    return output


def add(*arrs):
    """
    This version passes the second bonus test:
    it takes any number of arrays and
    raises a ValueError if the input arrays are different shapes.
    """
    output = []
    size = len(arrs[0])
    for inner_list in arrs:
        if len(inner_list) != size:
            raise ValueError("Given matrices are not the same size.")
    for inner_lists in zip(*arrs):
        current_size = len(inner_lists[0])
        for inner_list in inner_lists:
            if len(inner_list) != current_size:
                raise ValueError("Given matrices are not the same size.")

        inner_output = []
        for nums in zip(*inner_lists):
            inner_output.append(sum(nums))
        output.append(inner_output)
    return output


if __name__ == "__main__":

    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]
    print(add(matrix1, matrix2))

    # print(add([[1, 9], [7, 3]], [[1, 2], [3]]))

    m1 = [[6, 6], [3, 1]]
    m2 = [[1, 2], [3, 4], [5, 6]]
    print(add(m1, m2))
