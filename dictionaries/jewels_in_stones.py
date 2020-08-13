"""
https://leetcode.com/problems/jewels-and-stones/submissions/
Given J, the types of stones that are jewels. It is a string, like 'aA'
and given S, the stones you have, like 'aAAbbbb'
Return the num of stones you have that are jewels.

Example: J='z', S='ZZ' -> 0
Example: J='aA', S='aAAbbbb' -> 3
"""


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel_set = set(J)
        count = 0
        for stone in S:
            if stone in jewel_set:
                count += 1
        return count


s = Solution()
print(s.numJewelsInStones('aA', 'aAAbbbb'))
