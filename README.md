# algorithms

## [Segment Trees](/segment-tree.py)

Used to perform range queries and updates.

* Height `ceil(log n)`
* Number of nodes `1 + 2 + 4 + 8 + ... + 2^(log n) = 2^(log n + 1) - 1 < 4n` (sum of a gemetric series)
* `O(n)` time for building the tree
* `O(log n)` time for queries and updates
* `O(n)` space

Examples:

* [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/description/)

## [Union-Find (Disjoint-Set Union)](/union-find.py)

Used for managing disjoint sets and supports two main operations: union (combining two sets) and find (determining to which set an element belongs to).

* `O(n)` time for union and find
* Amortized `O(log n)` time with rank optimization
* Amortized `O(1)` time with rank optimization and path compression
* `O(n)` space

Examples:

* [Number of Provinces](https://leetcode.com/problems/number-of-provinces/description/)
