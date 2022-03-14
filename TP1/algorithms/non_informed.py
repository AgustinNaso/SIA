import time


# BFS
# in: node
# out: node with solution
def bfs(starting_node, metrics):
    start_time = time.time()
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
                metrics.time = time.time() - start_time
                return curr_node
            children = curr_node.get_children()
            if children:
                metrics.expanded_nodes += 1
            for child in children:
                stack.append(child)
    return None


# DFS
# in: node
# out: node with solution

def dfs(starting_node, metrics):  # function for dfs
    start_time = time.time()
    visited = set()  # Set to keep track of visited nodes of graph.
    stack = [starting_node]
    while stack:
        curr_node = stack.pop()
        if curr_node not in visited:
            visited.add(curr_node)
            if curr_node.state.board.is_solved():
                metrics.result = 1
                metrics.frontier_nodes = len(stack)
                metrics.time = time.time() - start_time
                return curr_node
            children = curr_node.get_children()
            if children:
                metrics.expanded_nodes += 1
            for child in children:
                stack.append(child)


# DLS
# in: starting node, metrics, max node depth
# out: solution node or None if cannot find one

def dls(starting_node, metrics, max_depth):
    visited = set()
    stack = [starting_node]
    while stack:
        curr_node = stack.pop()
        if curr_node not in visited and curr_node.depth < max_depth:
            visited.add(curr_node)
            if curr_node.state.board.is_solved():
                metrics.result = 1
                metrics.frontier_nodes += len(stack)
                return curr_node
            children = curr_node.get_children()
            if children:
                metrics.expanded_nodes += 1
            for child in children:
                stack.append(child)
    return None


# IDDFS
# in: node
# out: node with solution
#
def iddfs(starting_node, metrics, max_depth):
    start_time = time.time()
    ans = None
    while ans is not None:
        ans = dls(starting_node, metrics, max_depth)
        max_depth *= 2
        if max_depth > 1000000:
            return None
    max_depth /= 3
    second_ans = dls(starting_node, metrics, max_depth)
    metrics.time = time.time() - start_time
    if second_ans is not None:
        return second_ans
    return ans



