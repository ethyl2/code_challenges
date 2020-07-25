"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted arr of integers, remove the duplicates in-place and return the new length.
"It doesn't matter what values are set beyond the returned length." - makes me wonder if you
can have duplicates, but beyond the index of where all of the individual instances of the numbers are at?

Examples:

nums = [1,1,2]
modify nums to be [1,2], at least before index 2, and return length = 2

nums = [0,0,1,1,1,2,2,3,3,4]
modify nums to be [0,1,2,3,4], at least before index 5, and return length = 5

First thoughts: when a duplicate is found, it trades places with its right neighbor until it reaches the end of the array.
Stop the iteration along the arr when the element to the right of the current element is smaller.
Return i + 1 as the length.
"""

# My solution works for many of the test cases, but not the one with a really large input.


class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        while i < len(nums) - 1 and nums[i] <= nums[i+1]:
            if nums[i] == nums[i+1]:
                # send value at nums[i + 1] to the end of the arr:
                for j in range(i+2, len(nums)):
                    nums[j-1], nums[j] = nums[j], nums[j-1]
                # To get out of an endless loop when the rest of the list is the same number
                if nums.count(nums[i]) == len(nums) - i:
                    break
            else:
                i += 1
        print(nums)
        return i+1

    def removeDuplicates2(self, nums) -> int:
        swap_times = 0
        for i in reversed(range(1, len(nums)-1)):
            if nums[i] == nums[i-1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                increment_amount = 1

                for j in range(swap_times):
                    nums[i+increment_amount], nums[i + increment_amount +
                                                   1] = nums[i + increment_amount + 1], nums[i+increment_amount]
                    increment_amount += 1

                swap_times += 1
        print(nums)
        length = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                length += 1
            else:
                break
        return length


s = Solution()
# print(s.removeDuplicates2([1, 1, 2]))
# print(s.removeDuplicates2([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
# print(s.removeDuplicates([1, 1]))
# print(s.removeDuplicates([1, 1, 1]))
# print(s.removeDuplicates([1, 2, 2]))
# print(s.removeDuplicates([1, 2, 2, 2]))
print(s.removeDuplicates([1, 1, 2, 3]))
'''
for i in reversed(range(1, 4)):
    print(i)
'''
