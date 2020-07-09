"""
https://app.codesignal.com/interview-practice/task/SKZ45AF99NpbnvgTn/description

Given 9 x 9 grid
Each char is either a digit '1' to '9' or a period '.'
Check whether each col,
each row,
each of 9 3x3 subgrids 
ALL contain all of the nums 1-9 once. -> Looks like all numbers do not have to be there, but can't have duplicates.
Note: the puzzle represented by grid does not have to be solvable.

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
return True

grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
return False b/c 2 1s in 2nd col.
"""


def sudoku2(grid):
    # First, check rows by making a lookup set during each row iteration.
    # Also, check the col arrays for duplicates, too.
    # Make a lookup dict.
    # If value of lookup dict is already 1, return False
    col_sets = {}
    for i in range(len(grid)):
        row_set = set()

        for j in range(len(grid[i])):
            val = grid[i][j]
            # Check the row
            if val in row_set and val != '.':
                return False
            else:
                row_set.add(val)
                # Now, check the current column
                if j not in col_sets:
                    col_sets[j] = set(val)
                else:
                    if val in col_sets[j] and val != '.':
                        return False
                    else:
                        col_sets[j].add(val)
    print(col_sets)
    subgrid_check = check_subgrids(grid)
    if not subgrid_check:
        return False
    return True

    # Finally, check subgrids


def check_subgrids(grid):
    subgrid_starts = [[0, 0], [3, 0], [6, 0],  # y,x
                      [0, 3], [3, 3], [6, 3],
                      [0, 6], [3, 6], [6, 6]]
    # Loop through subgrids
    for i in range(len(subgrid_starts)):
        subgrid_start = subgrid_starts[i]
        print(grid[subgrid_start[1]][subgrid_start[0]])
        subgrid_set = set()
        for j in range(3):
            for k in range(3):
                val = grid[subgrid_start[1] + j][subgrid_start[0] + k]
                if val in subgrid_set and val != '.':
                    # print("found duplicate")
                    return False
                else:
                    subgrid_set.add(val)
    return True


grid1 = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
         ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
         ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
         ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
         ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
         ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
         ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

# print(sudoku2(grid1))

grid3 = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
         ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
         ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
         ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
         ['.', '3', '.', '.', '.', '.', '.', '7', '6'],
         ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
         ['.', '.', '.', '5', '.', '.', '.', '.', '7']]
# check_subgrids(grid3)
print(sudoku2(grid3))

grid2 = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
         ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
         ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
         ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
         ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
         ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
         ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
         ['.', '2', '.', '.', '3', '.', '.', '.', '.']]

# print(sudoku2(grid2))
