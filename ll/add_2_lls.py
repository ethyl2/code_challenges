"""
From Kapil Sharma's lecture 9 Jun 2020

Given 2 singly-linked lists.
Each list represents a positive integer.
Each node in the slls represents a digit in the integer.
5 -> 7 -> 9 represents the integer 975
7 -> 6 represents the integer 67

Return the sum of the two integers, in the form of a sll.
2 -> 4 -> 0 -> 1 represents 1042
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# The function has an additional parameter named carry,
# which holds the second digit (in the tens position) that might result from
# adding 2 single-digit ints.
# 5
# + 7
# -------
# 12  so 1 will be carry in this example


def add_2_lls(l1, l2, carry=0):
    # base cases
    if l1 == None and l2 == None and carry == 0:
        return None

    # Create a variable to hold the sum. It is initialized at 0 the first time this function is called.
    # Later calls to the function will add carry to the total used during the call.
    total = carry

    # Add the value of l1 to total
    if l1 != None:
        total += l1.data

    # Add the value of l2 to total
    if l2 != None:
        total += l2.data

    # Create a new node to hold the ones digit of total. This will be part of the returned sll.
    result = Node(total % 10)

    # As long as there are still nodes in at least one of the slls, recursively call the function.
    # If the current node of a sll has a next, advance to the next node
    if l1 != None:
        l1 = l1.next
    if l2 != None:
        l2 = l2.next

    # Determine what carry should be
    if total >= 10:
        carry = 1
    else:
        carry = 0

    next_node_of_result = add_2_lls(l1, l2, carry)

    # attach next_node_of_result to the sll we will return
    result.next = next_node_of_result

    return result


# Testing this out
# 5 -> 7 -> 9 represents the integer 975

node1 = Node(5)
node2 = Node(7)
node3 = Node(9)

node1.next = node2
node2.next = node3

# 7 -> 6 represents the integer 67

node4 = Node(7)
node5 = Node(6)

node4.next = node5

test = add_2_lls(node1, node4)
curr = test
return_value = ''
while curr:
    return_value = str(curr.data) + return_value
    curr = curr.next
print(return_value)

'''
Note: Kapil used an outer and inner function for his version:
def add_2_lls(l1, l2):
    # Initialize carry to be 0 to start with.
    return add_2_lls_inner(l1, l2, 0)


def add_2_lls_inner(l1, l2, carry):
    etc.
'''

"""
For part 2 of the challenge, what if the order of the nodes is reversed from how they are ordered in the first
code challenge? So 5 -> 7 -> 9 represents the integer 579
Return the nodes reversed as well
"""

# Helper function to be used to get the slls back to the order expected in the above function.


def reverse_ll(head):
    if head == None or head.next == None:
        return head
    prev = None
    curr = head
    while curr is not None:
        # print(curr.data)
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# Main function to use when the input nodes are reversed


def add_2_lls_that_are_reversed(l1, l2, carry=0):
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    print_ll(l1)
    l1 = reverse_ll(l1)

    print_ll(l2)
    l2 = reverse_ll(l2)

    result = reverse_ll(add_2_lls(l1, l2))
    print_ll(result)
    return result

# Helps me to visualize a sll


def print_ll(head):
    ll_list = []
    curr = head
    while curr is not None:
        ll_list.append(curr.data)
        curr = curr.next
    print(ll_list)
    return ll_list

# To visualize whether the reverse_ll() was correctly written


def print_before_and_after_reverse_ll(head):
    print_ll(head)
    new_head = reverse_ll(head)
    print_ll(new_head)


# print_before_and_after_reverse_ll(node1)


# 579 + 76 = 655
print(add_2_lls_that_are_reversed(node1, node4).data)
