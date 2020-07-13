"""
https://www.codewars.com/kata/566fc12495810954b1000030/train/python

Given an pos int n, 
and a digit that is < 10, d.
Square all ints from 0 - n, and return the number times d is used in the squared results.
"""


def nb_dig(n, d):
    '''
    results = ''
    for i in range(n+1):
        results += str(i * i)
    return results.count(str(d))
    '''
    return ''.join([str(i * i) for i in range(n + 1)]).count(str(d))


print(nb_dig(10, 1))  # 4
print(nb_dig(5750, 0))  # 4700
print(nb_dig(11011, 2))  # 9481
print(nb_dig(12224, 8))  # 7733
print(nb_dig(11549, 1))  # 11905
