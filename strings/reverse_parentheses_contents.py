"""
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

From Sean Chen lecture 07-30-2020

Reverse the strings inside ea pair of matching parenthesis, starting from the innermost one.
(So a substring could potentially get reversed back to original order, depending on amount of nesting).
Results shouldn't have ()
Strings all contain lower-case English letters and  ()  are balanced.

Examples:

Input: s = "(abcd)"
Output: "dcba"

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"

Approach:
Interate through list created from string.
Keep a stack of the starting parentheses' indices.
When we encounter a closing parenthesis, pop from the stack,
    and reverse the sublist between the index popped and before the closing parenthesis,
    making a new list that doesn't include the parenthesis currently involved, and does include the newly
    reversed sublist.
Finally, convert the list into a string and return that.
"""


class Solution:
    # My approach here gets rid of the () as we iterate and find a ).
    # Creating sublists isn't the most space efficient solution, but an in-place would be tricky
    #   if I keep the approach of taking out the () as I iterate. But it would be interesting to
    #   make a more space-efficient solution, in the future.
    # Sean's version took out the () at the very end, requiring another iteration.
    def reverseParentheses(self, s: str) -> str:
        opening_indices = []
        chars = list(s)
        i = 0
        # while i < len(chars):
        while i < len(chars):
            if chars[i] == '(':
                opening_indices.append(i)
                # print('found opening')
                i += 1
            elif chars[i] == ')':
                # print('found closing')
                current_opening_index = opening_indices.pop()
                # print('current_opening_index: ', current_opening_index)
                # print('current_index: ', i)
                # print(chars[i-1:current_opening_index:-1])
                chars = chars[:current_opening_index] + \
                    chars[i-1:current_opening_index:-1] + chars[i+1:]
                # print(chars)
                i -= 1
            else:
                i += 1
        # print('at end, i: ', i)
        # print(opening_indices)
        return ''.join(chars)

    # Here's Sean's recursive solution
    def recursive_reverse_in_parens(self, s):
        new_s = ''
        pos = 0
        while pos < len(s):
            if s[pos] == '(':
                # Call the helper using everything to the right of (
                result, length = self.helper(s[pos+1:])
                new_s += result
                # Advance the pos to be the result's length + 1 (to get rid of the ')')
                pos += (length + 1)
            else:
                new_s += s[pos]
            pos += 1
        return new_s

    def helper(self, s):
        # Returns the reversed substring and its length
        new_substring = ''
        pos = 0
        while pos < len(s) and s[pos] != ')':
            if s[pos] == '(':
                result, length = self.helper(s[pos+1])
                new_substring += result
                pos += (length + 1)
            else:
                new_substring += s[pos]
            pos += 1
        return new_substring[::-1], pos


s = Solution()
# print(s.reverseParentheses('(abcd)'))
# print(s.reverseParentheses("(u(love)i)"))
# print(s.reverseParentheses("(ed(et(oc))el)"))
# print(s.reverseParentheses("a(bcdefghijkl(mno)p)q"))
# print(s.recursive_reverse_in_parens("(abcd)"))
print(s.recursive_reverse_in_parens("(u(love)i)"))  # not working yet
# print(s.recursive_reverse_in_parens("(ed(et(oc))el)")) # ""
# print(s.recursive_reverse_in_parens("a(bcdefghijkl(mno)p)q")) # ""
