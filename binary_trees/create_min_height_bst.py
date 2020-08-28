"""
From algo expert

My gist: https://gist.github.com/ethyl2/6e5be4946f2bfce821c210f83ae4bd53

Given a non-empty sorted array of distinct integers, construct a BST with the smallest possible height.
Return the root of the BST.

You are given a BST class with an insert() method to use if you wish.

Example: array = [1,2,5,7,10,13,14,15,22]
An example of a minimal height BST of that array:

            10
           /  \
          5     15
         / \   / \
        2   7 14  22
       /      /
      1      13

Its height is 4.

Here's an example of a non-minimal height BST of that array:
             2
           /  \
          1     5
                 \
                  7
                   \
                   10
                    \
                    13
                     \
                      14
                       \
                        15
                          \
                          22
Its height is 8.


"""
from typing import List
import math


def minHeightBst(array: List[int]) -> List[int]:
    # Create the head of the entire BST
    middle_index = len(array)//2
    head = BST(array[middle_index])

    # Create its left and right sides
    head.left = create_node(array[:middle_index])
    head.right = create_node(array[middle_index+1:])

    # Print a bft to check the ordering
    print('bft: ', end=' ')
    head.bft_print(head)

    # Print the height and do a check to see if the tree created is of minimal height
    print('\nheight: ', head.find_height(head))
    print('Is the minimal height? ', check_if_min_height(array, head))

    return head


def minHeightBst2(array: List[int]) -> List[int]:
    # TODO: fix this version
    # Create the head of the entire BST
    middle_index = len(array)//2
    head = BST(array[middle_index])
    print(head.value)

    # Create its left and right sides
    print('about to create head.left with start: 0, end (middle_index-1): ',
          middle_index - 1)
    head.left = create_node2(0, middle_index - 1, array)
    print('about to create head.right with start (middle_index + 1): ',
          middle_index+1, ' and end (len(array) -1: ', len(array) - 1)
    # head.right = create_node2(middle_index+1, len(array) - 1, array)
    '''
    # Print a bft to check the ordering
    print('bft: ', end=' ')
    head.bft_print(head)

    # Print the height and do a check to see if the tree created is of minimal height
    print('\nheight: ', head.find_height(head))
    print('Is the minimal height? ', check_if_min_height(array, head))
    '''
    return head


def create_node(array: List[int]) -> List[int]:
    # Create the head of the subtree
    middle_index = len(array)//2
    new_node = BST(array[middle_index])

    # Create its left side
    if len(array[: middle_index]) > 1:
        new_node.left = create_node(array[: middle_index])
    elif len(array[: middle_index]) == 1:
        new_node.left = BST(array[: middle_index][0])

    # Create its right side
    if len(array[middle_index+1:]) > 1:
        new_node.right = create_node(array[middle_index+1:])
    elif len(array[middle_index+1:]) == 1:
        new_node.right = BST(array[middle_index+1:][0])

    return new_node


def create_node2(start, end, array: List[int]) -> List[int]:
    # Create the head of the subtree
    # middle_index = len(array)//2
    middle_index = (start + end) // 2
    new_node = BST(array[middle_index])
    print(new_node.value)

    # Create its left side
    # if len(array[: middle_index]) > 1:
    if middle_index - 1 - start > 0:
        # new_node.left = create_node(array[: middle_index])
        new_node.left = create_node2(start, middle_index - 1, array)
    # elif len(array[: middle_index]) == 1:
    elif middle_index - 1 - start <= 0:
        # new_node.left = BST(array[: middle_index][0])
        new_node.left = BST(array[middle_index-1])

    # Create its right side
    # if len(array[middle_index+1:]) > 1:
    if end - middle_index + 1 > 0:
        print('in here  with start = ', start, ' end = ',
              end, ' and middle index: ', middle_index)
        # new_node.right = create_node(array[middle_index+1:])
        new_node.right = create_node2(middle_index + 1, end, array)
    # elif len(array[middle_index+1:]) == 1:
    elif end - middle_index + 1 <= 0:
        # new_node.right = BST(array[middle_index+1:][0])
        new_node.right = BST(array[middle_index+1])

    return new_node


def check_if_min_height(array: List[int], node) -> bool:
    """
    This is my attempt to use math to see what height should be considered minimal.
    In my thinking, I can use log base 2. I'll need to experiment with this more.
    """
    return (math.ceil(math.log2(len(array)))) == node.find_height(node)


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def bft_print(self, node):
        q = Queue()
        while node is not None:
            print(node.value, end=' ')
            # Stick all of the node's children in the end of the queue.
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
            if q.size() > 0:
                # Get the first node in the queue and continue the loop with it.
                node = q.dequeue()
            else:
                break
        return

    def find_height(self, node):
        if node is None:
            return 0
        return max(self.find_height(node.left), self.find_height(node.right)) + 1


if __name__ == "__main__":
    # print('head1: ', minHeightBst(
    #     [1, 2, 5, 7, 10, 13, 14, 15, 22]).value, '\n')
    # print('head2: ', minHeightBst([1, 2, 5, 7, 10]).value)

    # print('head1: ', minHeightBst2(
    #     [1, 2, 5, 7, 10, 13, 14, 15, 22]).value, '\n')
    print('head2: ', minHeightBst2([1, 2, 5, 7, 10]).value)
