import numpy as np
from board import Board
from typing import Final


class Heuristic:
    heuristics: Final = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    def __init__(self, heuristic, board):
        self.board = board

    def misplaced_numbers(self):
        return np.sum(self.board.table != Board.final_table)


def misplaced_numbers(board):
    return np.sum(board.table != Board.final_table)


# data_set = {"0": misplaced_numbers(Board(np.array([[2, 3, 1], [4, 5, 6], [7, 8, 0]]))), "1": [4, 5, 6]}
# print(data_set["0"])
# a = np.array([[2, 3, 1], [4, 5, 6], [7, 8, 0]])
# print(a[0])
