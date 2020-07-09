'''
https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python
Given customers <- an array of pos ints representing a queue of customers. 
    The num is the time that customer takes to check out.
and n <- number of checkout tills.
Return the total time necessary for all customers to check out.
'''


def queue_time(customers, n):
    # If n is 1, just return the sum of the customers
    if n == 0:
        return sum(customers)
    # Initialize tills dict

    tills = {}
    for i in range(n):
        tills[i] = 0

    # Loop through customers
    while len(customers) > 0:
        # Find till with min value
        min_value = min(tills.values())
        min_key = [key for key, value in tills.items() if value ==
                   min_value][0]

        # Place customer in it
        tills[min_key] += customers[0]
        customers.remove(customers[0])

    # Return till with max sum
    return max(tills.values())


print(queue_time([5, 3, 4], 1))  # < - 12
print(queue_time([10, 2, 3, 3], 2))  # < - 10
print(queue_time([2, 3, 10], 2))  # < - 12

# Donald Whitely's version with recursion:


def queue_time_recursive(customers, n, tills=None):
    if len(customers) == 0:
        if tills is not None:
            current_max = max(tills.keys(), key=(lambda k: tills[k]))
            return tills[current_max]
        return 0
    if tills is None:
        tills = {}
    if len(tills) == 0:
        if n > 1:
            for i in range(n):
                tills[i] = 0
        else:
            tills[0] = 0
    current_key = min(tills.keys(), key=(lambda k: tills[k]))
    tills[current_key] += customers[0]
    return queue_time_recursive(customers[1:], n, tills)


print(queue_time_recursive([5, 3, 4], 1))  # < - 12
print(queue_time_recursive([10, 2, 3, 3], 2))  # < - 10
print(queue_time_recursive([2, 3, 10], 2))  # < - 12
