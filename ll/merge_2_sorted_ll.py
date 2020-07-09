"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

from leetcode
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # My first approach. It is O(n+m) time and O(n+m) space, where n is length of l1 and m is length of l2.
    # So not bad for time, but I could do better with space.
    # O(n+m) space because it creates a new sll, with length n+m.
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Edge cases
        if l1 == None and l2 != None:
            return l2
        if l2 == None and l1 != None:
            return l1
        if l1 == None and l2 == None:
            return None

        # Set the head of the new ll
        if l1.val <= l2.val:
            new_node = ListNode(l1.val)
            l1 = l1.next
        else:
            new_node = ListNode(l2.val)
            l2 = l2.next

        head = new_node

        # Go through the ll's to determine what should be linked next
        while l2 and l1:
            if l1.val <= l2.val:
                newest_node = ListNode(l1.val)
                l1 = l1.next
            else:
                newest_node = ListNode(l2.val)
                l2 = l2.next
            new_node.next = newest_node
            new_node = newest_node

        # Now that only 1 ll is left to go through, go ahead and add all of its nodes
        while l1:
            newest_node = ListNode(l1.val)
            new_node.next = newest_node
            new_node = newest_node
            l1 = l1.next

        while l2:
            newest_node = ListNode(l2.val)
            new_node.next = newest_node
            new_node = newest_node
            l2 = l2.next

        # print(head.val)
        return head

    # Another approach that Beej suggested as a possibility. O((n+m) log (n+m)) time, because of the sorting,
    # so time complexity isn't optimal.
    # O(n+m) space.
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Edge cases
        if l1 == None and l2 != None:
            return l2
        if l2 == None and l1 != None:
            return l1
        if l1 == None and l2 == None:
            return None

        # Stick all values of both slls into a list
        big_list = []
        curr = l1
        while curr:
            big_list.append(curr.val)
            curr = curr.next
        curr = l2
        while curr:
            big_list.append(curr.val)
            curr = curr.next
        # print(big_list)

        # Sort the list
        big_list.sort()

        # Turn the list into a sll
        new_head = ListNode(big_list[0])
        prev = new_head
        curr = ListNode(big_list[1])
        for i in range(2, len(big_list)):
            prev.next = curr
            prev = curr
            curr = ListNode(big_list[i])
        prev.next = curr

        # Return the head
        return new_head

    # A better approach that is in-place, just reassigns the next pointers instead of making new ListNodes.
    # Time O(n+m), Space O(1)
    def mergeTwoLists3(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Edge cases
        if l1 == None and l2 != None:
            return l2
        if l2 == None and l1 != None:
            return l1
        if l1 == None and l2 == None:
            return None

        # Determine which head should still be the head.
        # And create 2 pointers, one for each list, pointing to the nodes we will compare.
        if l1.val <= l2.val:
            new_head = l1
            pointer1 = l1.next
            pointer2 = l2
        else:
            new_head = l2
            pointer1 = l1
            pointer2 = l2.next

        # Create a prev variable. Initiatize it to be the head.
        prev = new_head

        # While both pointers are not None:
        while pointer1 and pointer2:
            #   compare their values. The smaller one (or the first one if it's a tie) becomes the next node
            if pointer1.val <= pointer2.val:
                prev.next = pointer1
                prev = pointer1
                pointer1 = pointer1.next
            else:
                prev.next = pointer2
                prev = pointer2
                pointer2 = pointer2.next

        # Add the remaining nodes
        while pointer1:
            prev.next = pointer1
            prev = pointer1
            pointer1 = pointer1.next

        while pointer2:
            prev.next = pointer2
            prev = pointer2
            pointer2 = pointer2.next

        # Return the head.
        return new_head


tail1 = ListNode(4, None)
node2 = ListNode(2, tail1)
head1 = ListNode(1, node2)

tail2 = ListNode(4, None)
node5 = ListNode(3, tail2)
head2 = ListNode(1, node5)

s = Solution()
current_node = s.mergeTwoLists(head1, head2)
# current_node = s.mergeTwoLists2(head1, head2)
# current_node = s.mergeTwoLists3(head1, head2)


while current_node:
    print(current_node.val)
    current_node = current_node.next
