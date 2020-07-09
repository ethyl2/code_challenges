"""
From Kapil Sharma's lecture 9 Jun 2020

Given the index of a node, and the head of linked list, delete the node at that index.

Singly-linked list
Return True if successful; False if not.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def delete_node(index, head):

    # Edge case
    if head == None:
        return False

    # Current node as we loop along the sll
    temp = head

    # Pointer to keep track of position as we loop along the sll
    track = 0

    # Loop until temp becomes None or track is one less than the desired index
    while temp != None and track < index - 1:
        temp = temp.next
        if temp == None or temp.next == None:
            return False
        track += 1

    # Now that we're out of the loop, temp.next should be the node at our desired index.
    # Skip the node at temp.next by assigning temp's next property to be the next.next instead.
    temp.next = temp.next.next
    return True

# Trying it out:


# Removing a middle node
# 1 -> 2 -> 3
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

delete_node(1, node1)
print(node1.value)
print(node1.next.value)
try:
    print(node1.next.next.value)
except AttributeError:
    print("End of sll")

# Removing a tail
# 1 -> 3 -> 4
node4 = Node(4)
delete_node(2, node1)
print(node1.value)
print(node1.next.value)
try:
    print(node1.next.next.value)
except AttributeError:
    print("End of sll")

# Removing a head
# 1 -> 3
delete_node(0, node1)
try:
    print(node1.next.value)
except AttributeError:
    print("Old head is no longer connected to rest of sll")

# Edge cases
print(delete_node(0, None))  # when head is None
print(delete_node(3, node3))  # when index is out of range
