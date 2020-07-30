"""
https://leetcode.com/problems/next-permutation/

From Andrew Candela's lecture 07-30-2020
Given an array of integers, return the next largest permutation of those ints.
If not possible, return the smallest permutation of those ints.

Must do it in-place with space O(1).
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

Approach to try:
Interate from right to left and
Find the first int that is larger, not smaller, than the int before it.
Its index will be the pivot index.
If no index if found, return the reversed list.

Then find the smallest possible int that we can swap with, and do the swap.

Finally, reverse the sublist right of the pivot.
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pivot_index = self.find_pivot(nums)
        print('pivot_index: ', pivot_index)
        if pivot_index == -1:
            nums.reverse()
            print('pivot index was -1')
            print(nums)
            return
        self.swap_pivot(pivot_index, nums)
        print('after swap_pivot')
        print(nums)
        self.reverse_remaining_slice(pivot_index, nums)
        print('at end')
        print(nums)

    def find_pivot(self, nums: List[int]) -> int:
        for i in reversed(range(1, len(nums))):
            print('at index: ', i, ' at value: ', nums[i])  # 132
            if nums[i] > nums[i-1]:
                print('found pivot')
                return i-1
        return -1

    def swap_pivot(self, pivot_index: int, nums: List[int]) -> None:
        for i in range(len(nums) - 1, pivot_index, -1):
            if nums[i] > nums[pivot_index]:
                nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
                return

    def reverse_remaining_slice(self, pivot_index: int, nums: List[int]) -> None:
        for i in range(len(nums) - 1, pivot_index, -1):
            # print('at index: ', i)
            swap_num = nums.pop(i)
            nums.append(swap_num)


def test_range(nums):
    for i in reversed(range(1, len(nums))):
        print(i)


s = Solution()
# print(s.nextPermutation([1, 2, 3]))  # 1,3,2
# print(s.nextPermutation([3, 2, 1]))  # 1,2,3
# print(s.nextPermutation([1, 1, 5])) # 1,5,1
# print(s.nextPermutation([6, 8, 4, 5, 3, 2]))
# print(s.nextPermutation([1]))
# print(s.nextPermutation([1, 1]))
print(s.nextPermutation([1, 3, 2]))  # -> [2,1,3]
# test_range([1, 3, 2])
