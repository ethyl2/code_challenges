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
    # My first approach. I was thinking that the .index() built-in function
    # might be more efficient than something I'd implement, so it would be worth
    # doing first, but it looks like .index() is just O(n). So this version is O(2n) -> O(n)
    def searchInsert(self, nums, target: int) -> int:
        try:
            search_result = nums.index(target)
            return search_result
        except:
            output_index = 0
            for i, num in enumerate(nums):
                if num > target:
                    return i
            return i+1

    # This second approach is little bit better, efficiency-wise. It only goes through nums 1 time. O(n)
    def searchInsert2(self, nums, target: int) -> int:
        for i, num in enumerate(nums):
            if num == target or num > target:
                return i
        return i+1

    # This third version should be the most time efficient of the 3 versions. It uses a binary search, so the
    # ave run time is Θ(log(n)). Worst case is still O(n).
    def searchInsert3(self, nums, target: int) -> int:
        left = 0
        right = len(nums)
        mid = (left + right) // 2
        while left < right:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
            mid = (left + right) // 2
        return mid


s = Solution()
# print(s.searchInsert3([1, 3, 5, 6], 5))  # 2
# print(s.searchInsert3([1, 3, 5, 6], 2))
# print(s.searchInsert3([1, 3, 5, 6], 7))
print(s.searchInsert3([1, 3, 5, 6], 0))
