"""
https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

Given a string of ints,
return a string in which they are ordered:
1. by the sum of their digits, low to high.
2. In case of a tie, by how they are ordered when treated as strings.
"""


def order_weight(strng: str) -> str:
    nums = strng.split()
    # print(nums)
    totals = []
    for num in nums:
        digits_sum = sum([int(char) for char in num])
        # print(digits_sum)
        totals.append((num, digits_sum))
    # print(totals)
    totals.sort(key=lambda x: [x[1], x[0]])
    # print(totals)
    output = ' '.join([total[0] for total in totals])
    # print(output)
    return output


print(order_weight("103 123 4444 99 2000"))
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
print(order_weight(''))
