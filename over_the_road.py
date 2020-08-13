"""
TODO: finish this.

https://www.codewars.com/kata/5f0ed36164f2bc00283aed07
Given n, the number of houses on either side of a road. And address, the house number. Return the house number on the opposite side of the street.
On the street, evens increase on the right,
    odds decrease on the left.
Every number is used.

Example:
1   6
3   4
5   2

over_the_road(address, n)
over_the_road(1, 3) = 6
over_the_road(3, 3) = 4
over_the_road(2, 3) = 5
over_the_road(3, 5) = 8

Thoughts:
total number of addresses = n*2
left side: odds from 1 to (n*2) - 1
right side: evens from n*2 to 2

maybe determine how many rows down the address is
then do math to figure out the opposite house address, based on the num rows
"""


def over_the_road(address, n):
    row_num = 0
    if address % 2 != 0:
        # address is odd
        row_num = (address + 1) // 3
        print(row_num)

    if address % 2 == 0:
        # address is even
        row_num = (n*2 - address) // 2
        print(row_num)


'''
print(over_the_road(1, 3))
print(over_the_road(3, 3))
print(over_the_road(5, 3))

# print(over_the_road(2, 3))
# print(over_the_road(4, 3))
# print(over_the_road(6, 3))
'''
'''
1   12
3   10
5   8
7   6
9   4
11  2
'''
'''
print(over_the_road(1, 6)) # row 0
print(over_the_road(3, 6))  # row 1
print(over_the_road(5, 6))  # row 2

print(over_the_road(2, 6))  # row 5
print(over_the_road(4, 6))  # row 4
print(over_the_road(6, 6))  # row 3
'''
'''
1   10
3   8
5   6
7   4
9   2
'''

print(over_the_road(1, 5))  # row 0
print(over_the_road(3, 5))  # row 1
print(over_the_road(5, 5))  # row 2
print(over_the_road(7, 5))  # row 3
print(over_the_road(9, 5))  # row 4

print(over_the_road(2, 5))  # row 4
print(over_the_road(4, 5))  # row 3
print(over_the_road(6, 5))  # row 2
print(over_the_road(8, 5))  # row 1
print(over_the_road(10, 5))  # row 0
