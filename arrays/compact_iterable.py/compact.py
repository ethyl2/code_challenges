"""
https://github.com/Py-Lambdas/code-challenges/tree/master/200_digging_deeper/compact

Given a sequence, return a new iterable (anything you can loop over) with adjacent
duplicate values removed.

For example:

>>> compact([1, 1, 1])
[1]
>>> compact([1, 1, 2, 2, 3, 2])
[1, 2, 3, 2]
>>> compact([])
[]
"""


def compact(sequence):
    if len(sequence) == 0:
        return sequence
    first, *rest = sequence
    output = [first]
    for el in rest:
        if el != output[-1]:
            output.append(el)
    return output


print(compact([1, 1, 1]))
print(compact([1, 1, 2, 2, 3, 2]))
print(compact([]))
