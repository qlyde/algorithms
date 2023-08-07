import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim(self):
        mst = []
        visited = set()
        heap = [(0, 0, -1)]  # Start with any vertex (0 here), -1 is a placeholder for the source vertex
        heapq.heapify(heap)

        while heap:
            weight, vertex, source = heapq.heappop(heap)
            if vertex not in visited:
                visited.add(vertex)
                if source != -1:
                    mst.append((source, vertex, weight))

                for neighbor, edge_weight in self.graph[vertex]:
                    if neighbor not in visited:
                        heapq.heappush(heap, (edge_weight, neighbor, vertex))

        return mst

# Example usage:
from collections import defaultdict

g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 4)
g.add_edge(3, 4, 2)
g.add_edge(4, 5, 6)

minimum_spanning_tree = g.prim()
print("Minimum Spanning Tree:")
for u, v, weight in minimum_spanning_tree:
    print("Edge:", u, "-", v, "Weight:", weight)
