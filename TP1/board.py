import numpy as np

class Board:
    table = np.array([1, 2, 3], [4, 5, 6], [7, 8, 0])

    def solved(current):
        return np.array_equal(current, Board.table)

    # def move_piece(board):
    #     swap many times
