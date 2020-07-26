"""
https://leetcode.com/problems/count-and-say/
Given a integer n, return the nth term of the 'count-and-say' sequence.

The count-and-say sequence's first 5 terms:
1
11
21
1211
111221

1 -> 'one 1' -> 11 ?
2 -> 'two 1s' -> 21
21 -> 'one 2, then one 1' -> 1211

# To be completed later, once I think more about this problem.
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        def split(word):
            return [char for char in word]
        lookup = {1: '1', 2: '11', 3: '21', 4: '1211', 5: '111221'}
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        elif n == 3:
            return '21'
        else:
            split_result = split(self.countAndSay(n-1))
            print(split_result)
            return self.countAndSay(int(split_result[0])) + self.countAndSay(int(split_result[1]))


s = Solution()
print(s.countAndSay(1))
print(s.countAndSay(4))
