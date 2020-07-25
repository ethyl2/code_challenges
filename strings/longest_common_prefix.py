"""
https://leetcode.com/problems/longest-common-prefix/
Given a list of strings, find the longest common prefix -- the beginning chars that all of the strings have in common.

Examples:
Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Output: ""
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) < 1:
            return ''
        output = ''
        # Sort the strings by length to put the shortest string as the first element.
        strs.sort(key=lambda x: len(x))
        # Iterate through the first element's characters
        for i in range(len(strs[0])):
            # Compare the char to what is located at the same position on the other strings.
            for j in range(len(strs)):
                # Stop when they don't match anymore.
                if strs[0][i] != strs[j][i]:
                    return output
            # If they all match, add the char to the output
            output += strs[0][i]
        return output

    # I feel that this approach might be more time-efficient, average-case-wise at least.
    # Instead of comparing the first char of each string in strs, like the first approach, and then
    # moving on to comparing the second char of each string in strs,
    # It looks at each string one at a time until there aren't elements in common anymore.
    def longestCommonPrefix2(self, strs) -> str:
        if len(strs) < 1:
            return ''

        # Sort the strings by length to put the shortest string as the first element.
        strs.sort(key=lambda x: len(x))
        output = list(strs[0])

        # Iterate thru strs only as long as first elements are in common
        for i in range(1, len(strs)):
            # Compare the chars in the current output list with the chars of the strs[i].
            for j, char in enumerate(output):
                # Stop if there are no longer any first chars in common
                if len(output) < 1:
                    return ''
                # When a char doesn't match, stop iterating on the chars of strs[i]
                # and chop off the rest of the current output list.
                if strs[i][j] != char:
                    output = output[:j]
                    break

        return ''.join(output)


s = Solution()
print(s.longestCommonPrefix2(["flower", "flow", "flight"]))
