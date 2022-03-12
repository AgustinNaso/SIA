import numpy as np
from board import Board
from typing import Final

MANHATTAN = 0
NILLSON = 1


class Heuristic:
    manhattan_coordinates: Final = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1]])
    nilsson_coordinates: Final = np.array([[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0], [1, 0]])
    sequence_coordinates: Final = np.array([[[0, 1], [0, 2], [1, 2]], [[0, 0], [1, 1], [2, 2]], [[1, 0], [2, 0], [2, 1]]])

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
        return self.manhattan(MANHATTAN)

    # Heuristic 3: Nilsson sequence (non-admissible)
    def nilsson_sequence(self):
        return self.manhattan(NILLSON) + 3 * self.sequence_sum()

    # Sum of sequence for nilsson sequence heuristic
    def sequence_sum(self):
        ans = 0
        for i in range(3):
            for j in range(3):
                if self.board.table[i][j] != 0:
                    if i == 1 and j == 1:
                        ans += 1
                    else:
                        x = Heuristic.sequence_coordinates[i][j][0]
                        y = Heuristic.sequence_coordinates[i][j][1]
                        if self.board.table[x][y] != self.board.table[i][j] + 1:
                            ans += 2
        return ans

    # Common manhattan
    # option: 0 for manhattan heuristic ; 1 for nilsson heuristic
    def manhattan(self, option):
        manhattan = 0
        for i in range(3):
            for j in range(3):
                if self.board.table[i][j] != 0:
                    if option == 0:
                        x = Heuristic.manhattan_coordinates[self.board.table[i][j] - 1][0]
                        y = Heuristic.manhattan_coordinates[self.board.table[i][j] - 1][1]
                    else:
                        x = Heuristic.nilsson_coordinates[self.board.table[i][j] - 1][0]
                        y = Heuristic.nilsson_coordinates[self.board.table[i][j] - 1][1]
                    manhattan += abs(i - x) + abs(j - y)
                else:
                    if option == 0:
                        manhattan += abs(i - 2) + abs(j - 2)
                    else:
                        manhattan += abs(i - 1) + abs(j - 1)
        return manhattan


h = Heuristic("nilsson", Board(np.array([[2, 1, 5],
                                   [3, 4, 6],
                                   [7, 0, 8]])))
print(h.heuristic)
