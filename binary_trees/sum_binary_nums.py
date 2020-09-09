"""
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3453/

Given a binary tree, in which each node as a value of 0 or 1, return the sum of adding all of the root-to-leaf path binary numbers together.

Example of binary path: 0 -> 1 -> 1 -> 0 -> 1 Represents 01101 binary, 13 decimal.

Example:
     1
   /   \
  0     1
 / \   / \
0   1  0  1

100 + 101 + 110 + 111 = 4 + 5 + 6 + 7 = 22
"""
from collections import deque
from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree_from_array(arr: List[int]) -> int:
    first_val, *rest = arr
    root = TreeNode(first_val)
    original_root = root
    left_sides_turn = True
    for i in range(1, len(rest), 2):
        left = TreeNode(arr[i])
        root.left = left
        right = TreeNode(arr[i+1])
        root.right = right

        if left_sides_turn:
            root = root.left
            left_sides_turn = False
            old_right = right
        else:
            root = old_right
            left_sides_turn = True
    return original_root


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        # base case
        if root == None:
            return []

        # setting up variables
        binary_nums = []
        q = deque()
        q.append((root, str(root.val)))

        while len(q) > 0:
            (current_node, current_string) = q.popleft()

            if not current_node.left and not current_node.right:
                # Reached a leaf
                binary_nums.append(current_string)

            if current_node.left:
                q.append((current_node.left, current_string +
                          str(current_node.left.val)))
            if current_node.right:
                q.append((current_node.right, current_string +
                          str(current_node.right.val)))
        return sum([int(num, 2) for num in binary_nums])


tree = create_binary_tree_from_array([1, 0, 1, 0, 1, 0, 1])

s = Solution()
print(s.sumRootToLeaf(tree))
