"""
From Sean Chen lecture 08-05-2020
https://leetcode.com/problems/invalid-transactions/

Given a list of transactions, each a string with format "{name},{time},{amount},{city}".
Return the transactions that could be invalid,
    which means that the amount exceeds $1000
    or it occurs within (and including) 60 minutes of another transaction with the same name, different city.

They can be returned in any order.

Examples: 

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]

"""
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        output = set()
        lookup = dict()
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')

            if int(amount) > 1000:
                output.add(transaction)

            if name not in lookup:
                lookup[name] = [transaction]

            else:
                lookup[name].append(transaction)
                users_transactions = lookup[name]
                for users_transaction in users_transactions:

                    users_transaction_list = users_transaction.split(',')
                    if city != users_transaction_list[3]:
                        if abs(int(time) - int(users_transaction_list[1])) <= 60:
                            output.add(transaction)
                            output.add(users_transaction)
        return list(output)

    # This version experiments with a nested dictionary.
    # It excludes looping through elements that have the same name & same city.
    # But it doesn't seem to be much more efficient.
    def invalidTransactions2(self, transactions: List[str]) -> List[str]:
        output = set()
        lookup = dict()

        for transaction in transactions:
            name, time, amount, city = transaction.split(',')

            if int(amount) > 1000:
                output.add(transaction)

            if name not in lookup:
                lookup[name] = {city: [transaction]}
            else:
                if city in lookup[name]:
                    lookup[name][city].append(transaction)
                    for current_city, cities_transactions in lookup[name].items():
                        if current_city != city:
                            for current_cities_transaction in cities_transactions:
                                cct_list = current_cities_transaction.split(
                                    ',')
                                if abs(int(time) - int(cct_list[1])) <= 60:
                                    output.add(transaction)
                                    output.add(current_cities_transaction)
                else:
                    for current_city, cities_transactions in lookup[name].items():
                        for current_cities_transaction in cities_transactions:
                            cct_list = current_cities_transaction.split(
                                ',')
                            if abs(int(time) - int(cct_list[1])) <= 60:
                                output.add(transaction)
                                output.add(current_cities_transaction)
                    lookup[name].update({city: [transaction]})

        return(output)


s = Solution()

# ["bob,50,1200,mtv"]
# print(s.invalidTransactions2(["alice,20,800,mtv", "bob,50,1200,mtv"]))
# print(s.invalidTransactions2(
#    ["alice,20,800,mtv", "bob,50,1200,mtv", "alice,20,700,mtv"]))

# ["alice,20,800,mtv","alice,50,100,beijing"]
# print(s.invalidTransactions2(["alice,20,800,mtv", "alice,50,100,beijing"]))

# ["alice,50,1200,mtv"]
# print(s.invalidTransactions2(["alice,20,800,mtv", "alice,50,1200,mtv"]))
