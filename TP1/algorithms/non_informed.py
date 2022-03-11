from .. import node
from ..node import Node


def bfs(node):
    visited = set()
    queue = [node]
    visited.add(node)  # save already visited nodes

    while queue:
        curr = queue.pop(0)
        # check if solution found
        # if (board.is_completed(curr)):
        #     metrics.success = True
        #     metrics.frontier = len(queue)
        #     print('finished with: ' + str(metrics.nodes_expanded))
        #
        #     return SearchResults(metrics, curr)
        visited.add(curr)
        # moves = board.get_possible_moves(curr, self.checkDeadlocks)  # get a tree level
        # if (moves):  # curr has children
        #     metrics.nodes_expanded += 1
        #
        # for move in moves:
        #     if move not in visited:
        #         queue.append(move)


# DFS
# in: node
# out: node with solution

def dfs(starting_node):  # function for dfs
    visited = set()  # Set to keep track of visited nodes of graph.
    stack = [starting_node]
    while stack:
        curr_node = stack.pop()
        if curr_node not in visited:
            visited.add(curr_node)
            if curr_node.state.board.is_solved():
                return curr_node
            for child in curr_node.get_children():
                stack.append(child)
    return
