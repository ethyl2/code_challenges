"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given a binary tree, return the level order of its nodes' values (i.e., from L to R, level by level)

Example:
binary tree: [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
Return 
[
  [3],
  [9,20],
  [15,7]
]
"""
from collections import deque
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        """
        My method to add a node to this binary tree.
        Note that this is not a BST, so slots are just filled in from left to right, one level at a time.
        TODO: Add handling for when the val is None, to not allow the subsequent insert to replace the node with value None.
        """

        """
        # For reference, this is code for inserting into a BST:
        if val < self.val:
            if not self.left:
                self.left = TreeNode(val)
            else:
                self.left = self.left.insert(val)
        else:
            if not self.right:
                self.right = TreeNode(val)
            else:
                self.right = self.right.insert(val)
        """
        if not self.left:
            self.left = TreeNode(val)
        elif not self.right:
            self.right = TreeNode(val)
        elif not self.left.left:
            self.left = self.left.insert(val)
        else:
            self.right = self.right.insert(val)


def create_binary_tree_from_array(arr: List[int]) -> int:
    first_val, *rest = arr
    root = TreeNode(first_val)
    original_root = root
    left_sides_turn = True
    for i in range(1, len(rest), 2):
        # print('root: ', root.val)
        left = TreeNode(arr[i])
        root.left = left
        right = TreeNode(arr[i+1])
        root.right = right

        # print(root.left.val, ' ', root.right.val)
        if left_sides_turn:
            root = root.left
            # print('new root: ', root.val)
            left_sides_turn = False
            old_right = right
        else:
            root = old_right
            # print('new root: ', root.val)
            left_sides_turn = True
    return original_root


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        pass


'''
root = TreeNode(3)
root.insert(9)
root.insert(20)
print(root.left.val)
print(root.right.val)
'''
tree = create_binary_tree_from_array([3, 9, 20, None, None, 15, 7])
print(tree.val)
print(tree.left.val)
