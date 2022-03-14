import numpy as np
from board import Board
from typing import Final

# class Heuristic:
manhattan_coordinates: Final = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1]])
sequence_coordinates: Final = np.array([[[0, 1], [0, 2], [1, 0]], [[1, 1], [1, 2], [2, 0]], [[2, 1], [2, 2], [2, 1]]])


def get_heuristic(heuristic):
    heuristics = [misplaced_numbers,
                  manhattan_distance,
                  nilsson_sequence]
    return heuristics[heuristic]


# Heuristic 1: sum of misplaced numbers (admissible)
def misplaced_numbers(node):
    return np.sum(node.state.board.table != Board.final_table)


# Heuristic 2: manhattan distance (admissible)
def manhattan_distance(node):
    manhattan = 0
    for i in range(3):
        for j in range(3):
            if node.state.board.table[i][j] != 0:
                x = manhattan_coordinates[node.state.board.table[i][j] - 1][0]
                y = manhattan_coordinates[node.state.board.table[i][j] - 1][1]
                manhattan += abs(i - x) + abs(j - y)
            else:
                manhattan += abs(i - 2) + abs(j - 2)
    return manhattan


# Heuristic 3: Nilsson sequence (non-admissible)
def nilsson_sequence(node):
    return manhattan_distance(node) + 3 * sequence_sum(node)


# Sum of sequence for nilsson sequence heuristic
def sequence_sum(node):
    ans = 0
    for i in range(3):
        for j in range(3):
            if node.state.board.table[i][j] != 0:
                if i == 2 and j == 2:
                    ans += 1
                else:
                    x = sequence_coordinates[i][j][0]
                    y = sequence_coordinates[i][j][1]
                    if node.state.board.table[i][j] != 8:
                        if node.state.board.table[x][y] != node.state.board.table[i][j] + 1:
                            ans += 2
                    else:
                        if node.state.board.table[x][y] != 0:
                            ans += 2
    return ans
