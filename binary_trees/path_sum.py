"""
https://leetcode.com/problems/path-sum-ii/

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

My results:
Runtime: 52 ms, faster than 52.94% of Python3 online submissions for Path Sum II.
Memory Usage: 15.1 MB, less than 77.73% of Python3 online submissions for Path Sum II.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        # Edge cases
        if not root:
            return []

        # Setting up variables
        q = deque()
        q.append((root, [root.val], root.val))
        output = []

        # tree traversal
        while len(q) > 0:
            # Using destructuring to label what comes off from popping
            curr_node, curr_path, curr_total = q.popleft()

            # If at a leaf node, check to see if the sums are equal
            if curr_total == sum and not curr_node.right and not curr_node.left:
                output.append(curr_path)

            # Add the right and left nodes to the stack
            if curr_node.right:
                path_copy = curr_path[:]
                path_copy.append(curr_node.right.val)
                q.append((curr_node.right, path_copy,
                          curr_total + curr_node.right.val))

            if curr_node.left:
                path_copy = curr_path[:]
                path_copy.append(curr_node.left.val)
                q.append((curr_node.left, path_copy,
                          curr_total + curr_node.left.val))

        return output

    def pathSum2(self, root: TreeNode, sum: int) -> List[List[int]]:
        # Edge cases
        if not root:
            return []

        # Setting up variables
        q = deque()
        q.append((root, [root.val]))
        output = []

        # tree traversal
        while len(q) > 0:
            # Using destructuring to label what comes off from popping
            curr_node, curr_path = q.popleft()

            # If at a leaf node, check to see if the sums are equal
            if not curr_node.right and not curr_node.left and sum(curr_path) == sum:
                output.append(curr_path)

            # Add the right and left nodes to the stack
            if curr_node.right:
                path_copy = curr_path[:]
                path_copy.append(curr_node.right.val)
                q.append((curr_node.right, path_copy))

            if curr_node.left:
                path_copy = curr_path[:]
                path_copy.append(curr_node.left.val)
                q.append((curr_node.left, path_copy))

        return output
