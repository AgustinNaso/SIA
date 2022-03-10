import numpy as np
from board import Board

class State:
    def __init__(self, board):
        self.board = board

    def print(self):
        self.board.print()

    def compare_to(self, state):
        return state.board.compare_to(self.board)


# state = State(Board(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])))
# state.print()
# print("-------------")
# childs = state.next_moves()
#
# for i in range(len(childs)):
#     print(childs[i].compare_to(state))
#
# print(state.board.is_solved())
