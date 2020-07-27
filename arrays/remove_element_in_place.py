"""
https://leetcode.com/problems/remove-element/
Given an array nums and value val, 'remove all instances of val' =
stick all instances of val at the end of the array and
return the length of the arr that doesn't include the instances of val
"""


class Solution:
    def removeElement(self, nums, val: int) -> int:
        # Edge case of empty arr
        if len(nums) < 1:
            return 0

        # Another edge case where ALL the elements are val, so instead of
        #   switching elements around, we just delete them all.
        if nums.count(val) == len(nums):
            nums = []
            return 0

        # Initialize a counter.
        # Initialize 2 pointers:
        # Left and right
        # When left points to a val, swap what's at left and right, increment the counter, and then decrement right
        # Otherwise, increment left
        # Stop when left and right cross.
        # Return len(nums) - count
        counter = 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                counter += 1
                right -= 1
            else:
                left += 1
        print(nums)

        return len(nums) - counter


s = Solution()
# print(s.removeElement([3, 2, 2, 3], 3))  # 2
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))  # 5
# print(s.removeElement([1], 1))
# print(s.removeElement([4, 5], 5))
