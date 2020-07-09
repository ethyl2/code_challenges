"""
***  Still in progress ***
https://app.codesignal.com/interview-practice/task/XP2Wn9pwZW6hvqH67/description

Given a sll (l),
reverse is nodes k at a time.
Return the modified list.
O(n) time complexity,
O(1) additional space complexity.

If the num of nodes in the sll is not a muliple of k, the nodes that are left at the end should remain as-is.
You can't alter the values in the nodes -- only the nodes themselves can be changed.

l = 1 -> 2 -> 3 -> 4 -> 5, k = 2
return
2 -> 1 -> 4 -> 3 -> 5
"""
# Make a variable to store current value of how many nodes you've visited - k, num_visited.
# Loop thru sll
# If num_visited < k:
# reassign next pointers to link node backwards
# If num_visited == k:
# don't reassign pointer
# reset num_visited

# How to deal with the nodes at the end??
# Maybe if we end where num_visited != k:
# Back up to fix the pointers back to original for the leftover nodes.


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def reverseNodesInKGroups(l, k):
    # Edge case
    if k == 1:
        return l

    curr = l
    num_visited = 0
    prev = None
    group_head = None

    while curr:
        print("Curr node: " + str(curr.value))
        num_visited += 1
        print("Num_visited: " + str(num_visited))
        if num_visited == 1:
            print("At start of group")
            prev = curr
            curr = curr.next
            group_head = curr

        elif num_visited < k:
            print("In the middle")
            next_node = curr.next
            curr.next = prev
            prev = curr.next
            curr = next_node
        else:
            print("num_visited == k")
            next_node = curr.next
            curr.next = prev
            curr = next_node
            prev = group_head
            num_visited = 0

    return l


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

result = reverseNodesInKGroups(node1, 3)
curr = result

print('results: ')
'''
while curr:
    print(curr.value)
    curr = curr.next
'''
print(curr.value)
print(curr.next.value)
