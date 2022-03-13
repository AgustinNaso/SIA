import numpy as np
from board import Board
from typing import Final


class Heuristic:
    manhattan_coordinates: Final = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1]])
    sequence_coordinates: Final = np.array([[[0, 1], [0, 2], [1, 0]], [[1, 1], [1, 2], [2, 0]], [[2, 1], [2, 2], [2, 1]]])

    def __init__(self, heuristic, board):
        self.board = board
        self.heuristics = {"misplaced numbers": self.misplaced_numbers(),
                           "manhattan": self.manhattan_distance(),
                           "nilsson": self.nilsson_sequence()}  # make json
        self.heuristic = self.heuristics[heuristic]

    # Heuristic 1: sum of misplaced numbers (admissible)
    def misplaced_numbers(self):
        return np.sum(self.board.table != Board.final_table)

    # Heuristic 2: manhattan distance (admissible)
    def manhattan_distance(self):
        manhattan = 0
        for i in range(3):
            for j in range(3):
                if self.board.table[i][j] != 0:
                    x = Heuristic.manhattan_coordinates[self.board.table[i][j] - 1][0]
                    y = Heuristic.manhattan_coordinates[self.board.table[i][j] - 1][1]
                    manhattan += abs(i - x) + abs(j - y)
                else:
                    manhattan += abs(i - 2) + abs(j - 2)
        return manhattan

    # Heuristic 3: Nilsson sequence (non-admissible)
    def nilsson_sequence(self):
        return self.manhattan_distance() + 3 * self.sequence_sum()

    # Sum of sequence for nilsson sequence heuristic
    def sequence_sum(self):
        ans = 0
        for i in range(3):
            for j in range(3):
                if self.board.table[i][j] != 0:
                    if i == 2 and j == 2:
                        ans += 1
                    else:
                        x = Heuristic.sequence_coordinates[i][j][0]
                        y = Heuristic.sequence_coordinates[i][j][1]
                        if self.board.table[i][j] != 8:
                            if self.board.table[x][y] != self.board.table[i][j] + 1:
                                ans += 2
                        else:
                            if self.board.table[x][y] != 0:
                                ans += 2
        return ans


h = Heuristic("nilsson", Board(np.array([[2, 1, 5],
                                   [3, 4, 6],
                                   [7, 0, 8]])))
print(h.heuristic)
