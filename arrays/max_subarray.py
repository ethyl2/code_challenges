"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Notes: After finishing a O(n) approach, implement a divide-and-conquer approach, 'which is more subtle'.

"""


class Solution:
    def maxSubArray(self, nums) -> int:
        """
        Hurray! This version passes all of the leetcode test cases!
        """
        current_total = nums[0]
        lowest_index = 0
        winner = nums[0]
        # Iterate along nums. Add the num to the current_total. If the current_total gets below 0, reset.
        #   Also see if taking off the lowest index of the subarray increases the current_total. If so, do it.
        # for i, num in enumerate(nums):
        for i in range(1, len(nums)):
            current_total += nums[i]
            if current_total - nums[lowest_index] > current_total:
                current_total -= nums[lowest_index]
                lowest_index += 1
            if current_total < 0:
                current_total = nums[i]
                lowest_index = i
            if current_total > winner:
                winner = current_total

        return winner

    def maxSubArray2(self, nums) -> int:
        """
        Brute force approach, just to get something working first.
        O(n^2) time
        https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
        This version states that you should return 0 if the list is empty or has all negative numbers.
        """
        if len(nums) == 0:
            return 0

        all_negs = True
        for num in nums:
            if num >= 0:
                all_negs = False
        if all_negs:
            return 0

        current_winner = nums[0]
        for i in range(1, len(nums)):
            for j in range(len(nums)-1):
                current_total = sum(nums[j:j+i])
                if current_total > current_winner:
                    current_winner = current_total

        return max(current_winner, sum(nums))

    def maxSubArray3(self, nums):
        """
        Here's someone else's solution. Interesting how the reset works! Whenever the current sum dips below zero, start over
        accumulating the sum. Otherwise, keep going.
        """
        max, curr = 0, 0
        for x in nums:
            curr += x
            if curr < 0:
                curr = 0
            if curr > max:
                max = curr
        return max


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray([1]))
print(s.maxSubArray([-2, 1]))  # 1
print(s.maxSubArray([-2, -1]))  # -1
# print(s.maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(s.maxSubArray2([]) == 0)
'''
print(s.maxSubArray2([7, 4, 11, -11, 39, 36, 10, -
                      6, 37, -10, -32, 44, -26, -34, 43, 43]))  # 155

print(s.maxSubArray3([7, 4, 11, -11, 39, 36, 10, -
                      6, 37, -10, -32, 44, -26, -34, 43, 43]))  # 155
'''
