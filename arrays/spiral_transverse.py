"""
From algo expert 08-14-2020

Given a n x m 2-dimensional array (rectangle or square-shaped), 
return a 1-dimensional array of its elements in spiral order.

Spiral order: Top left to the right, then down, then across from right to left, then up. Until every element has been visited.

Example:
    array = [
        [ 1,  2,  3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10,  9,  8, 7]
    ]

    output: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

Strategy:
    Think of this reversely, where you start at the outer ring.
    Then do the same thing for each inner ring, one layer at a time.

    Use 4 pointers to indicate the starting_row, starting_col, ending_row, and ending_col. Increment/decrement them each time, according to 
        how to get the ring smaller each time.
    Then traverse the ring, careful not to repeat elements as you change directions. 
    End the loop when the pointers cross.
"""
from typing import List


def spiral_traverse(arr: List) -> List:
    output = []
    sr = 0
    sc = 0
    er = len(arr) - 1
    ec = len(arr[0]) - 1

    while sr < er and sc < ec:

        # going across the top
        output.extend(arr[sr][sc:ec+1])

        # going down
        for i in range(1, er - sr + 1):
            output.append(arr[sr+i][ec])

        # going across the bottom
        for i in range(1, ec-sc+1):
            output.append(arr[er][ec-i])

        # going back up
        for i in range(2, er-sr+1):
            output.append(arr[sr-i][sc])

        # update the pointers
        sc += 1
        ec -= 1
        sr += 1
        er -= 1

    return(output)


'''
print(spiral_traverse([
    [1,  2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7]
]))
print(spiral_traverse([[1, 2], [4, 3]]))
print(spiral_traverse([[1, 2, 3], [6, 5, 4]]))
'''
print(spiral_traverse([
    [1, 2, 3, 4, 5, 6],
    [16, 17, 18, 19, 20, 7],
    [15, 24, 23, 22, 21, 8],
    [14, 13, 12, 11, 10, 9]]))

# Recursive version. Passes all tests I've made, except for one. TODO: figure out why!


def recursive_spiral_traverse(arr: List, sc: int = 0, ec: int = None, sr: int = 0, er: int = None, output=None):
    if output == None:
        output = []
    if ec == None:
        ec = len(arr[0]) - 1
    if er == None:
        er = len(arr) - 1

    # base case
    if sr >= er and sc >= ec:
        return output

    # going across the top
    output.extend(arr[sr][sc:ec+1])

    # going down
    for i in range(1, er - sr + 1):
        output.append(arr[sr+i][ec])

    # going across the bottom
    for i in range(1, ec-sc+1):
        output.append(arr[er][ec-i])

    # going back up
    for i in range(2, er-sr+1):
        output.append(arr[sr-i][sc])

    return recursive_spiral_traverse(arr, sc+1, ec-1, sr+1, er-1, output)


'''
print(recursive_spiral_traverse([[1, 2], [4, 3]]))
print(recursive_spiral_traverse([
    [1,  2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7]
]))

print(recursive_spiral_traverse([[1, 2, 3], [6, 5, 4]]))
print(recursive_spiral_traverse([
    [1, 2, 3, 4, 5, 6],
    [16, 17, 18, 19, 20, 7],
    [15, 24, 23, 22, 21, 8],
    [14, 13, 12, 11, 10, 9]]))
'''
