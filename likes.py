"""
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

Given an array of strings, where strings are names of people.
Return a string that is correctly formatted.

Formatting Rules:
likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
"""
from typing import List


def likes(names: List[str]) -> str:
    # Start with what the strings all have in common
    output = ' this'
    # Next, deal with lengths 0 & 1
    if len(names) <= 1:
        output = ' likes' + output
        if len(names) == 0:
            output = 'no one' + output
        else:
            output = names[0] + output
    # Or, deal with lengths 2 and above
    else:
        output = ' like' + output
        if len(names) == 2:
            output = f'{names[0]} and {names[1]}' + output
        elif len(names) == 3:
            output = f'{names[0]}, {names[1]} and {names[2]}' + output
        else:
            output = f'{names[0]}, {names[1]} and {len(names)-2} others' + \
                output
    return output

# Another person's implementation is below. I like it a lot.


def likes2(name: List[str]) -> str:
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


print(likes([]))
print(likes(['Beej']))
print(likes(['Beej', 'Sean']))
print(likes(['Beej', 'Sean', 'Kapil']))
print(likes(['Beej', 'Sean', 'Kapil', 'Andrew']))
print(likes(['Beej', 'Sean', 'Kapil', 'Andrew', 'Greg']))
