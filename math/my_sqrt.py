"""
https://leetcode.com/problems/sqrtx/
Implement sqrt(x)

Return an integer

Examples: 4 -> 2
8 -> 2
"""


class Solution:
    def mySqrt(self, x):
        return int(x**(1/2))


s = Solution()
print(s.mySqrt(16))
