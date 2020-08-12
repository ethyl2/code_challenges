"""
https://github.com/LambdaSchool/cs-module-project-hash-tables/tree/master/applications/sumdiff

Given a set of ints
and a function

f(x) = x * 4 + 6

What are the combinations of f(a) + f(b) == f(c) - f(d), where a,b,c,d are ints from the set?


For the above q, we get this sample output:

f(1) + f(1) = f(12) - f(7)    10 + 10 = 54 - 34
f(1) + f(4) = f(12) - f(4)    10 + 22 = 54 - 22
f(4) + f(1) = f(12) - f(4)    22 + 10 = 54 - 22
f(1) + f(7) = f(12) - f(1)    10 + 34 = 54 - 10
f(4) + f(4) = f(12) - f(1)    22 + 22 = 54 - 10
f(7) + f(1) = f(12) - f(1)    34 + 10 = 54 - 10
f(3) + f(3) = f(12) - f(3)    18 + 18 = 54 - 18
"""
# Need the cartesian product, to allow duplicates
from itertools import product

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Here's my implementation. Uses a cartesian product to get the combinations.
# Stores tuples of nums as keys, with sums and differences as values, to use and speed up the algorithm.


def sumdiff(num_set):
    lookup = {}
    sum_lookup = {}
    diff_lookup = {}

    for num in num_set:
        lookup[num] = f(num)

    combos = product(num_set, repeat=4)

    for group in combos:
        if (group[0], group[1]) not in sum_lookup:
            sum_lookup[(group[0], group[1])] = lookup[group[0]] + \
                lookup[group[1]]

        if (group[2], group[3]) not in diff_lookup:
            diff_lookup[(group[2], group[3])] = lookup[group[2]] - \
                lookup[group[3]]

        # if (lookup[group[0]] + lookup[group[1]] == lookup[group[2]] - lookup[group[3]]):
        if sum_lookup[(group[0], group[1])] == diff_lookup[(group[2], group[3])]:
            print(
                f'f({group[0]}) + f({group[1]}) = f({group[2]}) - f({group[3]})     {lookup[group[0]]} + {lookup[group[1]]} = {lookup[group[2]]} - {lookup[group[3]]}')


# sumdiff(q)

# Here is the given solution.
# It stores the sums and differences as keys, with the nums that result from them, as values.


def sumdiff2(num_set):
    sums = {}
    diffs = {}
    lookup = {}

    for num in num_set:
        lookup[num] = f(num)
        # print(lookup)

    for num1 in num_set:
        for num2 in num_set:
            total = lookup[num1] + lookup[num2]
            if total in sums:
                sums[total].append((num1, num2))
            else:
                sums[total] = [(num1, num2)]

            difference = lookup[num1] - lookup[num2]
            if difference in diffs:
                diffs[difference].append((num1, num2))
            else:
                diffs[difference] = [(num1, num2)]

    for sum_key in sums.keys():
        if sum_key in diffs.keys():
            for values_for_sum in sums[sum_key]:
                for values_for_diff in diffs[sum_key]:
                    group = (values_for_sum[0], values_for_sum[1],
                             values_for_diff[0], values_for_diff[1])
                    print(
                        f'f({group[0]}) + f({group[1]}) = f({group[2]}) - f({group[3]})     {lookup[group[0]]} + {lookup[group[1]]} = {lookup[group[2]]} - {lookup[group[3]]}')


sumdiff2(q)
