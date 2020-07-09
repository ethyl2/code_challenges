"""
https://leetcode.com/problems/wildcard-matching/

From Sean Chen Lecture 07-08-2020

Given: input string s
pattern p
Return boolean to should whether s matches p, with the matching covering the entire s (not partial)
'?' matches any single char, but not an empty string
'*' matches any sequence of chars, including an empty string
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return False


solution = Solution()
print(solution.isMatch('aa', 'a'))
