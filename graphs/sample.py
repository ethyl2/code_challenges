# sample adjacency list

sample_adjacency_list = {
    1: {2},
    2: {3, 5},
    3: {4},
    4: {3},
    5: {1}
}


class Graph:
    def __init__(self):
        self.edges = [[0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 1, 1],
                      [0, 0, 1, 0, 0, 0, 0],
                      [0, 0, 1, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 1, 0]]


sample_adjacency_matrix = [[0, 1, 0, 0, 1, 0],
                           [0, 0, 1, 1, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 1],
                           [0, 0, 1, 1, 0, 0],
                           [0, 0, 1, 1, 0, 0]]
