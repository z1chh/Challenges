# Unweighted Undirected Graph
class MGraph:
    def __init__(self, n, edges=[]):
        self.num_nodes = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        for e in edges:
            # self.addEdge(e[0], e[1], e[2]) # Use this line for weighted graphs
            self.addEdge(e[0], e[1]) # Use this line for unweighted graphs
    
    def addEdge(self, n1, n2, weight=1):
        self.matrix[n1][n2] = weight
        self.matrix[n2][n1] = weight # Comment out this line for directed graphs
    
    def __repr__(self):
        tr = ""
        for line in self.matrix:
            tr += str(line) + "\n"
        return tr
    
    def dfs(self, start_node, f=None):
        hof = []
        stack = []
        marked = set()
        stack.append(start_node)
        while stack:
            v = stack.pop()
            if v not in marked:
                print("MARKING", v)
                marked.add(v)
                for i, n in enumerate(self.matrix[v]):
                    if n != 0:
                        stack.append(i)

def main():
    g = MGraph(6, [(0, 1), (0, 2), (1, 2), (2, 3), (3, 1), (4, 3), (4, 5), (5, 5)])
    print(g)
    g.dfs(0)

if __name__ == "__main__":
    main()
