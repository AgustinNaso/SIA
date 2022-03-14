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
                print(self.table[i, j], end="")
            print("")

    def to_string(self):
        string = ""
        for i in range(3):
            for j in range(3):
                string += str(self.table[i, j])
        return string

    def next_moves(self):
        children = []
        for i in range(3):
            for j in range(3):
                if self.table[i, j] == 0:
                    if i < 2:
                        children.append(self.swap(i, j, 1, 0))
                    if j < 2:
                        children.append(self.swap(i, j, 0, 1))
                    if j > 0:
                        children.append(self.swap(i, j, 0, -1))
                    if i > 0:
                        children.append(self.swap(i, j, -1, 0))
        return children

    def compare_to(self, board):
        return np.array_equal(board.table, self.table)

    def __eq__(self, other):
        return self.to_string().__eq__(other.to_string())

    def __hash__(self):
        return self.to_string().__hash__()

    def swap_with_post(self, i, j, x, y):
        self.table[i][j], self.table[x, y] = self.table[x, y], self.table[i, j]
        return self

    def swap(self, i, j, x, y):
        table = self.table.copy()
        table[i][j], table[i + x, j + y] = table[i + x, j + y], table[i, j]
        return Board(table)
