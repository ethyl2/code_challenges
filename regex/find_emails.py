"""
https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/regular-expressions-matching-and-extracting-data

What will the following program print?:

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)

"""

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)
