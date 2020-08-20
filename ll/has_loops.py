"""
From Kapil Sharma's lecture 08-20-2020

'Given a linked list, found out if it has any loops.'

His question: Why would it be helpful to know whether a linked list is cyclic?
    Some reasons include:
    1. You might get stuck in an infinite loop trying to traverse it.
    2. You might not be able to add to it.

Example of acyclic linked list: 1 -> 3 -> 5 -> 8

Example of cyclic linked list: 1 -> 3 -> 5 -> 8
                                    ^         |
                                    |         | 
                                    ----------

First step: create a Node class. Then make sure with the interviewer that your implementation aligns with what they wanted it to look like.
Second: create two pointers, a fast one that skips ahead 2 nodes at a time, and a slow one that visits each node, advancing one at a time.
    If the pointers ever point to the same node, we will know that the linked list is cyclic.
    If the pointers ever point to None, we will know that the linked list is acyclic.
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    # O(n) time, where n is the length of the linked list.
    # O(1) space
    def is_cyclic(self):
        slow = self
        fast = self
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    # This second version uses a set instead. Less space efficient.
    # O(n) time, where n is the length of the linked list.
    # O(n) space because of the set.
    def is_cyclic_with_set(self):
        visited = set()
        current_node = self
        while current_node != None:
            if current_node in visited:
                return True
            visited.add(current_node)
            current_node = current_node.next
        return False


if __name__ == "__main__":

    fourth_node = Node(8)
    third_node = Node(5, fourth_node)
    second_node = Node(3, third_node)
    first_node = Node(1, second_node)

    print(first_node.is_cyclic())
    print(first_node.is_cyclic_with_set())

    fourth_node.next = second_node

    print(first_node.is_cyclic())
    print(first_node.is_cyclic_with_set())
