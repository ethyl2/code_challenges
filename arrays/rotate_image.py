"""
https://app.codesignal.com/interview-practice/task/5A8jwLGcEpTPyyjTB

Given n x n 2D matrix.
Rotate by 90 deg clockwise.
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
return
 [[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
"""


def rotate_image(a):
    # Initialize new arr
    new_a = [[]] * len(a)
    # print(new_a)
    # Nested Loop

    for i in range(len(a)):
        current_index = 0
        for j in range(len(a[0])):

            # print(a[i][j])
            current_num = a[i][j]
            # print(new_a[current_index])
            # new_a[current_index].insert(0, current_num)
            new_subset = new_a[current_index].copy()
            new_subset.insert(0, current_num)
            new_a[current_index] = new_subset
            # print(new_a)
            current_index = (current_index + 1) % len(a[0])
            # print(current_index)
    print(new_a)
    return(new_a)


rotate_image([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

'''
test = [[]] * 3
print([[]] * 3)

new_subset = test[0].copy()
new_subset.insert(0, 5)
test[0] = new_subset
print(test)
'''
