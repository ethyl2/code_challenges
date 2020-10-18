"""
https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/regular-expressions-practical-applications

What will search for a "$" in a regular expression?


$


\dollar\


\$


!$
"""
import re
myDollar = '$'
print(bool(re.match('\$', myDollar)))
print(bool(re.match('$', myDollar)))
print(bool(re.match('\$$', myDollar)))


'''
FYI: $ indicates the end of the string.
'''
