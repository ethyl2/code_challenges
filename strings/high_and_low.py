"""
https://www.codewars.com/kata/554b4ac871d6813a03000035

Given a string of space separated numbers, 
return a string of highest number + space + lowest number

Examples:
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
"""

# O(n) overall because 3 O(n)s: making the num_list, max(), and min()


def high_and_low(s):
    num_list = [int(num) for num in s.split(' ')]
    return f"{max(num_list)} {min(num_list)}"

# This second version uses sort, so not as time efficient: O(n log n), but the lookups for the max and min values are O(1)
# This could be easily modified to use sort() instead of sorted() for more memory efficiency.


def high_and_low2(s):
    num_list = sorted([int(num) for num in s.split(' ')])
    return f"{num_list[-1]} {num_list[0]}"


print(high_and_low2("1 2 3 4 5"))
print(high_and_low2("1 2 -3 4 5"))
print(high_and_low2("1 9 3 4 -5"))  # return "9 -5"
