"""
Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy?
prices = list of prices
k = amount he can spend

7
1 12 5 111 200 1000 10 -> 4
"""

# Sort prices lowest to highest
# initialize variable to hold money spent
# initialize variable num_items
# Loop thru array
#   Add price to money_spent if money_spent would not go above k and increment num_items
#   If price would make it go over k, return num_items


def maximumToys(prices, k):
    prices.sort()
    print(prices)

    money_spent = 0
    num_items = 0
    for price in prices:
        if money_spent + price <= k:
            num_items += 1
            money_spent += price
        else:
            return num_items


print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))
