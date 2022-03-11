from board import Board
import random
import numpy as np
from node import Node
from state import State




def shuffle():
    new_table = Board(Board.final_table)
    iterations = random.randint(50, 100)
    for i in range(iterations):
        new_table = random.choice(new_table.next_moves())
    return new_table


def dfs(starting_node):  # function for dfs
    visited = set()  # Set to keep track of visited nodes of graph.
    stack = [starting_node]
    while stack:
        curr_node = stack.pop()
        curr_node.print_state()
        print('\n')
        if curr_node not in visited:
            visited.add(curr_node)
            print("Aceptado")
            node.print_state()
            if curr_node.state.board.is_solved():
                return curr_node
        for child in curr_node.get_children():
            stack.append(child)
    return


# Driver Code

table = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
board = Board(table)
state = State(board)
node = Node(state, 0)
node.print_state()

print('dfs!')
dfs(node)


