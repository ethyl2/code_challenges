"""
https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python
Given a string, return whether the string is valid.
String will contain 0 or more ().

Examples:
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Similar to some other challenges, but this one only deals with 1 type of parentheses.
So instead of making a stack to keep track of coming across opening parentheses, only a running count is needed.
"""


def valid_parentheses2(string: str) -> bool:
    num_opening = 0
    for char in string:
        if char == '(':
            num_opening += 1
        elif char == ')':
            if num_opening == 0:
                # No opening parenthesis to pair with the closing one
                return False
            num_opening -= 1
    return num_opening == 0


def valid_parentheses(string):
    count = 0
    for char in string:
        if char == '(':
            count += 1
        if char == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


print(valid_parentheses("()"))
print(valid_parentheses(")(()))"))
print(valid_parentheses("("))
print(valid_parentheses("(())((()())())"))

# False. This one shows why just doing a comparison to see if the count of closing and opening are the same, isn't sufficient.
print(valid_parentheses("hi())("))
