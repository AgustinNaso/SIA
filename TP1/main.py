import numpy as np
from node import Node
from state import State


def is_solution(curr_node):
    solution = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    return np.array_equal(curr_node.state.table, solution)


def dfs(starting_node):  # function for dfs
    visited = set()  # Set to keep track of visited nodes of graph.
    stack = [starting_node]
    while stack:
        print(visited)
        curr_node = stack.pop()
        if curr_node not in visited:
            visited.append(curr_node)
            node.state.print()
            print('\n')
            if is_solution(curr_node):
                return
        for child in curr_node.get_children():
            stack.append(child)
    return


# Driver Code
print("Following is the Depth-First Search")

table = np.array([[1, 2, 4], [3, 5, 7], [6, 8, 0]])
state = State(table)
node = Node(state, 0)
dfs(node)
# for n in node.get_children():
#     n.state.print()
#     print('\n')

print('Hello world!')
