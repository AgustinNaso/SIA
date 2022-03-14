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
