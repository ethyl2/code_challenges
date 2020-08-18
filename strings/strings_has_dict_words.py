"""
https://leetcode.com/problems/word-break/

from Andrew Candela's lecture 08-18-2020

Given a non-empty string s
and a dictionary wordDict containing non-empty words,
Return whether s can be segmented into a space-separated sequence of one or more words from wordDict.

Examples:
s = 'leetcode', wordDict = ['leet', 'code'] -> True
s = 'applepenapple', wordDict = ['apple', 'pen'] -> True
s = 'catsandog', wordDict = ['cats', 'dog', 'sand', 'and', 'cat'] -> False b/c it has the words, but the letters overlap, so you couldn't make
    a space-separated sequence
"""
from typing import List, Set


class Solution:

    # Here's his first solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        return self.wordBreakWithSet(s, wordSet)

    def wordBreakWithSet(self, s: str, wordSet: Set[str]) -> bool:
        if len(s) == 0:
            return True
        for i in range(1, len(s) + 1):
            left_slice = s[:i]
            right_slice = s[i:]
            if left_slice in wordSet:
                if self.wordBreakWithSet(right_slice, wordSet):
                    return True

        if s in wordSet:
            return True
        return False

    # Here's my version. It was buggy at first, because I was advancing the index up past the found word at first, instead of just advancing the
    # index up by 1 when a word from the dictionary was found.
    # Example: It was finding 'aaa' and not 'aaaa' (when both were valid words)
    #  because the index would go past 'aaa' and therefore caused a incorrect False because a stray 'a' was left over.

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        index = 1

        while len(s) > 1 and index < len(s) + 1:
            if s[:index] in wordDictSet and self.wordBreak2(s[index:], wordDictSet):
                # Check to see if the rest of the string also returns True
                if self.wordBreak2(s[index:], wordDictSet):
                    return True
            else:
                # Otherwise, expand the amount of the string being searched by incrementing the index pointer.
                index += 1

        if len(s) == 0 or s in wordDictSet:
            return True

        return False

    def wordBreak3(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        self.cache_of_rejected_strings = set()
        return self.wordBreak4(s, wordDict)

    def wordBreak4(self, s: str, wordDict: List[str]) -> bool:
        if s in self.cache_of_rejected_strings:
            return False
        index = 1

        while len(s) > 1 and index < len(s) + 1:
            if s[:index] in wordDict and self.wordBreak4(s[index:], wordDict):
                # Check to see if the rest of the string also returns True
                if self.wordBreak4(s[index:], wordDict):
                    return True
                else:
                    self.cache_of_rejected_strings.add(s[index:])
            else:
                # Otherwise, expand the amount of the string being searched by incrementing the index pointer.
                index += 1

        if len(s) == 0 or s in wordDict:
            return True

        return False


solution = Solution()
# print(solution.wordBreak2('leetcode', ['leet', 'code']))
# print(solution.wordBreak3('applepenapple', ['apple', 'pen']))
# print(solution.wordBreak3('catsandog', [
#       'cats', 'dog', 'sand', 'and', 'cat']))  # False
# print(solution.wordBreak3('abc', ['a', 'b', 'c'])) # True
# print(solution.wordBreak3('aaaaaaa', ['aaaa', 'aaa']))  # True
string1 = "bccdbacdbdacddabbaaaadababadad"
dict1 = ["cbc", "bcda", "adb", "ddca", "bad", "bbb", "dad", "dac", "ba", "aa", "bd", "abab", "bb", "dbda", "cb", "caccc", "d", "dd", "aadb", "cc", "b", "bcc", "bcd", "cd", "cbca", "bbd",
         "ddd", "dabb", "ab", "acd", "a", "bbcc", "cdcbd", "cada", "dbca", "ac", "abacd", "cba", "cdb", "dbac", "aada", "cdcda", "cdc", "dbc", "dbcb", "bdb", "ddbdd", "cadaa", "ddbc", "babb"]
print(solution.wordBreak3(string1, dict1))
