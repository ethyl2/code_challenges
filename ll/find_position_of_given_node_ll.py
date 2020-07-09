"""
From Kapil Sharma's lecture 11 Jun 2020

Given the head of a sll and a node, return its index (position).
Assume that indexing starts at 0.
Return -1 if index is not found.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_index(head, node):
    # Edge cases
    if head == None or node == None:
        return -1
    if head == node:
        return 0

    position = 0
    curr = head

    # Iterate thru sll until node is found or reach tail
    while curr is not None and curr != node:
        curr = curr.next
        position += 1

    # If node is not found
    if curr == None:
        return -1

    # If node is found
    return position


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

node4 = Node(4)


def print_ll(head):
    ll_list = []
    curr = head
    while curr is not None:
        ll_list.append(curr.data)
        curr = curr.next
    print(ll_list)
    return ll_list


try:
    print_ll(node1)
    print(find_index(node1, node1))  # 0
    print(find_index(node1, node2))  # 1
    print(find_index(node1, node3))  # 2
    print(find_index(node1, node4))  # -1
    print(find_index(node1, node5))  # Exception
except Exception:
    print("node does not exist")
