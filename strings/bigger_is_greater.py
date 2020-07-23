"""
https://www.hackerrank.com/challenges/bigger-is-greater/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

from Sean Chen's coding challenge 07-22-2020

A string is greater than another string if it comes later in a lexicographically (alphabetically) sorted list.

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
# Return the one that is smallest of the ones that are greater than w.
# Not very efficient at all! Time complexity is O(n!) where n is the length of w.
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

# Now, for a more efficient solution. Time complexity O(n^2)
# This solution traverses right to left, starting from the 2nd to last char.
# If the current_char is greater than the one to the right of it,
#   continue the traversal.
# Otherwise, the current_char must be lesser than the one to the right of it,
#   so we should swap it with a char somewhere along its right, to move up a char with a greater value and
#   therefore, create a word with a greater value.
#   So we will look at each char to its right, to find the one that is greater, but that would result in the
#       smallest positive difference. Because we want the smallest of the greater words.
#   And then swap the current_char with that one.
#   Sort the chars right of the current char and return the string.


def bigger_is_greater2(w):
    chars = list(w)
    min_diff = float('inf')
    for i in reversed(range(len(w)-1)):
        if chars[i] < chars[i+1]:
            # Need to swap chars[i] with a char that is greater (but the least of the greater ones)
            for j in range(i+1, len(w)):
                current_diff = ord(chars[j]) - ord(chars[i])
                if current_diff < min_diff and current_diff > 0:
                    min_diff = current_diff
                    smallest_letter_index = j
            # Now we know what to swap with.
            chars[i], chars[smallest_letter_index] = chars[smallest_letter_index], chars[i]

            return ''.join(chars[:i+1] + sorted(chars[i+1:]))
    return 'no answer'


# print(bigger_is_greater2('abcd'))  # abdc
# print(bigger_is_greater2('ab')) # ba
# print(bigger_is_greater2('bb')) # no answer
# print(bigger_is_greater2('hefg')) # hegf
# print(bigger_is_greater2('dhck')) # dhkc
print(bigger_is_greater2('dkhc'))  # hcdk
