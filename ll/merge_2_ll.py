"""
https://app.codesignal.com/interview-practice/task/6rE3maCQwrZS3Mm2H/description

Given 2 sll in non-decreasing order. (the heads of the slls)
Return a sll that contains the els from the 2 lists, in non-decreasing order

1 -> 2 -> 3
and
4 -> 5 -> 6
return
1 -> 2 -> 3 -> 4 -> 5 -> 6

One more example:

1 -> 1 -> 2 -> 4
0 -> 3 -> 5
return
0 -> 1 -> 1 -> 2 -> 3 -> 4 -> 5
"""


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def mergeTwoLinkedLists(l1, l2):
    # Edge cases
    if l1 == None and l2 != None:
        return l2
    if l2 == None and l1 != None:
        return l1
    if l1 == None and l2 == None:
        return None

    # Start a new sll for the output
    if l1.value <= l2.value:
        new_list = ListNode(l1.value)
        l1 = l1.next
    else:
        new_list = ListNode(l2.value)
        l2 = l2.next

    # Store the head in a variable to return later
    new_head = new_list

    # While there are elements in both slls, compare the current nodes of each.
    # Add the smallest one to the new sll, connected to the prev node of the new sll
    # and move to the new node of the winning sll
    while l1 and l2:
        if l1.value < l2.value:
            new_node = ListNode(l1.value)
            l1 = l1.next
        else:
            new_node = ListNode(l2.value)
            l2 = l2.next
        new_list.next = new_node
        new_list = new_node

    # Add the leftovers of whatever sll was left
    while l1:
        new_node = ListNode(l1.value)
        new_list.next = new_node
        new_list = new_node
        l1 = l1.next

    while l2:
        new_node = ListNode(l2.value)
        new_list.next = new_node
        new_list = new_node
        l2 = l2.next

    return new_head
