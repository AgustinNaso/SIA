import time
from queue import PriorityQueue
from itertools import count


def local_search(node, metrics, heuristic):
    start_time = time.time()
    visited = set()
    sorted_list = [node]
    while sorted_list:
        curr_node = sorted_list.pop()
        visited.add(curr_node)
        if curr_node.state.board.is_solved():
            metrics.result = 1
            metrics.frontier_nodes = len(sorted_list)
            metrics.time = time.time() - start_time
            return curr_node
        children = curr_node.get_children()
        if children:
            metrics.expanded_nodes += 1
        children.sort(key=heuristic)
        children.reverse()
        for child_node in children:
            if child_node not in visited:
                sorted_list.append(child_node)
    return None


# A_star
# in: starting node, metrics, h(n)
# out: solution node if exists, or None if not

def a_star(node, metrics, heuristic):
    unique = count()
    start_time = time.time()
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((heuristic(node), next(unique), node))
    while priority_queue:
        curr_node = priority_queue.get()[2]
        visited.add(curr_node)
        if curr_node.state.board.is_solved():
            metrics.result = 1
            metrics.frontier_nodes = priority_queue.qsize()
            metrics.time = time.time() - start_time
            return curr_node
        children = curr_node.get_children()
        if children:
            metrics.expanded_nodes += 1
        for child_node in children:
            if child_node not in visited:
                priority_queue.put((heuristic(child_node), next(unique), child_node))
    return None