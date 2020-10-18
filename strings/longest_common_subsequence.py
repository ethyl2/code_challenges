"""
https://leetcode.com/problems/longest-common-subsequence/

Given 2 strings text1 & text2, return the length of their longest common subsequence.
A subsequence is a new string that has 0 or more chars deleted without changing the relative order of the remaining chars.

Examples:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

My strategy:
Create a graph of matches.
Traverse the graph to count the number of matches,
    incrementing the col start index for each row by 1, to make sure the matches happen in order.

    a b c
a   1 0 0
b   - 1 0
c   - - 1

total: 3

    a b c
a   1 0 0
c   - 0 1
b   - - 0

total: 2

b has a match in the one above, but it is out of order, so don't count it
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        grid = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        for line in grid:
            print(line)

        count = 0
        index = 0

        for i in range(len(text1)):
            for j in range(index, len(text2)):
                if text1[i] == text2[j]:
                    '''
                    count += 1
                    grid[i][j] = count
                    print(text1[i])
                    '''
                    largest_prev_count = 0
                    for k in range(j):
                        # TBD
                    index += 1
        print('count: ', count)

        for line2 in grid:
            print(line2)
        return count

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1

        count = 0
        index = 0

        for i in range(len(text1)):
            for j in range(index, len(text2)):
                if text1[i] == text2[j]:

                    count += 1
            index += 1
        return count


s = Solution()
# print(s.longestCommonSubsequence('ab', 'ab'))
# print(s.longestCommonSubsequence('abc', 'abc'))
# print(s.longestCommonSubsequence2('abc', 'acb'))
# print(s.longestCommonSubsequence('abc', 'a'))
# print(s.longestCommonSubsequence("abcde", 'ace'))
# print(s.longestCommonSubsequence("ace", 'abcde'))
print(s.longestCommonSubsequence("ezupkr",
                                 "ubmrapg"))
