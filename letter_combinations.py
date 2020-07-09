"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits 2-9 inclusive, 
return all possible letter combinations that the number could represent.
Order doesn't matter.

The numbers map to letters on phone buttons.

Example: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

"""


class Solution:
    def letterCombinations(self, digits: str):
        # Create lookup list.
        # I chose a list so I can use the indices as keys.
        # Looking up with a list, when you have the index, is O(1).
        # (Finding a element in a list when you just have the value is O(n) -- not the case here.)
        lookup = [set(), set(), ('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i'), ('j', 'k', 'l'),
                  ('m', 'n', 'o'), ('p', 'q', 'r', 's'), ('t', 'u', 'v'), ('w', 'x', 'y', 'z')]

        # Edge cases
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(lookup[int(digits)])

        # Create the output list, initially with the letters that correspond to the first digit.
        output = []
        for letter in lookup[int(digits[0])]:
            output.append(letter)

        # Create a variable to hold the next index of the digit string we will deal with.
        index = 1

        # Loop, while the index is less than the length of the digits, to deal with each digit.
        while index < len(digits):
            # A variable to hold the results from combining each element of the output list
            # with the characters of the current digit:
            new_output = []

            # Generate the combinations of each element of the output list with the characters
            # of the current digit
            for combo in output:
                for letter in lookup[int(digits[index])]:
                    new_output.append(combo + letter)
            index += 1
            # Set the value of output to be new_output to get it ready for the next iteration of the while loop.
            output = new_output

        return new_output


s = Solution()
# print(s.letterCombinations("23"))
# print(s.letterCombinations("234"))
print(s.letterCombinations("5678"))
