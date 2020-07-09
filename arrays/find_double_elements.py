"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?
Input:
[4,3,2,7,8,2,3,1]
Output: 
[2,3]

My questions: Does the output order matter?
I assume the elements have to appear exactly twice? There never will be 3x.
"""

# First-pass would be to solve it with a dictionary, but it wouldn't be O(1) space complexity.
# This is O(n) time (if the order doesn't matter, O(n log n) if it does) and O(n) space.


def find_double_elements(my_list):
    lookup = {}
    for num in my_list:
        if num in lookup:
            lookup[num] += 1
        else:
            lookup[num] = 1
    # Note: use sorted() only if order does matter
    print(sorted([key for (key, value) in lookup.items() if value == 2]))
    return sorted([key for (key, value) in lookup.items() if value == 2])

# Another variation that is O(n) time but O(n) space


def find_double_elements4(my_list):
    lookup = set()
    output = []
    for num in my_list:
        if num in lookup:
            output.append(num)
        else:
            lookup.add(num)
    return output

# A little better. This one gets rid of the output list, and just modifies the input list


def find_double_elements5(my_list):
    lookup = set()
    pointer = 0
    while pointer < len(my_list):
        curr = my_list[pointer]
        if curr in lookup:
            pointer += 1
        else:
            lookup.add(curr)
            del my_list[pointer]

    return my_list


# Another solution is still not optimal. It uses sort, so it has O(n log n) runtime.
# It does have O(1) space complexity, though.


def find_double_elements2(my_list):
    my_list.sort()
    pointer = 0
    while pointer < len(my_list) - 1:
        if my_list[pointer] != my_list[pointer + 1]:
            del my_list[pointer]
        else:
            pointer += 1

    # print(my_list[:-1])
    return(my_list[:-1])

# Another posibility, but not optimal. Space is O(n).
# Time is not ideal at all because count() is O(n) and has to be called for each element.


def find_double_elements3(my_list):
    return list(set([x for x in my_list if my_list.count(x) == 2]))


#find_double_elements([4, 3, 2, 7, 8, 2, 3, 1])
print(find_double_elements5([4, 3, 2, 7, 8, 2, 3, 1]))

# Store history in each element somehow as we travese thru it? But how to not increase space complexity?
# Traverse twice should be okay -- b/c simplifies to O(n) - but probably not most ideal
