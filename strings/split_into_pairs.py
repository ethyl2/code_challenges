"""
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/python

Given a string
Return an array, where each element is a pair of 2 consecutive chars from that string,
    where the final pair will be a character and underscore if the len(string) is odd.

Examples:
solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']   
"""
# Initialize return_array
# Loop through chars in string, 2 at a time.
# If len(final element in return_array) is 1, add '_'
# Return return_array


import re


def solution(s):
    output = []
    for i in range(0, len(s), 2):
        print(s[i:i+2])
        output.append(s[i:i+2])
    if len(output[-1]) == 1:
        output[-1] += '_'
    return output

# My 2nd solution, utilizing a list comprehension


def solution2(s):
    output = [s[i:i+2] for i in range(0, len(s), 2)]
    if len(output) > 0 and len(output[-1]) == 1:
        output[-1] += '_'
    return output

# Here's a solution with everything inside the list comprehension:


def solution3(s):
    return [s[i:i+2] if i < len(s) - 1 else s[-1] + '_' for i in range(0, len(s), 2)]


# And here's someone else's solution, which uses regex:


def solution4(s):
    # This adds an _ to the end of the string, and then returns the groups of 2.
    # If the len(s) is even, it just leaves out the _ because it won't be part of a group of 2.
    return re.findall(".{2}", s + "_")


print(solution4('abc'))
print(solution4('abcdef'))


# Another example of using re.findall, from https://www.geeksforgeeks.org/python-regex-re-search-vs-re-findall/
# A sample text string where regular expression
# is searched.
string = """Hello my Number is 123456789, and 
			my friend's number is 987654321."""

# A sample regular expression to find digits.
regex = '\d+'

match = re.findall(regex, string)
print(match)  # ['123456789', '987654321']
