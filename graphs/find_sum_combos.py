"""
From Kapil Sharma's lecture 6-25-2020

Given a set of candidate numbers (integers, with no duplicates) called candidates,
and a target sum (an integer) called target,
find all unique combinations of candidates where the candidate numbers sum up to the target.

All numbers (including target) will be positive integers.
The same candidate number can be used an unlimited number of times in a combination that is returned.
The solution set must not contain duplicate combinations.

Example: 
    given candidates [2,3,7] and target 7, return [[2,3,7], [7]]

More info: We decided that the solution set will be a nested list.
And that if either parameter is None, we will return an empty list.

This problem can be visualized as a graph.  

Example of how each node is represented in my drawing: 
    2 (5-2=3)
    The first 2 here is the candidate.
    5 is the current target, at this point in traversing the graph.
    Subtract the candidate from the current target, to see if the result is
        either 0 (which indicates we've found a winning combination)
        or if it is less than the candidate (which indicates it's time to break).
        Otherwise, continue the traversal downwards.
      
                                   
        2 (7-2=5)     -         3 (7-3=4)   -   7 (7-7=0)
      /         \               /       
    2 (5-2=3)    3 (5-3=2)     3 (4-3=1)                    
   /         \          
2 (3-2=1)     3 (3-3=0) 

Note: we need to sort the candidates, from low to high.
We will use DFS.
TODO: Figure out time and space complexity.
"""


def find_sum_combinations(candidates, target):
    result = []
    # base case:
    if candidates == None or target == None:
        return result

    candidates.sort()
    combination = []
    level = 0
    find_sum_combination_at_given_level(
        result, combination, candidates, target, level)
    return result


def find_sum_combination_at_given_level(result, combination, candidates, target, level):
    if target == 0:
        result.append(combination.copy())
        return
    for i in range(level, len(candidates)):
        if candidates[i] > target:
            break
        combination.append(candidates[i])
        new_target = target - candidates[i]
        find_sum_combination_at_given_level(
            result, combination, candidates, new_target, i)
        combination.pop()


print(find_sum_combinations([3, 7, 2], 7))

print(find_sum_combinations([1, 3, 2], 5))

print(find_sum_combinations([], 7))
print(find_sum_combinations([3, 4, 5], None))
