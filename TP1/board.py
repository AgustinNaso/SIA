import numpy as np
from typing import Final


class Board:
    final_table: Final = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    def __init__(self, table):
        self.table = table

    def is_solved(self):
        return np.array_equal(self.table, Board.final_table)

    def print(self):
        for i in range(3):
            for j in range(3):
                print(self.table[i][j], end="")
            print("")

    # def move_piece(board):
    #     swap many times

    def compare_to(self, board):
        return np.array_equal(board.table, self.table)

    def swap(self, i, j, x, y):
        table = self.table.copy()
        table[i][j], table[i + x][j + y] = table[i + x][j + y], table[i][j]
        return Board(table)
