"""
https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python

Given an array of arrays. Each inner array has 2 integers, representing the number of people getting on,
and then getting off, the bus, at a bus stop.
Return number of people left on bus at the end.

Sample tests: 
test.assert_equals(number([[10,0],[3,5],[5,8]]),5)
test.assert_equals(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]),17)
test.assert_equals(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]),21)
"""


def number(bus_stops):
    total = 0
    for bus_stop in bus_stops:
        total += (bus_stop[0]-bus_stop[1])
    return total


def number2(bus_stops):
    return sum([bus_stop[0]-bus_stop[1] for bus_stop in bus_stops])


print(number2([[10, 0], [3, 5], [5, 8]]))
print(number2([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]))
print(number2([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]))
