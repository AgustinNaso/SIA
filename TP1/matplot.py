import json

from algorithms.informed import a_star, local_search
from algorithms.non_informed import dfs, bfs, iddfs
from heuristic import misplaced_numbers, manhattan_distance, nilsson_sequence
from metrics import Metrics
from board import Board
import random
from node import Node
from state import State
import numpy as np
import matplotlib.pyplot as plt


def shuffle():
    new_table = Board(Board.final_table)
    iterations = random.randint(50, 100)
    for i in range(iterations):
        new_table = random.choice(new_table.next_moves())
    return new_table


# game settings
with open("settings.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

informed = bool(jsonObject['matplot']['informed'])
depth = int(jsonObject['max_depth'])

axis = np.array(["Costo", "Profundidad", "Nodos Expandidos", "Nodos Frontera", "Tiempo (ms)"])
titles = np.array(["Costo", "Profundidad", "Nodos Expandidos", "Nodos Frontera", "Tiempo"])


def f(n):
    return n.depth + heuristic(n)


def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),
                 ha='center', va='bottom')


# Tests
# costo, profundidad, nodos expandidos, frontera, tiempo
if not informed:
    bfs_metrics = np.array([0, 0, 0, 0, 0])
    dfs_metrics = np.array([0, 0, 0, 0, 0])
    iddfs_metrics = np.array([0, 0, 0, 0, 0])
    for i in range(5):
        print("round" + str(i))
        board = shuffle()
        state = State(board)
        node = Node(state, None, 0)
        metrics1 = Metrics("BFS", 0, 0, 0, 0, 0, 0)
        print("bfs")
        ans = bfs(node, metrics1)
        metrics1.set_depth(ans.depth)
        metrics1.set_cost(ans.depth)
        bfs_metrics[0] += metrics1.cost
        bfs_metrics[1] += metrics1.depth
        bfs_metrics[2] += metrics1.expanded_nodes
        bfs_metrics[3] += metrics1.frontier_nodes
        bfs_metrics[4] += metrics1.time * 1000
        metrics2 = Metrics("DFS", 0, 0, 0, 0, 0, 0)
        print("dfs")
        ans1 = dfs(node, metrics2)
        metrics2.set_depth(ans1.depth)
        metrics2.set_cost(ans1.depth)
        dfs_metrics[0] += metrics2.cost
        dfs_metrics[1] += metrics2.depth
        dfs_metrics[2] += metrics2.expanded_nodes
        dfs_metrics[3] += metrics2.frontier_nodes
        dfs_metrics[4] += metrics2.time * 1000
        metrics3 = Metrics("IDDFS", 0, 0, 0, 0, 0, 0)
        print("iddfs")
        ans2 = iddfs(node, metrics3, depth)
        metrics3.set_depth(ans2.depth)
        metrics3.set_cost(ans2.depth)
        iddfs_metrics[0] += metrics3.cost
        iddfs_metrics[1] += metrics3.depth
        iddfs_metrics[2] += metrics3.expanded_nodes
        iddfs_metrics[3] += metrics3.frontier_nodes
        iddfs_metrics[4] += metrics3.time * 1000

    for i in range(5):
        bfs_metrics[i] /= 5
        dfs_metrics[i] /= 5
        iddfs_metrics[i] /= 5

    x_labels = ["BFS", "DFS", "IDDFS"]

    for i in range(5):
        fig = plt.figure()
        names = ['BFS', 'DFS', 'IDDFS']
        metrics = [bfs_metrics[i], dfs_metrics[i], iddfs_metrics[i]]
        rects = plt.bar(names, metrics)
        plt.title("Comparaci??n en base a: " + titles[i])
        plt.xlabel("M??todos de B??squeda")
        plt.ylabel(axis[i])
        rects[0].set_color('mediumturquoise')
        rects[1].set_color('hotpink')
        rects[2].set_color('mediumpurple')
        plt.tight_layout()
        plt.show()
else:
    local_metrics = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    global_metrics = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    a_metrics = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    heuristics = np.array([misplaced_numbers, manhattan_distance, nilsson_sequence])

    board = shuffle()

    for j in range(3):
        heuristic = heuristics[j]
        # board = shuffle()
        state = State(board)
        node = Node(state, None, 0)
        metrics1 = Metrics("Local", 0, 0, 0, 0, 0, 0)
        ans = local_search(node, metrics1, heuristic)
        metrics1.set_depth(ans.depth)
        metrics1.set_cost(ans.depth)
        local_metrics[j][0] = metrics1.cost
        local_metrics[j][1] = metrics1.depth
        local_metrics[j][2] = metrics1.expanded_nodes
        local_metrics[j][3] = metrics1.frontier_nodes
        local_metrics[j][4] = metrics1.time * 1000
        metrics2 = Metrics("Global", 0, 0, 0, 0, 0, 0)
        ans1 = a_star(node, metrics2, heuristic)
        metrics2.set_depth(ans1.depth)
        metrics2.set_cost(ans1.depth)
        global_metrics[j][0] += metrics2.cost
        global_metrics[j][1] += metrics2.depth
        global_metrics[j][2] += metrics2.expanded_nodes
        global_metrics[j][3] += metrics2.frontier_nodes
        global_metrics[j][4] += metrics2.time * 1000
        metrics3 = Metrics("A-Star", 0, 0, 0, 0, 0, 0)
        ans2 = a_star(node, metrics3, f)
        metrics3.set_depth(ans2.depth)
        metrics3.set_cost(ans2.depth)
        a_metrics[j][0] += metrics3.cost
        a_metrics[j][1] += metrics3.depth
        a_metrics[j][2] += metrics3.expanded_nodes
        a_metrics[j][3] += metrics3.frontier_nodes
        a_metrics[j][4] += metrics3.time * 1000

    for i in range(5):
        ind = np.arange(3)
        width = 0.25

        xvals = [local_metrics[0][i], global_metrics[0][i], a_metrics[0][i]]
        bar1 = plt.bar(ind, xvals, width, color='mediumturquoise')

        yvals = [local_metrics[1][i], global_metrics[1][i], a_metrics[1][i]]
        bar2 = plt.bar(ind + width, yvals, width, color='hotpink')

        zvals = [local_metrics[2][i], global_metrics[2][i], a_metrics[2][i]]
        bar3 = plt.bar(ind + width * 2, zvals, width, color='mediumpurple')

        plt.xlabel("M??todos de B??squeda")
        plt.ylabel(axis[i])
        plt.title("Comparaci??n en base a: " + titles[i])

        autolabel(bar1)
        autolabel(bar2)
        autolabel(bar3)
        plt.xticks(ind + width, ['Local', 'Global', 'A Estrella'])
        plt.legend((bar1, bar2, bar3), ('H1', 'H2', 'H3'))
        plt.show()
