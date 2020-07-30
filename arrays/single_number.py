"""
https://leetcode.com/problems/single-number/
Given a non-empty array of integers, every element appears twice except for one. Find the single one.

Examples:
[2,2,1] -> 1
[4,1,2,1,2] -> 4

Notes: Runtime should be linear.
Can you implement it w/o using extra mem?
"""
from typing import List


class Solution:
    # 1st approach would create a look-up dictionary
    def singleNumber(self, nums: List[int]) -> int:
        lookup = dict()
        for num in nums:
            if num in lookup:
                lookup[num] += 1
            else:
                lookup[num] = 1
        return [num for num, key in lookup.items() if key == 1][0]

    # 2nd approach sorts and then looks to see if neighbor is the same.
    # O(n log n) time and O(1) space.
    def singleNumber2(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
        # If it hasn't returned by now, the single element must be at the end
        return nums[i]


s = Solution()
print(s.singleNumber2([2, 2, 1]))
print(s.singleNumber2([4, 1, 2, 1, 2]))
