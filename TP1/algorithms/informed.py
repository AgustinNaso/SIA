def local_search_heuristic(node):
    visited = set()
    queue = [node]
    visited.add(node)  # save already visited nodes

    while queue:

        curr = queue.pop(0)
        #check if curr is solution


def a_star(node, heuristic):
    visited = set()
    queue = [node]
    visited.add(node)