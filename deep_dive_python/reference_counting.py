"""
Based off of deep dive python udemy course lectures.

Here's my attempt to make a code challenge, based on what I've learned.

1. Write a function that determines if two variables point to the same object in memory.

2. Write a function that, given a variable name, returns the reference count of an object in memory.
"""
import ctypes


def are_same_object(var1, var2):
    return id(var1) == id(var2)


def get_ref_count(var):

    mem_address = id(var)
    return ctypes.c_long.from_address(mem_address).value


"""
a = 1
b = 1
print(are_same_object(a, b))
print(get_ref_count(a))
a = 'fish'
b = 'fish'
print(are_same_object(a, b))
print(get_ref_count(a))
a = b
print(are_same_object(a, b))
a = 3
print(are_same_object(a, b))
b = 3
print(are_same_object(a, b))
a = {'fish': 1, 'koala': 2}
b = {'fish': 1, 'koala': 2}
print(are_same_object(a, b))
print(get_ref_count(a))
b = a
print(are_same_object(a, b))
a = None
b = None
print(get_ref_count(a))
"""

c = None
print(get_ref_count(c))
c = 'bob'
print(get_ref_count(c))
d = c
print(get_ref_count(c))
e = c
print(get_ref_count(c))
