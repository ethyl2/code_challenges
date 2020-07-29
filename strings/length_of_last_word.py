"""
https://leetcode.com/problems/length-of-last-word/

Given string s of upper/lower case alphabets and empty space characters ' ', return the
length of the last word (last word  means the last appearing word if we loop from left -> right)
If no last word, return 0.

word = maximal substring consisting of non-space chars.

Example:
"Hello World" -> 5
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0 or s == None:
            return 0
        # words = s.strip().split(' ')
        # return len(words[-1])
        # More concise, and uses less memory but has a longer runtime,
        # according to leetcode
        return len(s.strip().split(' ')[-1])


solution = Solution()
print(solution.lengthOfLastWord("Hello World"))
print(solution.lengthOfLastWord("a "))
