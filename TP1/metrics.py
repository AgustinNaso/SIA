class Metrics:
    def __init__(self, algorithm, result, depth, cost, expanded_nodes, frontier_nodes, time):
        self.algorithm = algorithm
        self.result = result
        self.depth = depth
        self.cost = cost
        self.expanded_nodes = expanded_nodes
        self.frontier_nodes = frontier_nodes
        self.time = time

    def print(self):
        print("Algorithm: ", self.algorithm)
        print("Result: ", "successful" if self.result else "unsuccessful")
        print("Depth: ", self.depth)
        print("Cost: ", self.cost)
        print("Expanded nodes: ", self.expanded_nodes)
        print("Frontier nodes: ", self.frontier_nodes)
        print("Time: ", self.time)

    def set_depth(self, depth):
        self.depth = depth

    def set_cost(self, cost):
        self.cost = cost
