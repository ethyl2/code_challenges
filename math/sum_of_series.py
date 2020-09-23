"""
https://www.codewars.com/kata/555eded1ad94b00403000071/train/python

Your task is to write a function which returns the sum of following series upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
Rules:
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return 0.00

You will only be given Natural Numbers as arguments.

Examples:
SeriesSum(1) => 1 = "1.00"
SeriesSum(2) => 1 + 1/4 = "1.25"
SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"
"""


def series_sum(n: int) -> str:
    if n == 0:
        return '0.00'
    total = 1
    denominator = 4
    for i in range(1, n):
        total += (1/denominator)
        denominator += 3
    return "{:.2f}".format(total)


print(series_sum(1))
print(series_sum(2))
print(series_sum(5))
