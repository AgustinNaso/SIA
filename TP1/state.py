import numpy as np
from board import Board

class State:
    def __init__(self, board):
        self.board = board

    def next_moves(self):
        childs = []
        for i in range(3):
            for j in range(3):
                if self.board.table[i][j] == 0:
                    if i < 2:
                        childs.append(State(self.board.swap(i, j, 1, 0)))
                    if j < 2:
                        childs.append(State(self.board.swap(i, j, 0, 1)))
                    if j > 0:
                        childs.append(State(self.board.swap(i, j, 0, -1)))
                    if i > 0:
                        childs.append(State(self.board.swap(i, j, -1, 0)))
        return childs

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
