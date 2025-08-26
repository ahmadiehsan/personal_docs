# BFS & DFS [$O(n)$] [Brute-Force]

## Description

Breadth-first search (BFS) and Depth-first search (DFS) locate the target element by traversing every element of the data structure.

They are two traversal strategies for **graphs** and **trees**.

- **BFS**: starts from the initial node and searches layer by layer (left to right), accessing nodes from near to far.
- **DFS**: starts from the initial node, follows a path until the end (top to bottom), then backtracks and tries other paths until the entire data structure is traversed.

**Time complexity:** $O(n)$, where $n$ is the number of elements, so the performance is poor with large data sets.

!!! info

    The advantage is its simplicity and versatility, **no need for data preprocessing or the help of additional data structures**.
