import sys


class Graph():
    def __init__(self, vertices, items):
        self.V = vertices
        self.items = {idx: item for idx, item in enumerate(items)}
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.start = -1
        self.dij = {}

    def addEdge(self, edge):
        self.graph[edge[0] - 1][edge[1] - 1] = edge[2]
        self.graph[edge[1] - 1][edge[0] - 1] = edge[2]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
        # Initialize min_index to -1
        min_index = -1
        # Initialize minimum distance for next node
        min = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
        self.start = src

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        d = {}
        for node in range(self.V):
            d[node] = dist[node]
        self.dij = d
        # self.printSolution(dist)

    def __repr__(self):
        string = ""
        for line in self.graph:
            string += " ".join(map(str, line)) + "\n"
        return string


# Big Truck
def main():
    # Create graph
    g = Graph(int(input()), map(int, input().split()))
    for _ in range(int(input())):
        g.addEdge(list(map(int, input().split())))

    # Compute Dijkstra
    g.dijkstra(0)

    # Check if impossible to reach
    if g.dij[g.V - 1] == sys.maxsize:
        print("impossible")
        exit()

    # Otherwise, output shortest path and items picked up
    print(g.dij[g.V - 1])


if __name__ == "__main__":
    main()
