"""
https://www.codewars.com/kata/5552101f47fc5178b1000050/python

given positive integer n and positive integer p,
find k, if it exists, in which n*k = (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...)
If it doesn't exist, return -1

dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
"""


def dig_pow(n, p):
    total = 0
    power = p
    for digit in str(n):
        total += int(digit)**power
        power += 1
    if total % n == 0:
        return int(total/n)
    else:
        return -1


def dig_pow2(n, p):
    total = 0
    for i, digit in enumerate(str(n)):
        total += pow(int(digit), p+i)
    return int(total/n) if total % n == 0 else -1


print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(695, 2))
print(dig_pow2(46288, 3))
