"""
Add up and print the sum of the all of the minimum elements of each inner array:
[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
The expected output is given by:
4 + -1 + 9 + -56 + 201 + 18 = 175
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""


def sum_min_inners(arr):
    return sum([min(inner) for inner in arr])
    '''
    total = 0
    for inner in arr:
        total += min(inner)
    return total
    '''


'''
print(sum_min_inners([[8, 4], [90, -1, 3], [9, 62],
                      [-7, -1, -56, -6], [201], [76, 18]]))
'''
"""
Stretch:
Add up and print the sum of the all of the minimum elements of each inner array. 
Each array may contain additional arrays nested arbitrarily deep, 
in which case the minimum value for the nested array should be added to the total.
[
  [8, [4]],  # 8 # 4
  [[90, 91], -1, 3],  # 90 # -1
  [9, 62], # 9
  [[-7, -1, [-56, [-6]]]], #-7 # -56 # -6
  [201],  #201
  [[76, 0], 18], #0 #18
]
The expected output for the above input is:
8 + 4 + 90 + -1 + 9 + -7 + -56 + -6 + 201 + 0 + 18 = 260
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""


def sum_min_nested(arr):
    # Check to make sure that arr is not a nested arr
    values = []
    total = 0
    for item in arr:
        if type(item) == list:
            total += find_min(item)
        else:
            values.append(item)

    return total + sum(values)


def find_min(arr):
    values = []
    for item in arr:
        if type(item) == list:
            value = find_min(item)
        else:
            value = item
        values.append(value)
    return min(values)


print(sum_min_nested([
    [8, [4]],
    [[90, 91], -1, 3],
    [9, 62],
    [[-7, -1, [-56, [-6]]]],
    [201],
    [[76, 0], 18],
]))
