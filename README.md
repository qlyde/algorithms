# algorithms

A random assortment of algorithms, what they're used for, their implementations in Python, their complexity analyses and relevant examples.

* [Segment Tree](#segment-tree)
* [Union-Find (Disjoint-Set Union)](#union-find-disjoint-set-union)
* [Topological Sorting](#topological-sorting)
* [Kadane's Algorithm](#kadanes-algorithm)
* [Rabin-Karp Algorithm](#rabin-karp-algorithm)
* [Knuth-Morris-Pratt (KMP) Algorithm](#knuth-morris-pratt-kmp-algorithm)
* [Dijkstra's Algorithm](#dijkstras-algorithm)

## [Segment Tree](/python/segment-tree.py)

Used to perform range queries and updates.

* Height `ceil(log n)`
* Number of nodes `1 + 2 + 4 + 8 + ... + 2^(log n) = 2^(log n + 1) - 1 < 4n` (sum of a geometric series)
* `O(n)` time for building the tree
* `O(log n)` time for queries and updates
* `O(n)` space

**Examples:**

* [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/description/)

## [Union-Find (Disjoint-Set Union)](/python/union-find.py)

Used for managing disjoint sets and supports two main operations: union (combining two sets) and find (determining to which set an element belongs to).

* `O(n)` time for union and find
* Amortized `O(log n)` time with rank optimization
* Amortized `O(1)` time with rank optimization and path compression
* `O(n)` space

**Examples:**

* [Number of Provinces](https://leetcode.com/problems/number-of-provinces/description/)

## [Topological Sorting](/python/topological-sorting.py)

A linear ordering of the vertices in a directed acyclic graph (DAG) in such a way that for every directed edge `u -> v`, the vertex `u`  comes before `v` in the ordering.

* `O(V + E)` time
* `O(V)` space

**Examples:**

* [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/)

## [Kadane's Algorithm](/python/kadanes-algorithm.py)

Used to find the maximum subarray sum in an array of integers. Based on dynamic programming.

* `O(n)` time
* `O(1)` space

**Examples:**

* [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)

## [Rabin-Karp Algorithm](/python/rabin-karp-algorithm.py)

A string searching algorithm that finds the occurrences of a pattern within a text. It uses hashing to quickly compare the pattern to potential substrings in the text.

* Time complexity depends on the hash function used
* Typically linear in the length of the text
* Worst case `O((n + m - 1) * m)` time, where `m` is the length of the pattern and `n` is the length of the text
* Typically `O(1)` space

**Examples:**

* [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)

## [Knuth-Morris-Pratt (KMP) Algorithm](/python/kmp-algorithm.py)

A string searching algorithm that finds the occurrences of a pattern within a text. It uses a "LPS" array to skip unnecessary comparisons during the search.

* `O(n + m)` time
* `O(m)` space due to the LPS array

**Examples:**

* [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)

## [Dijkstra's Algorithm](/python/dijkstras-algorithm.py)

Used to find the shortest paths from a single source vertex to all other vertices in a weighted graph with non-negative edge weights. The algorithm maintains a set of vertices with known shortest distances and gradually explores and updates the distances to other vertices.

* `O((V + E) * log V)` time using a priority queue
* `O(V + E)` space

**Examples:**

* [Network Delay Time](https://leetcode.com/problems/network-delay-time/description/)
