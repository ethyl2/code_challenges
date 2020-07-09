"""
https://leetcode.com/problems/wildcard-matching/

From Sean Chen Lecture 07-08-2020

Given: input string s
pattern p
Return boolean to should whether s matches p, with the matching covering the entire s (not partial)
'?' matches any single char, but not an empty string
'*' matches any sequence of chars, including an empty string
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def recurse(s, p):
            if not s:
                # return (p == '') or (p[0] == '*' and recurse(s, p[1:]))
                cache[(s, p)] = (p == '') or (
                    p[0] == '*' and recurse(s, p[1:]))
            if not p:
                # return s == ''
                cache[(s, p)] = s == ''
            if (s, p) not in cache:
                if p[0] == '*':
                    cache[(s, p)] = recurse(s, p[1:]) or recurse(s[1:], p)
                else:
                    if s[0] != p[0] and p[0] != '?':
                        cache[(s, p)] = False
                    else:
                        # Use pointers to move along s and p while current p isalpha or ?
                        sp, pp = 0, 0

                        while sp < len(s) and pp < len(p) and (s[sp] == p[pp] or p[pp] == '?'):
                            sp += 1
                            pp += 1

                        # If we've made it to the end for both s and p
                        if sp == len(s) and pp == len(p):
                            cache[(s, p)] = True
                        # Otherwise, we're not at the end because the current p is a *.
                        # So, need to recurse to explore the different matches * causes.
                        else:
                            cache[(s, p)] = recurse(s[1:], p[1:])
            return cache[(s, p)]
        return recurse(s, p)


solution = Solution()
print(solution.isMatch('aa', 'a'))  # False
print(solution.isMatch('cb', '?a'))  # False
print(solution.isMatch('aa', '*'))  # True
print(solution.isMatch('adceb', 'a*b'))  # True
print(solution.isMatch('acdcb', 'a*c?b'))  # False
