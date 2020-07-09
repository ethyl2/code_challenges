"""
https://leetcode.com/problems/search-a-2d-matrix-ii/

Given an m x n matrix in which integers are sorted small -> large from left to right and top to bottom.
Return true if given value is found. False otherwise.
Write an efficient algorithm.

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.

My plan: If there's an optimal way to pick which inner array to start with, use that.
(Tricky to figure out b/c the flattened array would not be sorted.)
Otherwise, start at first inner array.
If target is not in that array, continue through arrays until inner_array[0] > target.
    Actually, if inner_array[0], return true
    and then if inner_array[0] < target, continue checking rest of array. --> Most optimally, with a binary search.
 
"""
a = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # edge cases
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row = 0
        while row < len(matrix) and matrix[row][0] <= target:

            if matrix[row][0] == target:
                return True
            in_row = binary_search(matrix[row], target)
            if in_row:
                return True
            row += 1

        return False


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    mid = len(arr) // 2
    while left <= right:
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            right = mid - 1
            mid = (right - left) // 2
        else:
            left = mid + 1
            mid = 1 + mid + (right - left) // 2
    return False


s = Solution()

print(s.searchMatrix(a, 5))  # True
print(s.searchMatrix(a, 20))  # False
print(s.searchMatrix([], 0))  # False
print(s.searchMatrix([[-5]], -5))  # True
print(s.searchMatrix([[-1, 3]], 3))  # True

print(s.searchMatrix([[-5]], -2))  # False
print(s.searchMatrix([[5], [6]], 6))  # True
