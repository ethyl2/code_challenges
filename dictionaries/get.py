"""
https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/dictionaries-common-applications

What will the following code print?

counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))
"""

counts = {'quincy': 1, 'mrugesh': 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))
