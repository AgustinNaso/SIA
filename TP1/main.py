from TP1.algorithms.non_informed import dfs, bfs, iddfs
from TP1.metrics import Metrics
from board import Board
import random
from node import Node
from state import State


def show_solution(ans_node):
    stack = []
    while ans_node:
        stack.append(ans_node)
        ans_node = ans_node.parent
    while stack:
        stack.pop().print_state()
        print('\n')

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
node = Node(state, None, 0)
metrics = Metrics("BFS", 0, 0, 0, 0, 0, 0)
print('initial state: ')
node.print_state()
print('bfs!')
ans = iddfs(node, metrics, 80)

metrics.set_depth(ans.depth)
# El costo por cada movimiento es 1
metrics.set_cost(ans.depth)
metrics.print()
print("Solution: ")
show_solution(ans)

