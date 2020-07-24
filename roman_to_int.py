"""
https://leetcode.com/problems/roman-to-integer/

Given a string representig a Roman numeral, return its int value.
Input is guaranteed to be within the range from 1 to 3999.

'III' -> 3
'IV' => 4
'IX' => 9
'LVIII' => 58
'MCMXCIV' => 1994 b/c M = 1000, CM = 900, XC = 90, IV = 4

My approach:
    Make a lookup dict.
    Initialize a total variable.
    Iterate through the string.
    If the value to the right of the current char is greater than the current value,
        do subtraction to find what needs to be added to total.
        and then skip over that char to the right.
    Otherwise, add the current value to the total.
    Return the total at the end.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        roman_list = list(s)
        i = 0
        total = 0
        while i < len(roman_list) - 1:
            if lookup[roman_list[i]] >= lookup[roman_list[i+1]]:
                total += lookup[roman_list[i]]
                i += 1
            else:
                total += lookup[roman_list[i+1]] - lookup[roman_list[i]]
                i += 2
        if i < len(roman_list):
            total += lookup[roman_list[i]]
        return total

    # The only difference with this version is that it doesn't put the roman numerals into a list,
    # because I realized it isn't necessary. I'm not altering the string in any way.
    # More space efficient to just leave it as a string.
    def romanToInt2(self, s: str) -> int:
        lookup = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        i = 0
        total = 0
        while i < len(s) - 1:
            if lookup[s[i]] >= lookup[s[i+1]]:
                total += lookup[s[i]]
                i += 1
            else:
                total += lookup[s[i+1]] - lookup[s[i]]
                i += 2
        if i < len(s):
            total += lookup[s[i]]
        return total


s = Solution()
# print(s.romanToInt('II'))
# print(s.romanToInt('III'))
# print(s.romanToInt('IV'))
# print(s.romanToInt('IX'))
# print(s.romanToInt('LVIII'))
print(s.romanToInt2('MCMXCIV'))
