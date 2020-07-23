"""
https://www.hackerrank.com/challenges/bigger-is-greater/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

from Sean Chen's coding challenge 07-22-2020

Given a word with all lower case chars, return the word that is an arrangment of its chars AND
is lexicographically greater than the word 
AND is the smallest word of the potential words that are lexicographically greater.

Return 'no answer' if no string meets the criteria.

Examples:
lmno -> lmon
ab -> ba
bb -> no answer
hefg -> hegf
dhck -> dhkc
dkhc -> hcdk
dcba -> no answer
dcbb -> no answer
abdc -> acbd
abcd -> abdc
fedcbabcd => fedcbabdc
"""
# My first instinct is to try a brute-force approach.
# Find all of the combinations
# Return the one that is smallest of the ones that are larger than w.
from itertools import permutations


def bigger_is_greater(w):
    combos = list(permutations(w))
    current_combo_winner = None
    for combo in combos:
        current_word = ''.join(combo)
        if current_word > w:
            if current_combo_winner is None or current_word < current_combo_winner:
                current_combo_winner = current_word
    if current_combo_winner is None:
        return 'no answer'
    return current_combo_winner


print(bigger_is_greater('abcd'))
print(bigger_is_greater('ab'))
print(bigger_is_greater('bb'))
print(bigger_is_greater('hefg'))
print(bigger_is_greater('dhck'))
print(bigger_is_greater('dkhc'))
