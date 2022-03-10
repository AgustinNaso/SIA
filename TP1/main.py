import numpy as np
from node import Node


def is_solution(curr_node):
    solution = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    return np.array_equal(curr_node.table, solution)


def dfs(starting_node):  # function for dfs
    visited = set()  # Set to keep track of visited nodes of graph.
    stack = [starting_node]
    while stack:
        curr_node = stack.pop()
        if curr_node not in visited:
            visited.add(curr_node)
            if is_solution(curr_node):
                return
        for child in curr_node.genChilds():
            stack.append(child)
    return


# Driver Code
print("Following is the Depth-First Search")

table = np.array([[1, 2, 4], [3, 5, 6], [7, 8, 0]])
node = Node(table)
dfs(node)


print('Hello world!')
