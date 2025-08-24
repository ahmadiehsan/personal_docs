# Tree Search {Adaptive} {$O(\log n)$}

## Description

In a specific tree structure (such as a **binary search tree**), quickly eliminates nodes based on node value comparisons, thus locating the target element.

**Time complexity**: $O(\log n)$

<img src="workflow.jpg" style="width:3in" />

!!! info

    Using this algorithm often requires data preprocessing.
    For example, requires the help of additional data structures.
    Maintaining these structures also requires more overhead in terms of time and space.

## Use Cases

- Suitable for massive data, because tree nodes are stored scattered in memory.
- Suitable for maintaining ordered data or range searches.
- With the continuous addition and deletion of nodes, the binary search tree may become skewed, degrading the time complexity to $O(n)$.
- If using AVL trees or red-black trees, operations can run stably at $O(\log n)$ efficiency, but the operation to maintain tree balance adds extra overhead.
