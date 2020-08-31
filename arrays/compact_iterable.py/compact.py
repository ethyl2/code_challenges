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

Article on iterators: https://opensource.com/article/18/3/loop-better-deeper-look-iteration-python

"""


def compact1(sequence):
    if len(sequence) == 0:
        return sequence
    first, *rest = sequence
    output = [first]
    for el in rest:
        if el != output[-1]:
            output.append(el)
    return output


def compact2(sequence):
    """
    Bonus 1: This version accepts any iterable, not just a sequence.
    """
    if type(sequence) == list and len(sequence) == 0:
        return sequence
    first, *rest = sequence
    output = [first]
    for el in rest:
        if el != output[-1]:
            output.append(el)
    return output


def compact3(sequence):
    """
    Bonus 2: This version accepts any iterable, not just a sequence.
    And returns an iterator instead of a list.
    TODO: Figure out how to modify the sequence iterable without exhausting it.
    Calling next() on the return value of compact() OR on sequence should advance both.
    """

    if type(sequence) == list and len(sequence) == 0:
        return sequence
    first, *rest = sequence
    output = [first]
    for el in rest:
        if el != output[-1]:
            output.append(el)
    return iter(output)


if __name__ == '__main__':
    '''
    print(compact([1, 1, 1]))
    print(compact([1, 1, 2, 2, 3, 2]))
    print(compact([]))
    print(compact(n**2 for n in [1, 2, 2]))  # [1,4]
    '''
    nums = (n ** 2 for n in [1, 2, 3])
    output = compact(nums)
    print(iter(output) is output)
    print(next(nums))
    # print(next(output))
    # print(next(output))
    # print(next(output))
