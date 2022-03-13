import time


# from TP1.heuristic import misplaced_numbers

# function used to reorder a_star list
# def f(n):
# return n.depth + n.heuristic.he(n.state.board)

# def h(n):
#     return heurictic
def local_search(node, metrics, heuristic):
    start_time = time.time()
    visited = set()
    sorted_list = [node]
    while sorted_list:
        curr_node = sorted_list.pop(0)
        visited.add(curr_node)
        if curr_node.state.board.is_solved():
            metrics.result = 1
            metrics.frontier_nodes = len(sorted_list)
            metrics.time = time.time() - start_time
            return curr_node
        children = curr_node.get_children()
        if children:
            metrics.expanded_nodes += 1
        for child_node in children:
            if child_node not in visited:
                sorted_list.append(child_node)
        sorted_list.sort(key=heuristic)
    return None


# A_star
# in: starting node, metrics
# out: solution node if exists, or None if not

def a_star(node, metrics, heuristic):
    start_time = time.time()
    visited = set()
    sorted_list = [node]
    while sorted_list:
        curr_node = sorted_list.pop(0)
        visited.add(curr_node)
        if curr_node.state.board.is_solved():
            metrics.result = 1
            metrics.frontier_nodes = len(sorted_list)
            metrics.time = time.time() - start_time
            return curr_node
        children = curr_node.get_children()
        if children:
            metrics.expanded_nodes += 1
        for child_node in children:
            if child_node not in visited:
                sorted_list.append(child_node)
        sorted_list.sort(key=heuristic)
    return None
