"""
https://github.com/LambdaSchool/cs-module-project-hash-tables/tree/master/applications/no_dups

Input: a string of words separated by spaces. Only the letters a-z are utilized.

Output: the string in the same order, but with subsequent duplicate words removed.

There must be no extra spaces at the end of your returned string.

The solution must be O(n).
"""


def no_dups(s):
    lookup = set()
    s_list = s.split()
    output = ''
    for word in s.split():

        if word not in lookup:
            lookup.add(word)
            output += word + ' '
    return output.strip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
