# BFS
# in: node
# out: node with solution
def bfs(starting_node, metrics):
    visited = set()  # Set to keep track of visited nodes of graph.
    stack = [starting_node]

    while stack:
        curr_node = stack.pop(0)
        # check if solution found
        if curr_node not in visited:
            visited.add(curr_node)
            if curr_node.state.board.is_solved():
                metrics.result = 1
                metrics.frontier_nodes = len(stack)
                return curr_node
            children = curr_node.get_children()
            if children:
                metrics.expanded_nodes += 1
            for child in children:
                stack.append(child)


# DFS
# in: node
# out: node with solution

def dfs(starting_node, metrics):  # function for dfs
    visited = set()  # Set to keep track of visited nodes of graph.
    stack = [starting_node]
    while stack:
        curr_node = stack.pop()
        if curr_node not in visited:
            visited.add(curr_node)
            if curr_node.state.board.is_solved():
                metrics.result = 1
                metrics.frontier_nodes = len(stack)
                return curr_node
            children = curr_node.get_children()
            if children:
                metrics.expanded_nodes += 1
            for child in children:
                stack.append(child)
