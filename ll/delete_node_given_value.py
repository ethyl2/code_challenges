"""
From Kapil Sharma's lecture 11 Jun 2020
Given the head of a sll and a value, delete the node with that value.
Return True if successful; False otherwise.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_node_given_value(value, head):
    # Edge cases
    if head == None or value == None:
        return False

    if head.data == value:
        head.next = None
        return True

    # Iterate thru sll until find the value or reach the tail
    prev = None
    curr = head
    while curr is not None and curr.data != value:
        prev = curr
        curr = curr.next

    # If reached tail w/o finding the value
    if not curr:
        return False

    # If found value, reassign the next pointer of prev node to skip node with the value
    prev.next = curr.next
    return True


def print_ll(head):
    ll_list = []
    curr = head
    while curr is not None:
        ll_list.append(curr.data)
        curr = curr.next
    print(ll_list)
    return ll_list


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

test = delete_node_given_value(2, node1)
print(test)  # True
print_ll(node1)  # Should be only 1 and 3


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
test2 = delete_node_given_value(1, node1)
print(test2)  # True
print_ll(node1)  # Should just show the 1 because it is not detached from the sll
print_ll(node2)  # Now 2 is the head

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
test3 = delete_node_given_value(3, node1)
print(test3)  # True
print_ll(node1)  # Should just show tail is gone

node4 = Node(4)
test4 = delete_node_given_value(4, node1)
print(test4)  # Should be False b/c no node with value of 4 exists in sll
