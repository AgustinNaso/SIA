import numpy as np


class State:
    def __init__(self, table):
        self.table = table

    def next_moves(self):
        childs = []
        for i in range(3):
            for j in range(3):
                if self.table[i][j] == 0:
                    if i < 2:
                        childs.append(State(self.swap(i, j, 1, 0)))
                    if j < 2:
                        childs.append(State(self.swap(i, j, 0, 1)))
                    if j > 0:
                        childs.append(State(self.swap(i, j, 0, -1)))
                    if i > 0:
                        childs.append(State(self.swap(i, j, -1, 0)))
        return childs

    def swap(self, i, j, x, y):
        table = self.table.copy()
        table[i][j], table[i + x][j + y] = table[i + x][j + y], table[i][j]
        return table

    def print(self):
        for i in range(3):
            for j in range(3):
                print(self.table[i][j], end="")
            print(" ")

    def compare_to(self, state):
        return np.array_equal(self.table, state.table)


state = State(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))
state.print()
print("-------------")
childs = state.next_moves()

for i in range(len(childs)):
    print(childs[i].compare_to(state))

print(state.compare_to(state))