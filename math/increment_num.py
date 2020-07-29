"""
https://leetcode.com/problems/plus-one/

Given a non-empty arr of digits representing a non-neg int, increment that int by 1.
Most significant digit is at the head of the list.
Each el contains a single digit.
The int doesn't contain leading zeros, except for the int 0 itself.

examples:
[1,2,3] -> [1,2,4]
[4,3,2,1] -> [4,3,2,2]
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        return int(''.join(map(str, digits)))


s = Solution()
print(s.plusOne([1, 2, 3]))
print(s.plusOne([4, 3, 2, 1]))
