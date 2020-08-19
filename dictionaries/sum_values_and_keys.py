"""
Given an object/dictionary with keys and values that consist of both strings and integers, 
    design an algorithm to calculate and return the sum of all of the numeric values.
For example, given the following object/dictionary as input:
{
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}
Your algorithm should return 41, the sum of the values 23 and 18.
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""
from typing import Dict


def sum_numeric_values(input: Dict) -> int:
    total = 0
    for value in input.values():
        if type(value) == int:
            total += value
    return total


print(sum_numeric_values({
    "cat": "bob",
    "dog": 23,
    19: 18,
    90: "fish"
}))

"""
Given an object/dictionary with keys and values that consist of both strings and integers, 
design an algorithm to calculate and return the sum of all of the numeric values and keys.
For example, given the following object/dictionary as input:
{
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}
Your algorithm should return 150, the sum of the values 23, 19, 18, and 90.
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""


def sum_numeric_keys_and_values(input: Dict) -> int:
    total = 0
    for key, value in input.items():
        if type(key) == int:
            total += key
        if type(value) == int:
            total += value
    return total


print(sum_numeric_keys_and_values({
    "cat": "bob",
    "dog": 23,
    19: 18,
    90: "fish"
}))
