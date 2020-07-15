"""
From Sean Chen's lecture 7-15-2020
https://app.codesignal.com/interview-practice/task/PhNPP45hZGNwpPchi

Given a binary tree (not necessarily a BST), return its node values in this format:
1. Root
2. Then root children's values, L to R.
3. Then the values at the next level, etc.

Told to try not using recursion.

Return a list.

Looks like a BFT, which uses a queue.
"""


from collections import deque


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def traverseTree(t):
    output = []
    if t is None:
        return output
    q = deque()

    q.append(t)

    while len(q) > 0:
        current = q.popleft()
        output.append(current.value)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
    return output
