'''
Sean Chen's solution.
See mine in largest_values_in_each_row.py
'''

from collection import deque


def largest_values_in_tree_rows(t):
    rv = []

    if t is None:
        return rv

    current_depth = 0
    current_max = t.value
    q = deque()

    # add the root node to the queue at a depth of 0
    q.append((t, current_depth))

    while len(q) > 0:
        node, depth = q.popleft()

        # if the depth of the current node is different from
        # `current_node`, add `current_max` to `rv` and then
        # reset `current_max` and `current_depth`
        if depth != current_depth:
            rv.append(current_max)
            current_max = node.value
            current_depth = depth

        # otherwise, we update `current_max` if we need to
        else:
            current_max = max(node.value, current_max)

        # add the left and right children of the current node
        # to the queue, along with their depths
        if node.left:
            q.append((node.left, depth + 1))

        if node.right:
            q.append((node.right, depth + 1))

        # don't forget to append the last `current_max`
        rv.append(current_max)
        return rv
