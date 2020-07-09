"""
https://leetcode.com/problems/min-stack/

push(x), pop() doesn't return, top() gets top el, getMin() <- all with O(1) time complexity
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.storage = []

    def push(self, x: int) -> None:
        if len(self.storage) > 0:
            current_min = self.storage[-1][1]
        if x < current_min or len(self.storage) == 0:
            current_min = x
        self.storage.append(x, current_min)

    def pop(self) -> None:
        self.storage.pop()

    def top(self) -> int:
        return self.storage[-1][0]

    def getMin(self) -> int:
        return self.storage[-1][1]
