"""
https://leetcode.com/problems/valid-parentheses/
Given a string containing only (){}[], determine if input string is valid: 
open brackets are closed by the same type of brackets and in the correct order.

Examples:
Input: "()"
Output: true

Input: "()[]{}"
Output: true

Input: "(]"
Output: false

Input: "([)]"
Output: false

Input: "{[]}"
Output: true

My approach:
Traverse thru the string. If the current char is an opening bracket, put it in a stack.
    If it is a closing bracket, see if it corresponds to the opening brackets popped from the stack.
    If not, return False.
If done traversing, return True.
"""
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        opening = ('(', '{', '[')
        closing = (')', '}', ']')
        stack = deque()
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if len(stack) < 1:
                    return False
                if closing.index(char) != opening.index(stack.pop()):
                    return False
        if len(stack) > 0:
            return False
        return True


s = Solution()
print(s.isValid('()'))
print(s.isValid('()]'))
print(s.isValid('([])'))
print(s.isValid('([)]'))
