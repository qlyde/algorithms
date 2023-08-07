class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def kruskal(self):
        mst = []
        self.graph.sort(key=lambda x: x[2])  # Sort edges by weight
        parent = [i for i in range(self.vertices)]

        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])

        def union(parent, rank, x, y):
            x_root = find(parent, x)
            y_root = find(parent, y)

            if x_root != y_root:
                parent[y_root] = x_root

        edge_count = 0
        i = 0

        while edge_count < self.vertices - 1:
            u, v, w = self.graph[i]
            i += 1
            x = find(parent, u)
            y = find(parent, v)

            if x != y:
                edge_count += 1
                mst.append((u, v, w))
                union(parent, [], x, y)

        return mst

# Example usage:
g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 4)
g.add_edge(3, 4, 2)
g.add_edge(4, 5, 6)

minimum_spanning_tree = g.kruskal()
print("Minimum Spanning Tree:")
for u, v, weight in minimum_spanning_tree:
    print("Edge:", u, "-", v, "Weight:", weight)
