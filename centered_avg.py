"""
from codingbat.com and PT lecture

Return centered avg of array, which excludes min and max value (one instance of each) and is the mean avg (int division)
of the rest of the list.
"""


def find_centered_avg(arr):
    min_value = min(arr)
    max_value = max(arr)
    return (sum(arr) - min_value - max_value) // (len(arr) - 2)


print(find_centered_avg([0, 2, 2, 4]))
