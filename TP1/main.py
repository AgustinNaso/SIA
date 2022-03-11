from algorithms.non_informed import dfs, bfs
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


# Setup for DFS
table = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
board = Board(table)
state = State(board)
node = Node(state, 0)
node.print_state()

print('dfs!')
dfs(node)


