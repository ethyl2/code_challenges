"""
https://leetcode.com/problems/happy-number/submissions/

Given a pos int. Return whether it is a 'happy num'

Find the sum of its digits squared
Repeat until you get 1, or it loops endlessly in a cycle that doesn't include 1.
"""


class Solution:

    def isHappy(self, n: int) -> bool:
        prev = None
        current = n
        answer_set = set()

        while current not in answer_set and current != 1:
            prev = current
            string_num = str(current)
            new_num = 0
            for digit in string_num:
                new_num += int(digit) ** 2
            current = new_num
            answer_set.add(prev)

        if current == 1:
            return True
        return False


s = Solution()

# print(s.isHappy(19))
print(s.isHappy(2))
