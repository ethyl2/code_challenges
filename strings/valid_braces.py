"""
https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python

Given a string of braces, return whether the order of the braces is valid.

String will be non-empty and consist of ()[]{}

"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False

"""


def validBraces(string):
    # Stack to hold opening braces as we come across them
    opening_braces = []

    reference = {"(": ")", "{": "}", "[": "]"}

    for brace in string:
        if brace in reference:
            opening_braces.append(brace)
        else:
            current_opening = opening_braces.pop()
            if reference[current_opening] != brace:
                return False
    return True


print(validBraces("(){}[]"))
print(validBraces("([{}])"))
print(validBraces("(}"))
print(validBraces("[(])"))
print(validBraces("[({})](]"))
