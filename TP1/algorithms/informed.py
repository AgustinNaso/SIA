import time


def local_search_heuristic(node):
    visited = set()
    queue = [node]
    visited.add(node)  # save already visited nodes

    while queue:
        curr = queue.pop(0)
        # check if curr is solution


# function used to reorder a_star list
def f(n):
    return n.depth + n.heuristic(n.state.board)

# A_star
# in: starting node, metrics
# out: solution node if exists, or None if not


def a_star(node, metrics):
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
        sorted_list.sort(key=f)
    return None
