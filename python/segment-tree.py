class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)

    def build(self, node, start, end):
        if start == end:  # Leaf node
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node + 1, start, mid)
            self.build(2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, node, start, end, left, right):
        if right < start or left > end:
            return 0  # Out of range
        if left <= start and right >= end:
            return self.tree[node]  # Completely inside the range

        # Partially inside the range
        mid = (start + end) // 2
        left_sum = self.query(2 * node + 1, start, mid, left, right)
        right_sum = self.query(2 * node + 2, mid + 1, end, left, right)
        return left_sum + right_sum

    def update(self, node, start, end, index, value):
        if start == end:  # Leaf node
            self.arr[index] = value
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if index <= mid:
                self.update(2 * node + 1, start, mid, index, value)
            else:
                self.update(2 * node + 2, mid + 1, end, index, value)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def build_tree(self):
        self.build(0, 0, self.n - 1)

    def query_range(self, left, right):
        return self.query(0, 0, self.n - 1, left, right)

    def update_value(self, index, value):
        self.update(0, 0, self.n - 1, index, value)


# Example usage:
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)
seg_tree.build_tree()

print(seg_tree.query_range(1, 4))  # Query the sum of elements in range [1, 4]
seg_tree.update_value(2, 6)        # Update element at index 2 to 6
print(seg_tree.query_range(1, 4))  # Query again after the update
