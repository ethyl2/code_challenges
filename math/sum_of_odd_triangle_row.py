"""
https://www.codewars.com/kata/55fd2d567d94ac3bc9000064

Considering a triangle made of odd numbers:
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...

Given a row, return the sum of that row.

Examples:
row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
"""


def row_sum_odd_numbers(n: int) -> int:
    '''
    My first approach. 2 outer loops.
    '''
    current_num = 1
    print(current_num)
    for i in range(2, n):
        print('row: ', i)
        for j in range(i):
            current_num += 2
            print(current_num)
    print('row: ', n)
    total = 0
    for i in range(n):
        current_num += 2
        print(current_num)
        total += current_num
    return total


def row_sum_odd_numbers2(n: int) -> int:
    '''
    My second approach. Combines the 2 outer loops from above into 1.
    '''
    current_num = 1
    total = 0
    print(current_num)
    for i in range(2, n+1):
        print('row: ', i)
        for j in range(i):
            current_num += 2
            print(current_num)
            if i == n:
                total += current_num

    return total


def row_sum_odd_numbers3(n: int) -> int:
    '''
    My third approach. A little more efficient.
    '''
    # Figure out how many elements are located before the nth row.
    num_elements_before = 0
    for i in range(1, n):
        num_elements_before += i

    # Figure out the value of the element right before the nth row starts.
    current_num = -1 + (2*num_elements_before)

    # Now sum up the values of the nth row.
    total = 0
    for i in range(n):
        current_num += 2
        total += current_num
    return total


def row_sum_odd_numbers4(n):
    '''
    And here's all that needed doing, all along! Oh well.
    '''
    return n ** 3


# print(row_sum_odd_numbers(4))
print(row_sum_odd_numbers2(4))
print(row_sum_odd_numbers3(4))
print(row_sum_odd_numbers4(4))
