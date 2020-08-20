"""
From Kapil Sharma's lecture 08-20-2020

'Find is a number is an armstrong number or not.'

Question: What is an Armstrong number?
Kapil's response: An Armstrong number is a number in which all of its digits cubed and summed together equal the number.

153 = 1*1*1 + 5*5*5 + 3*3*3
370 = 3*3*3 + 7*7*7 + 0*0*0
371 = 3*3*3 + 7*7*7 + 1*1*1

Note:
In this problem, we are always dealing with numbers with 3 digits. Armstrong numbers (AKA narcissistic numbers) more generally refer to
a number 'that is the sum of its own digits each raised to the power of the number of digits',
so if a number had more or less digits than 3, we would have to rewrite this implementation.
https://en.wikipedia.org/wiki/Narcissistic_number
https://mathworld.wolfram.com/NarcissisticNumber.html

Question #2: Is space complexity a consideration? If so, and we need to handle numbers with large amounts of digits,
we might want to put our results of handling each digit in a cache, to handle those extremely large numbers.
"""
import math

# This first function deals with 3 digit nums only.
# Time complexity: it would be O(n), where n is the number of digits of the value parameter,
#   if the number of digits varied between inputs.
# However, in this case, n is always 3, so technically, time complexity O(3) simplifies to O(1).
# O(1) space.


def three_digit_num_is_armstrong_num(value: int) -> bool:
    initial_value = value
    total = 0
    remainder = 0
    while value > 0:
        # Get the digit currently in the ones place
        remainder = value % 10
        total += remainder**3
        # Take off the digit currently in the ones place
        value = value//10
    return initial_value == total

# This second one will take any number of digits.
# Time O(n) where n is the number of digits.
# Space O(1).


def num_is_armstrong_num(value: int) -> bool:
    initial_value = value
    total = 0
    remainder = 0
    power = math.floor(math.log(value, 10) + 1)
    while value > 0:
        remainder = value % 10
        total += remainder**power
        value = value//10
    return initial_value == total

# This one will be more time efficient, but a LITTLE less space efficient, due to the cache.
# Time O(n), where n is the number of digits of value.
# Technically, space might be O(1) still, though because cache will never be bigger than 9 slots (keys 0-9). However, the
#   values stored at those might be large enough to make a noticeable difference in memory usage.


def num_is_armstrong_num_with_cache(value: int) -> bool:
    cache = {}
    initial_value = value
    total = 0
    remainder = 0
    power = math.floor(math.log(value, 10) + 1)
    while value > 0:
        remainder = value % 10
        if remainder not in cache:
            cache[remainder] = remainder**power
        total += cache[remainder]
        value = value//10
    return initial_value == total


if __name__ == '__main__':

    # These should print in a true-true-true false-false-false pattern

    print(three_digit_num_is_armstrong_num(153))
    print(three_digit_num_is_armstrong_num(370))
    print(three_digit_num_is_armstrong_num(371))

    print(three_digit_num_is_armstrong_num(789))
    print(three_digit_num_is_armstrong_num(123))
    print(three_digit_num_is_armstrong_num(369))

    print(num_is_armstrong_num(153))
    print(num_is_armstrong_num(370))
    print(num_is_armstrong_num(371))

    print(num_is_armstrong_num(789))
    print(num_is_armstrong_num(123))
    print(num_is_armstrong_num(369))

    print(num_is_armstrong_num(1))
    print(num_is_armstrong_num(2))
    print(num_is_armstrong_num(3))

    print(num_is_armstrong_num(1632))
    print(num_is_armstrong_num(54758))
    print(num_is_armstrong_num(1741726))

    print(num_is_armstrong_num(1634))
    print(num_is_armstrong_num(54748))
    print(num_is_armstrong_num(1741725))

    print(num_is_armstrong_num_with_cache(1741726))
    print(num_is_armstrong_num_with_cache(
        115132219018763992465095597973971522401))
    print(num_is_armstrong_num_with_cache(
        12815792078366059955099570545496129367))

    print(num_is_armstrong_num_with_cache(
        12815792078366059955099770545296129367))
    print(num_is_armstrong_num_with_cache(
        115132219018763992565095597973971522400))
    print(num_is_armstrong_num_with_cache(
        115132219018763992565095597973971522401))
