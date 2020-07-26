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

    # Another way, if using .find() was not allowed:
    def strStr2(self, haystack, needle):
        if len(needle) == 0:
            return 0
        substring_length = len(needle)
        for i in range(len(haystack) - substring_length):
            print(haystack[i:i+substring_length])
            if haystack[i:i+substring_length] == needle:
                return i
        return -1


s = Solution()
print(s.strStr2('hello', 'll'))
