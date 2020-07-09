"""
Hackerrank test #1
Given head of ll
and int k

Remove the kth node from the end of a linked list and return the head

If k > len(ll)  return head without modifying anything

Optimal is O(n) runtime and O(1) space.
"""


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# My first approach, the one I submitted. Time O(2n) -> O(n). Space O(1).


def removeKthLinkedListNode(head, k):
    # edge cases
    if head is None:
        return None

    # Determine length of ll
    length = 1
    curr = head
    while curr.next:
        length += 1
        curr = curr.next
    # print(length)

    # If k > length:
    # return head
    if k > length:
        print("k > length")
        return head

    # If k == length, return the next node
    if k == length:
        return head.next

    # Progress until length - k - 1 This will get us to the node before the kth node from end.
    distance = length - k - 1
    # Reset curr
    curr = head
    while distance > 0:
        curr = curr.next
        distance -= 1
    # Reassign next pointers to skip over kth node from end.
    curr.next = curr.next.next

    return head


# Second approach.
# Time complexity is a little better -- because it doesn't need 2 traversals.
# Time O(n). Space O(1).


def removeKthLinkedListNode2(head, k):
    if head is None:
        return None
    # Set up 2 pointers, current aka curr, and end_finder
    curr = head
    end_finder = curr
    # Move end_finder to be k spaces ahead of curr
    while k > 0:
        # If k > length of ll:
        if end_finder is None:
            return head
        # Otherwise, continue traversal
        end_finder = end_finder.next
        k -= 1

    # Case where kth index from end is the head:
    if end_finder is None:
        return head.next

    # Traverse until the end_finder is one place before the end of the ll
    while end_finder.next:
        curr = curr.next
        end_finder = end_finder.next
    # Now we are at one place before k from the end.
    # Reassign pointers to skip over the kth node from the end.
    curr.next = curr.next.next

    return head


# Testing

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
result = removeKthLinkedListNode2(node1, 2)
print(result.value)


def print_ll(head):
    ll_list = []
    curr = head
    while curr is not None:
        ll_list.append(curr.value)
        curr = curr.next
    print(ll_list)
    return ll_list


print_ll(result)
