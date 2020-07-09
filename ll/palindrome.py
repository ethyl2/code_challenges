"""
From Kapil Sharma's lecture 6-23-2020
"Determine if a linked list is a palindrome"

More info: For this challenge, the linked list is a sll. The values stores are ints.

1 -> 3 -> 5 -> 3 -> 1 is a palindrome

"""
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# First version. Time O(n) b/c O(2n) simplifies to O(n). Space O(n)


def is_palindrome(node):
    if node is None:
        return False  # or what you determine should be returned

    # Make a reversed copy
    reversed_head = make_reversed_copy(node)

    # See if the reversed copy's data values are equal to the original sll.
    return are_values_equal(node, reversed_head)


def make_reversed_copy(node):
    head = None
    while node is not None:
        new_node = Node(node.data)
        next_node = node.next
        new_node.next = head
        head = new_node
        node = next_node
    return head


def are_values_equal(original, reversed):
    while original is not None and reversed is not None:
        if original.data != reversed.data:
            return False
        original = original.next
        reversed = reversed.next
    return True

# Second version. Time O(n). At least, only 1 traversal this time.
# Space O(n/2) simplifies to O(n).
# This version uses a stack.
# We traverse thru the sll, adding data values to the stack.
# Once we get past the middle, we pop a value off the stack and compare it to the current data value.
# We can tell when we've (the slow pointer) made it to the middle
# when our faster pointer reaches the end.


def is_palindrome2(node):
    stack = deque()
    slow = node
    fast = node
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    # To deal with slls that have an odd length:
    # When the slls have an odd length, the fast pointer will end up at the end.
    # (With even, the fast pointer ends up as None.)
    # If odd, move slow one more time, to get over the middle node.
    if fast is not None:
        slow = slow.next

    # Now, start comparing
    while slow:
        if stack.pop() != slow.data:
            return False
        slow = slow.next
    return True

# This version below, from Joshua Hill, uses O(1) space. O(n) time.


def is_palindrome3(head: Node) -> bool:
    fast = slow = head
    # find mid, make slow reference mid.
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse the rest of the list, from slow to the end
    node = None
    while slow:
        nxt = slow.next
        slow.next = node
        node = slow
        slow = nxt

    # check if original list is equal to reversed list
    while node:
        if head.data != node.data:
            return False
        node = node.next
        head = head.next
    return True

#  Testing


# 1 -> 3 -> 5 -> 4 -> 1 odd, not a palindrome
node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(4)
node5 = Node(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# print(is_palindrome(node1))
# print(is_palindrome2(node1))
print(is_palindrome3(node1))

# 1 -> 3 -> 5 -> 3 -> 1 odd, palindrome
node01 = Node(1)
node02 = Node(3)
node03 = Node(5)
node04 = Node(3)
node05 = Node(1)
node01.next = node02
node02.next = node03
node03.next = node04
node04.next = node05

# print(is_palindrome(node01))
# print(is_palindrome2(node01))
print(is_palindrome3(node01))

# 1 -> 3 -> 3 -> 4 # even, not a palindrome
node0001 = Node(1)
node0002 = Node(3)
node0003 = Node(3)
node0004 = Node(4)
node0001.next = node0002
node0002.next = node0003
node0003.next = node0004
# print(is_palindrome(node0001))
# print(is_palindrome2(node0001))
print(is_palindrome3(node0001))

# 1 -> 3 -> 3 -> 1 # even, palindrome
node001 = Node(1)
node002 = Node(3)
node003 = Node(3)
node004 = Node(1)
node001.next = node002
node002.next = node003
node003.next = node004
# print(is_palindrome(node001))
# print(is_palindrome2(node001))
print(is_palindrome3(node001))
