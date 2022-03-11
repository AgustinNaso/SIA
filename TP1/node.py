import numpy as np

from TP1.state import State


class Node:
    state = None

    def __init__(self, state, parent):
        self.state = state
        self.parent = parent  # root is null

    def get_children(self):
        children = []
        for child_board in self.state.board.next_moves():
            new_state = State(child_board)
            new_node = Node(new_state, self)
            children.append(new_node)
        return children

    def __eq__(self, other):
        return self.state.__eq__(other.state)

    def __hash__(self):
        return self.state.__hash__()

    def print_state(self):
        self.state.print()

# for i in range(len(aux)):
# aux[i].print()
