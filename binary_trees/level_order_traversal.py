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

My approach:
First, make a function to that takes a list and converts it into a binary tree. (For local testing purposes)
Then make the function that takes a binary tree and returns the nested array of its levels.

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
        '''
        I chose a deque object as my queue,
        because "Deques support thread-safe, memory efficient appends and 
        pops from either side of the deque with approximately the same O(1) performance in either direction."
        '''
        # Edge case
        if not root:
            return []

        # Set up variables
        output = [[]]
        q = deque()
        level = 0
        q.append((root, level))

        while len(q) > 0:
            current_node, node_level = q.popleft()
            if node_level > level:
                output.append([])
                level = node_level
            output[-1].append(current_node.val)
            if current_node.left:
                q.append((current_node.left, node_level + 1))
            if current_node.right:
                q.append((current_node.right, node_level + 1))
        return output


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
s = Solution()
print(s.levelOrder(tree))
