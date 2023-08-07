# algorithms

A random assortment of algorithms, what they're used for, their implementations in Python, their complexity analyses and relevant examples.

* [Segment Tree](#segment-tree)
* [Union-Find (Disjoint-Set Union)](#union-find-disjoint-set-union)
* [Topological Sorting](#topological-sorting)

## [Segment Tree](/segment-tree.py)

Used to perform range queries and updates.

![segment-tree](/img/segment-tree.jpeg)

* Height `ceil(log n)`
* Number of nodes `1 + 2 + 4 + 8 + ... + 2^(log n) = 2^(log n + 1) - 1 < 4n` (sum of a geometric series)
* `O(n)` time for building the tree
* `O(log n)` time for queries and updates
* `O(n)` space

**Examples:**

* [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/description/)

## [Union-Find (Disjoint-Set Union)](/union-find.py)

Used for managing disjoint sets and supports two main operations: union (combining two sets) and find (determining to which set an element belongs to).

![union-find](/img/union-find.png)

* `O(n)` time for union and find
* Amortized `O(log n)` time with rank optimization
* Amortized `O(1)` time with rank optimization and path compression
* `O(n)` space

**Examples:**

* [Number of Provinces](https://leetcode.com/problems/number-of-provinces/description/)

## [Topological Sorting](/topological-sorting.py)

A linear ordering of the vertices in a directed acyclic graph (DAG) in such a way that for every directed edge `u -> v`, the vertex `u`  comes before `v` in the ordering.

![topological-sorting](/img/topological-sorting.png)

* `O(V + E)` time
* `O(V)` space

**Examples:**

* [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/)
