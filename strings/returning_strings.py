"""
https://www.codewars.com/kata/55a70521798b14d4750000a4/train/python

Make a function that will return a greeting statement that uses an input; 
your program should return, "Hello, <name> how are you doing today?".

Sample test: 
Test.assert_equals(greet('Ryan'), "Hello, Ryan how are you doing today?")
"""


def greet(name):
    return(f"Hello, {name} how are you doing today?")


print(greet('Ryan'))
