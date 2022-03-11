from TP1.algorithms.non_informed import dfs
from board import Board
import random
from node import Node
from state import State


def show_steps(solution_node):
    stack = []
    while solution_node.parent:
        stack.append(solution_node)
        solution_node = solution_node.parent
    while stack:
        stack.pop().print_state()
        print('\n')


def shuffle():
    new_table = Board(Board.final_table)
    iterations = random.randint(50, 100)
    for i in range(iterations):
        new_table = random.choice(new_table.next_moves())
    return new_table


# Setup for DFS
board = shuffle()
state = State(board)
node = Node(state, None)
print('initial state: ')
node.print_state()
print('dfs!')
ans = dfs(node)

print('solution:')
show_steps(ans)



