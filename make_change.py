"""
From algo expert 08-14-2020
Given a money amount and an array showing the kinds of denominations you have available,
return the number of ways you could make change.

Assume that you have an unlimited amount of each denomination.

Example: target = 10
        denominations = [1,5,10,15]
        Return: 4
        because you could return:
            1. ten 1s
            2. five 1s + one 5
            3. two 5s
            4. one 10

Dynamic programming!

His approach:
1. Make an array that holds all of the incremental amounts from 0 up to your target -- the indices will represent the amounts. 
    So make an array of length target + 1. We'll call it ways.
    _ _ _ _ _ _ _ _ _ _ _
    0 1 2 3 4 5 6 7 8 9 10

2. In ways, put 0 in all but the first index. (We consider there to be just 1 way to get 0 money.)

    1 0 0 0 0 0 0 0 0 0 0 0
    _ _ _ _ _ _ _ _ _ _  _ 
    0 1 2 3 4 5 6 7 8 9 10

3. Iterate through a nested loop that consists of 
    for each denomination, 
        for each index in ways.

    Each time, do a check comparing the denomination to the index in ways.
        If the denomination is greater than the amount represented by the index, 
        then there is no way to use that denomination to make change for that amount.)
        So if demonination > the index, just continue.
    Otherwise,
        update the value at ways[index] to be what was currently there + ways[index - denomination].
        This is probably the hardest thing for me to understand. But it works. 
            After the loop where 1 is the denomination, the 10 index holds 1 way.
                At that point, you could make change for 10 with ten 1s only.
            After the loop where 5 is the denomination, the 10 index holds 3 ways, because 10-5=5 and the 5 index's value is 2, so that is added.
                At that point, you could make change for 5 with five 1s or one 5.
                At that point, you could make change for 10 with ten 1s, five 1s + one 1, or two 5s.
            After the loop where 10 is the denomination, the 10 index holds 4 ways, because 10-10-0 and the 0 index's value is 1, so that is added.
                At that point, you could make change for 10 with ten 1s, five 1s + one 1, two 5s, or one 10.
4. Return ways[0].
"""
from typing import List


def make_change(target: int, denominations: List) -> int:
    ways = [0] * (target + 1)
    ways[0] = 1

    relevant_denominations = [
        denom for denom in denominations if denom <= target]

    for denom in relevant_denominations:
        for index in range(1, len(ways)):
            if denom <= index:
                ways[index] += ways[index-denom]
            print(f'denom: {denom:{2}}, index: {index:{2}}, {ways= }')
    return ways[0]


print(make_change(10, [1, 5, 10, 15]))
