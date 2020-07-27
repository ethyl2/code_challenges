"""
https://leetcode.com/problems/search-insert-position/
Given a sorted arr and a target val, if the target is found, return index; otherwise, return
the index where it would be inserted.
Input: [1,3,5,6], 5
Output: 2

Input: [1,3,5,6], 2
Output: 1

Input: [1,3,5,6], 7
Output: 4

Input: [1,3,5,6], 0
Output: 0
"""


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        try:
            search_result = nums.index(target)
            return search_result
        except:

            output_index = 0
            for i, num in enumerate(nums):
                if num >= target:
                    return i
            return i+1


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))  # 2
print(s.searchInsert([1, 3, 5, 6], 2))
print(s.searchInsert([1, 3, 5, 6], 7))
print(s.searchInsert([1, 3, 5, 6], 0))
