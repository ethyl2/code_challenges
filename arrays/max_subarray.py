"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Notes: After finishing a O(n) approach, implement a divide-and-conquer approach, 'which is more subtle'.

To be continued...
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        current_total = nums[0]
        lowest_index = 0
        # Iterate along nums. See if adding current num increases the current_total. If so, add it.
        #   Also see if taking off the lowest index of the subarray increases the current_total. If so, do it.
        for i, num in enumerate(nums):
            if current_total + num > current_total:
                current_total += 1
            if current_total - nums[lowest_index] > current_total:
                current_total -= nums[lowest_index]
                lowest_index += 1
            print(current_total)
            print(nums[lowest_index:i])
        return current_total


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
