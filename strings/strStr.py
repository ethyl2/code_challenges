"""
https://leetcode.com/problems/implement-strstr/
Return the first occurence of needle in haystack, or -1 if not found. Return 0 when needle is an empty string.
haystack and needle are both strings
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        else:
            return haystack.find(needle)
