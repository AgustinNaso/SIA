import numpy as np


class Node:
    state = None

    def __init__(self, state, parent):
        self.state = state
        self.parent = parent  # root is null

    def get_children(self):
        children = []
        for child_state in self.state.next_moves():
            new_node = Node(child_state, self)
            children.append(new_node)
        return children

    def __eq__(self, other):
        return self.state == other.state


print("----------------")
# for i in range(len(aux)):
# aux[i].print()
