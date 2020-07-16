'''
https://app.codesignal.com/interview-practice/task/m9vC4ALaAeudkwRTF/description
Started in Sean Chen's lecture 07-15-2020

Given a binary tree (not necessarily a BST), return the highest value at each level of the tree, in an array.

This is my solution. His is in largest_values_in_tree_rows.py
'''
from collections import deque


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def largestValuesInTreeRows(t):
    if t is None:
        return []
    output = [t.value]
    q = deque()
    q.append((t, 0))
    lookup = dict()

    while len(q) > 0:
        current = q.popleft()
        # print(f'({current[0].value}: {current[1]})')
        if current[0].left is not None:
            q.append((current[0].left, current[1] + 1))
            if (current[1] + 1) in lookup:
                if current[0].left.value > lookup[current[1] + 1]:
                    lookup[current[1] + 1] = current[0].left.value
            else:
                lookup[current[1] + 1] = current[0].left.value

        if current[0].right is not None:
            q.append((current[0].right, current[1] + 1))
            if (current[1] + 1) in lookup:
                if current[0].right.value > lookup[current[1] + 1]:
                    lookup[current[1] + 1] = current[0].right.value
            else:
                lookup[current[1] + 1] = current[0].right.value

    # print(lookup)
    for value in lookup.values():
        output.append(value)
    return output


t = Tree(-1)
node5 = Tree(5)
t.left = node5
node7 = Tree(7)
t.right = node7
node1 = Tree(1)
node7.right = node1
print(largestValuesInTreeRows(t))
