"""
https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/comparing-and-sorting-tuples


Which does the same thing as the following code?:

lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)

Choices:

print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )

print( [ (k,v) for k,v in counts.items().sorted() ] )

print( sorted( [ (v,k) for k,v in counts.keys() ] ) )

print( [ (k,v) for k,v in counts.values().sort() ] )
"""
counts = {'May': 200, 'Mashima': 15, 'Hui': 215}
lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)

print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )
