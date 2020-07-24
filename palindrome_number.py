"""
https://leetcode.com/problems/palindrome-number/

Return True if a number is a palindrome

121 -> True
-121 -> False 121-
10 -> False 01

Bonus: Could you solve it without converting the int to a string?

I think I'll try converting the int into a list by using modulus.
Then make 2 pointers left and right to compare items.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_list = []
        while x > 0:
            curr_digit = x % 10
            x_list.append(curr_digit)
            x //= 10

        left = 0
        right = len(x_list) - 1
        while left < right:
            if x_list[left] != x_list[right]:
                return False
            left += 1
            right -= 1
        return True

    # This version compares the 2 sublists that result, instead of using 2 pointers.
    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        x_list = []
        while x > 0:
            curr_digit = x % 10
            x_list.append(curr_digit)
            x //= 10
        if len(x_list) % 2 == 0:
            return x_list[:len(x_list)//2] == list(reversed(x_list[len(x_list)//2:]))
        else:
            return x_list[:len(x_list)//2] == list(reversed(x_list[(len(x_list)//2)+1:]))


s = Solution()
print(s.isPalindrome2(121))
print(s.isPalindrome2(-121))
print(s.isPalindrome2(1221))
print(s.isPalindrome2(1231))
print(s.isPalindrome2(12321))
