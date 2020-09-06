"""
from algo expert
Given a binary tree, invert it, which means that every left node should be swapped with its right node.

Example:
binary tree: [3, 9, 20, None, None, 15, 7]
    3
   / \
  9  20
    /  \
   15   7

Return 
    3
   / \
  20  9
  / \ 
 7   15    
"""
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode):
    """
    O(n) time, O(n) space
    """
    q = deque()
    q.append(root)
    while len(q) > 0:
        current = q.popleft()
        if current.right or current.left:
            current.right, current.left = current.left, current.right
            q.append(current.right)
            q.append(current.left)
    return root


def invert_tree_recursive(root: TreeNode):
    """
    O(n) time, 
    O(log n) space (which also could be defined as O(h), where h is the height of the binary tree)
    """
    root.left, root.right = root.right, root.left
    if root.left:
        invert_tree_recursive(root.left)
    if root.right:
        invert_tree_recursive(root.right)
    return root


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


def level_order(root: TreeNode) -> List[List[int]]:
    '''
    Returns a nested array, 
    in which each inner array contains the values of the nodes at that level.
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


if __name__ == "__main__":
    # Testing iterative version of invert_tree()

    tree = create_binary_tree_from_array([3, 9, 20, None, None, 15, 7])
    invert_tree(tree)
    level_order_representation = level_order(tree)
    print(level_order_representation)
    print(level_order_representation == [[3], [20, 9], [7, 15, None, None]])

    tree2 = create_binary_tree_from_array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    invert_tree(tree2)
    level_order_representation2 = level_order(tree2)
    print(level_order_representation2)
    print(level_order_representation2 == [[1], [3, 2], [7, 6, 5, 4], [9, 8]])

    # Testing Recursive Version

    tree3 = create_binary_tree_from_array([3, 9, 20, None, None, 15, 7])
    invert_tree_recursive(tree3)
    level_order_representation3 = level_order(tree3)
    print(level_order_representation3)
    print(level_order_representation3 == [[3], [20, 9], [7, 15, None, None]])

    tree4 = create_binary_tree_from_array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    invert_tree_recursive(tree4)
    level_order_representation4 = level_order(tree2)
    print(level_order_representation4)
    print(level_order_representation4 == [[1], [3, 2], [7, 6, 5, 4], [9, 8]])
