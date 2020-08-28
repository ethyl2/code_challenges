"""
https://www.codewars.com/kata/563b662a59afc2b5120000c6

Given p0: initial population,
percent: the amount of growth each year (%)
aug: the number of new inhabitants per year that come to live in the town
p: the target population

Return the number of years it will take to reach the target population.

Examples:
nb_year(1500, 5, 100, 5000) -> 15
nb_year(1500000, 2.5, 10000, 2000000) -> 10
nb_year(1500000, 0.25, 1000, 2000000) -> 94
"""


def nb_year(po: int, percent: float, aug: int, p: int) -> int:
    years = 0
    while po < p:
        po += (po * percent / 100) + aug
        years += 1
    return years


print(nb_year(1500, 5, 100, 5000))
print(nb_year(1500000, 2.5, 10000, 2000000))

print(nb_year(1500000, 0.25, 1000, 2000000))
