import numpy as np
from board import Board

class State:
    def __init__(self, board):
        self.board = board

    def next_moves(self):
        children = []
        for i in range(3):
            for j in range(3):
                if self.board.table[i][j] == 0:
                    if i < 2:
                        children.append(State(self.board.swap(i, j, 1, 0)))
                    if j < 2:
                        children.append(State(self.board.swap(i, j, 0, 1)))
                    if j > 0:
                        children.append(State(self.board.swap(i, j, 0, -1)))
                    if i > 0:
                        children.append(State(self.board.swap(i, j, -1, 0)))
        return children

    def print(self):
        self.board.print()

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
