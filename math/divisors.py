"""
https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python

Given an int, return list with all of its divisors (besides 1 and the number itself).
If int is prime, return  f"{int} is prime"
https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python

Examples:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
"""


def divisors(integer: int):

    output = []
    for i in range(2, integer):
        if integer % i == 0:
            output.append(i)

    return output if len(output) else f"{str(integer)} is prime"


def divisors_concise(integer: int):
    """
    Same as above, except I used a list comprehension
    """
    output = [i for i in range(2, integer) if integer % i == 0]
    return output if len(output) else f"{str(integer)} is prime"


def divisors_more_concise(integer: int):
    """
    Here's what someone else did, using 'or' to conditionally return
    """
    return [i for i in range(2, integer) if not integer % i] or '%d is prime' % integer


print(divisors_more_concise(12))
print(divisors(25))
print(divisors(13))
