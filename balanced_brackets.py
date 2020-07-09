"""
From hackerrank test
Given string that can contain 4 types of brackets: [] () {} ||

Return boolean indicating whether the string is balanced. =
    has as many opening brackets of a type as closing brackets of that type.
    Brackets cannot overlap each other such as [(])
"""
# Time: O(2n) -> O(n)
# Space: O(2n) -> O(n)

# Easiest thing to do is to start with a check that the number of opening brackets == num closing brackets
# With a lookup dict
# Loop through arr
# If char in "[ ] ( ) { } |".split(" ")
#   add to lookup
# Then do a check for each type of brackets.


def balancedBrackets(string):
    # print("[ ] ( ) { } |".split(" "))
    lookup = {}
    brackets = "[ ] ( ) { } |".split(" ")
    for char in brackets:
        lookup[char] = 0
    for char in string:
        if char in brackets:
            lookup[char] += 1
    print(lookup)

    if lookup["("] != lookup[")"]:
        return False

    if lookup["["] != lookup["]"]:
        return False

    if lookup["{"] != lookup["}"]:
        return False

    if lookup["|"] % 2 != 0:
        return False

    # Now, to make sure brackets don't overlap each other:
    # Setting up variables:
    opening_brackets = ["(", "[", "{"]
    closing_brackets = [")", "]", "}"]
    pair_lookup = {"(": ")", "{": "}", "[": "]", "|": "|"}
    pipe_is_opening = True
    opening_stack = []

    # Loop through string. If char is an opening bracket, put it on the stack.
    # When the char is closing, pop the stack and see if they are a pair.
    # If not, return False, otherwise, continue

    for char in string:
        if char in opening_brackets:
            opening_stack.append(char)
        elif char == "|" and pipe_is_opening:
            opening_stack.append(char)
            pipe_is_opening = False
        elif char in closing_brackets:
            current_opening = opening_stack.pop()
            if pair_lookup[current_opening] != char:
                return False
        elif char == "|" and not pipe_is_opening:
            current_opening = opening_stack.pop()
            if pair_lookup[current_opening] != char:
                return False
            pipe_is_opening = True

    return True


print(balancedBrackets("[(foo(bar))baz)]"))  # False
print(balancedBrackets("[(foo(bar)baz)]"))  # True

# 2nd approach only uses the 2nd part of my first approach, because it is sufficient on its own.
# The 1st part was not strictly necessary.
# This check will also return False if the number of types of brackets is not balanced.

# Time and space complexity is a little better. O(n) for both because only a stack is made.


def balancedBrackets2(string):
    opening_brackets = ["(", "[", "{"]
    closing_brackets = [")", "]", "}"]
    pair_lookup = {"(": ")", "{": "}", "[": "]", "|": "|"}
    pipe_is_opening = True
    opening_stack = []

    # Loop through string. If char is an opening bracket, put it on the stack.
    # When the char is closing, pop the stack and see if they are a pair.
    # If not, return False, otherwise, continue

    for char in string:
        if char in opening_brackets:
            opening_stack.append(char)
        elif char == "|" and pipe_is_opening:
            opening_stack.append(char)
            pipe_is_opening = False
        elif char in closing_brackets:
            current_opening = opening_stack.pop()
            if pair_lookup[current_opening] != char:
                return False
        elif char == "|" and not pipe_is_opening:
            current_opening = opening_stack.pop()
            if pair_lookup[current_opening] != char:
                return False
            pipe_is_opening = True

    return True


print(balancedBrackets2("[(foo(bar))baz)]"))  # False
print(balancedBrackets2("[(foo(bar)baz)]"))  # True
print(balancedBrackets2("[(|foo(bar)baz|)]"))  # True
print(balancedBrackets2("[(foo||(bar)baz|)]"))  # False
