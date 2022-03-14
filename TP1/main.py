from TP1.algorithms.informed import a_star, local_search
from TP1.algorithms.non_informed import dfs, bfs, iddfs
from TP1.heuristic import misplaced_numbers, manhattan_distance, nilsson_sequence, sequence_sum
from TP1.metrics import Metrics
from board import Board
import random
from node import Node
from state import State
import numpy as np


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
# board = shuffle()
board = Board(np.array([[2, 3, 1], [4, 0, 8], [7, 6, 5]]))
state = State(board)
node = Node(state, None, 0)
metrics = Metrics("BFS", 0, 0, 0, 0, 0, 0)
non_informed = [dfs, bfs, iddfs]
non_i_names = ['dfs', 'bfs', 'iddfs']
i_names = ['local', 'global', 'a_star']
informed = [local_search, a_star, a_star]
heuristic = misplaced_numbers


def f(n):
    n.depth + heuristic(n)


print('initial state')
node.print_state()
ans = a_star(node, metrics, manhattan_distance)
metrics.print()
# for i in range(0, 3):
#     metrics = Metrics(non_i_names[i], 0, 0, 0, 0, 0, 0)
#     if i == 2:
#         ans = non_informed[i](node, metrics, 10000)
#     else:
#         ans = non_informed[i](node, metrics)
#     metrics.set_depth(ans.depth)
#     metrics.set_cost(ans.depth)
#     metrics.print()
#     metrics = Metrics(i_names[i], 0, 0, 0, 0, 0, 0)
#     if i == 2:
#         ans = informed[i](node, metrics, f)
#     else:
#         ans = informed[i](node, metrics, heuristic)
#     metrics.set_depth(ans.depth)
#     # El costo por cada movimiento es 1
#     metrics.set_cost(ans.depth)
#     metrics.print()
