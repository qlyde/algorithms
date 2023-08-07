import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def dijkstra(self, src):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[src] = 0

        heap = [(0, src)]
        heapq.heapify(heap)

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances

# Example usage:
from collections import defaultdict

g = Graph(6)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 3)
g.add_edge(1, 3, 6)
g.add_edge(1, 2, 2)
g.add_edge(2, 4, 4)
g.add_edge(2, 5, 2)
g.add_edge(2, 3, 7)
g.add_edge(3, 4, -1)
g.add_edge(4, 5, -2)

src = 0
shortest_distances = g.dijkstra(src)
print("Shortest distances from source vertex", src, ":", shortest_distances)
