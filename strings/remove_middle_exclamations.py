"""
https://www.codewars.com/kata/57faefc42b531482d5000123

Given a string,
remove all exclamation marks from the string, except for a ! if it exists at the very end.

remove("Hi!") == "Hi!"
remove("Hi!!!") == "Hi!!!"
remove("!Hi") == "Hi"
remove("!Hi!") == "Hi!"
remove("Hi! Hi!") == "Hi Hi!"
remove("Hi") == "Hi"
"""


def remove(s):
    output = ''
    allowed = True
    for i in range(len(s)-1, -1, -1):
        if s[i] == '!' and allowed:
            output = s[i] + output
        elif s[i] != '!':
            output = s[i] + output
            allowed = False

    return(output)


print(remove("Hi!"))
print(remove("Hi"))
print(remove("!Hi"))
print(remove("Hi! Hi!"))
print(remove("Hi!!!"))

# Another person's solution:


def remove2(s):
    return s.replace('!', '') + '!'*(len(s) - len(s.rstrip('!')))


print(remove2("Hi!"))
print(remove2("Hi"))
print(remove2("!Hi"))
print(remove2("Hi! Hi!"))
print(remove2("Hi!!!"))
