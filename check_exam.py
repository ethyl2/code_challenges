"""
https://www.codewars.com/kata/5a3dd29055519e23ec000074

Given an array with answers to an exam. Elements are strings.
And a 2nd array with a student's answers. Same length.
Both arrays are not empty.

Return the score, with +4 for each correct answer, -1 for each wrong answer,
and 0 for ''.

If the score is < 0, return 0.

Examples: 
checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) → 6
checkExam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) → 7
checkExam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) → 16
checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) → 0
"""


def check_exam(arr1, arr2):
    '''
    total = 0
    for i, ans in enumerate(arr1):
        if ans == arr2[i]:
            total += 4
        elif arr2[i] != '':
            total -= 1

    '''
    # List comprehension instead
    '''
    total = sum([4 if arr1[i] == arr2[i] else 0 if arr2[i]
                 == '' else -1 for i in range(len(arr1))])
    return total if total > 0 else 0
    '''
    # Even more concise
    return max(0, sum([4 if arr1[i] == arr2[i] else 0 if arr2[i]
                       == '' else -1 for i in range(len(arr1))]))


print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))
print(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]))
print(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]))
print(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]))
