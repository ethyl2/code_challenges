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
                    if city != users_transaction[3]:
                        if abs(int(time) - int(users_transaction[1])) <= 60:
                            output.add(transaction)
                            output.add(users_transaction)
        return list(output)


s = Solution()
# ["bob,50,1200,mtv"]
# print(s.invalidTransactions(["alice,20,800,mtv", "bob,50,1200,mtv"]))
print(s.invalidTransactions(["alice,20,800,mtv", "alice,50,100,beijing"]))
