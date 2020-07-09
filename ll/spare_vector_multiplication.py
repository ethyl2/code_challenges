"""
From Kapil Sharma's lecture 7-9-2020
Code challenge from Facebook

Given 2 sparse vectors (Vector is like a generic term for a list; sparse meaning mostly 0s with a few values),
Return the sum of multiplying them. (Multiplying them means v1[given_index]*v2[given_index] for each of the indices, 
such as v1[0] * v2[0] + v1[1] + v2[1] etc.)

First question of interviewer: What data structure should you use?
Kapil suggests using an arraylist with Java or linked list with other languages.

1. Once vectors are converted into lls,
2. Traverse thru both lls until one has reached the end.
3. If indices are the same, mult the values and add them to the total. Then move to next els of both lls.
4. Else, if v1's index is smaller, move to next el for v1.
5. Else, move to next el of v2.
6. Finally, return total.

Time complexity:  O(n+m), where n is the length of v1 and m is the length of v2
Space complexity: O(n+m), taking the data structure conversions into account. O(1) otherwise.
"""
A = [1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 7]
B = [0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'({self.data.index}: {self.data.value})'


class VectorElement:
    def __init__(self, index, value):
        self.index = index
        self.value = value


def create_ll_from_vector(vector):
    head = None
    prev_node = None
    for i in range(len(vector)):

        if vector[i] > 0:
            vector_el = VectorElement(i, vector[i])
            if not head:
                head = Node(vector_el)
                prev_node = head
            else:
                new_node = Node(vector_el)
                prev_node.next = new_node
                prev_node = new_node
    return head


def print_ll(node):
    output = str(node) + ' -> '
    node = node.next
    while node:
        output += str(node) + ' -> '
        node = node.next
    output += 'None'
    return output


def sparse_vector_multiplication(v1, v2):
    if v1 == None or v2 == None:
        return 0
    total = 0
    while v1 != None and v2 != None:
        if v1.data.index == v2.data.index:
            total += v1.data.value * v2.data.value
            v1 = v1.next
            v2 = v2.next
        elif v1.data.index < v2.data.index:
            v1 = v1.next
        else:
            v2 = v2.next
    return total


def convert_ll_to_vector(head):
    output = [0] * (head.data.index)
    output.append(head.data.value)
    prev = head
    curr = head.next

    while curr:
        for i in range(curr.data.index-prev.data.index-1):
            output.append(0)
        output.append(curr.data.value)
        prev = curr
        curr = curr.next

    return(output)


v1 = create_ll_from_vector(A)
v2 = create_ll_from_vector(B)
print(print_ll(v1))
print(print_ll(v2))
print(sparse_vector_multiplication(v1, v2))
print(convert_ll_to_vector(v1))
print(convert_ll_to_vector(v2))

'''
Experimenting using a dictionary instead.

Similar time complexity : O(n+m), where n is the length of v1 and m is the length of v2, but 
less traversals overall, when taking the data structure conversions into account, so a little
more efficient. Unlike the first approach, only A has to be converted.

Space complexity: O(n), where n is the length of v1. Again, more efficient when data structure conversions
are taken into account.
'''


def sparse_vector_multiplication_with_dictionary(A, B):
    dict_a = dict()
    total = 0
    for i in range(len(A)):
        if A[i] != 0:
            dict_a[i] = A[i]

    for i in range(len(B)):
        if B[i] != 0:
            if A[i]:
                total += B[i] * A[i]
    return total


print(sparse_vector_multiplication_with_dictionary(A, B))
