"""
https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python

Given: an array of "hashes of names" -- such as {'name': 'Hildegard'}
Return a string with names separated by ',' except last 2 are separated by '&'

Examples:
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
"""

# My first version. Time O(2n) -> O(n). Space O(2n) => O(n)


def namelist(names):
    if len(names) == 0:
        return ''
    if len(names) == 1:
        return names[0]['name']
    name_list = []
    for entry in names:
        name_list.append(entry['name'])
    return ', '.join(name_list[:-1]) + ' & ' + name_list[-1]

# My second version. Improves time & space complexity a bit b/c doesn't make a name_list. O(n) for both.


def namelist2(names):
    if len(names) == 0:
        return ''
    if len(names) == 1:
        return names[0]['name']
    return ', '.join([names[i]['name'] for i in range(0, len(names) - 1)]) + ' & ' + names[-1]['name']

# Someone else's version, which uses .format


def namelist3(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''


print(namelist3([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(namelist3([{'name': 'Bart'}, {'name': 'Lisa'}]))
print(namelist3([{'name': 'Bart'}]))
print(namelist3([]))
