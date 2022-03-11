import numpy as np
from board import Board


class State:
    def __init__(self, board):
        self.board = board

    def print(self):
        self.board.print()

    def __eq__(self, other):
        return self.board.__eq__(other.board)

    def __hash__(self):
        return self.board.__hash__()

    def compare_to(self, state):
        return state.board.compare_to(self.board)

# state = State(Board(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])))
# # state.print()
# # print("-------------")
# children = state.next_moves()
# children2 = [[],[],[]]
# for i in range(len(children)):
#     children2[i] = children[i].next_moves()
#     for j in range(len(children2)):
#         children2[i][j].print()
#         print("")
