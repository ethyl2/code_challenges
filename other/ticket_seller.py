"""
https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8
Given an array of customers, where each customer is represented by the denomination of money he has (a single 100, 50, or 25 dollar bill),
return 'YES' if the clerk can sell a ticket costing 25 dollars to each person and given them back the correct change. Otherwise, 'NO.'
He starts with no money.

Examples:
tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
"""
from typing import List


def tickets(people: List[int]) -> str:
    change_box = {}
    for denomination in people:
        if denomination in change_box:
            change_box[denomination] += 1
        else:
            change_box[denomination] = 1
        change_needed = denomination - 25
        if change_needed == 75:
            if 50 in change_box and change_box[50] >= 1 and 25 in change_box and change_box[25] >= 1:
                change_box[50] -= 1
                change_box[25] -= 1
            elif 25 in change_box and change_box[25] >= 3:
                change_box[25] -= 3
            else:
                return 'NO'
        elif change_needed == 25:
            if 25 in change_box and change_box[25] >= 1:
                change_box[25] -= 1
            else:
                return 'NO'
    return 'YES'


print(tickets([25, 25, 50]))
print(tickets([25, 100]))
print(tickets([25, 25, 50, 50, 100]))
