class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n  # Union by rank optimization

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in the same set

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

    # Without union by rank optimization:

    # def union(self, x, y):
    #     root_x = self.find(x)
    #     root_y = self.find(y)

    #     if root_x != root_y:
    #         self.parent[root_y] = root_x
    #         return True

    #     return False  # Already in the same set


# Example usage:
n = 6  # Number of elements
uf = UnionFind(n)

uf.union(0, 1)
uf.union(2, 3)
uf.union(4, 5)

print(uf.find(1))  # Output: 0
print(uf.find(3))  # Output: 2
print(uf.find(5))  # Output: 4
print(uf.find(0))  # Output: 0
