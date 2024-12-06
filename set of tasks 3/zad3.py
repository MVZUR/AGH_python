class Network():

    def __init__(self, nodes):
        self.nodes_count = nodes
        self.matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]

    def displayResult(self, distances):
        print("Node \t Distance from Start")
        for node in range(self.nodes_count):
            print(node, "\t\t", distances[node])

    def findClosestNode(self, distances, visited_nodes):
        min_distance = float('inf')

        for node in range(self.nodes_count):
            if distances[node] < min_distance and not visited_nodes[node]:
                min_distance = distances[node]
                closest_node = node

        return closest_node

    def calculateShortestPaths(self, start_node):

        distances = [float('inf')] * self.nodes_count
        distances[start_node] = 0
        visited_nodes = [False] * self.nodes_count

        for _ in range(self.nodes_count):
            current_node = self.findClosestNode(distances, visited_nodes)
            visited_nodes[current_node] = True

            for neighbor in range(self.nodes_count):
                if self.matrix[current_node][neighbor] > 0 and not visited_nodes[neighbor] and distances[neighbor] > distances[current_node] + self.matrix[current_node][neighbor]:
                    distances[neighbor] = distances[current_node] + self.matrix[current_node][neighbor]

        self.displayResult(distances)


network = Network(9)
network.matrix = [
    [0, 5, 0, 0, 0, 0, 0, 9, 0],
    [5, 0, 9, 0, 0, 0, 0, 13, 0],
    [0, 9, 0, 6, 0, 3, 0, 0, 3],
    [0, 0, 6, 0, 10, 15, 0, 0, 0],
    [0, 0, 0, 10, 0, 11, 0, 0, 0],
    [0, 0, 3, 15, 11, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 2, 7],
    [9, 13, 0, 0, 0, 0, 2, 0, 8],
    [0, 0, 3, 0, 0, 0, 7, 8, 0]
]

network.calculateShortestPaths(0)
