"""
https://www.codewars.com/kata/5650ab06d11d675371000003
Given a string and a size, split the string into substrings of that size.

Example:
Split the string into other strings of size #3 'supercalifragilisticexpialidocious'
Will return a new string
'sup erc ali fra gil ist ice xpi ali doc iou s'

Assumptions:
len(string) > 0
Strings have no spaces
Size > 0
"""


def split_in_parts(s, part_length):
    output = ''
    for i in range(0, len(s), part_length):
        output += s[i:i + part_length] + ' '
    return output[:-1]


print(split_in_parts("HelloKata", 3))  # "H e l l o K a t a"
print(split_in_parts('supercalifragilisticexpialidocious', 3))

# My second version uses a list comprehension.
# Also, using join() makes it so I don't have to slice off the extra space that results from the first version.


def split_in_parts2(s, part_length):
    return ' '.join([s[i:i + part_length] for i in range(0, len(s), part_length)])


print(split_in_parts2("HelloKata", 3))
print(split_in_parts2('supercalifragilisticexpialidocious', 3))
