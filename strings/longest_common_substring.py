"""
From Brannan Conrad's presentation 08-08-2020
Given 2 strings, return the length of the longest substring they have in common.

Example:
"abba" & "abcd" -> 2 because "ab" is the longest substring they have in common
"""

# Make a graph to show whether the chars at corresponding characters at the same index are the same.
# If that is true, add one to the value stored at [-1][-1] from it, which represents the length of the substring in common so far before it.

"""
    A B B A
A   1 0 0 1
B   0 2 1 0
C   0 0 0 0
D   0 0 0 0
"""

# Keep track of the largest substring length as we iterate through the graph.


def lcs(s1, s2):
    grid = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
    max_length = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i-1][j-1] + 1
                max_length = max(grid[i][j], max_length)
    return max_length


print(lcs('abba', 'abcd'))
print(lcs('babba', 'abbacdabb'))

# This version returns the longest substring


def lcs2(s1, s2):
    grid = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
    max_length = 0
    index = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i-1][j-1] + 1
                if grid[i][j] > max_length:
                    max_length = grid[i][j]
                    index = i
    if max_length > 0:
        return s1[index-max_length+1:index+1]


print(lcs2('abba', 'abcd'))
