"""
https://leetcode.com/problems/happy-number/submissions/

Given a pos int. Return whether it is a 'happy num'

Find the sum of its digits squared
Repeat until you get 1, or it loops endlessly in a cycle that doesn't include 1.
"""


class Solution:

    def __init__(self):
        self.answer_set = set()

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

    def transform(num):
        # 23
        pass

    def is_happy_recursive(self, n):

        if n == 1:
            return True
        elif n in self.answer_set:
            return False

        new_num = sum([int(digit)**2 for digit in str(n)])
        self.answer_set.add(n)
        return self.is_happy_recursive(new_num)

    def is_happy_recursive2(self, n, answer_set=None):
        if answer_set == None:
            answer_set = set()
        if n == 1:
            return True
        elif n in self.answer_set:
            return False

        new_num = sum([int(digit)**2 for digit in str(n)])
        self.answer_set.add(n)
        return self.is_happy_recursive(new_num, answer_set)


s = Solution()

# print(s.isHappy(19))
# print(s.isHappy(2))
# print(s.is_happy_recursive(19))
print(s.is_happy_recursive(2))
