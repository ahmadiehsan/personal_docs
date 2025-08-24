# Hash Search {Adaptive} {$O(1)$}

## Description

Uses a hash table to establish a key-value mapping between search data and target data, thus implementing the query operation.

**Time complexity**: $O(1)$

<img src="workflow.jpg" style="width:4in" />

!!! info

    Using this algorithm often requires data preprocessing.
    For example, requires the help of additional data structures.
    Maintaining these structures also requires more overhead in terms of time and space.

## Use Cases

- Suitable for scenarios where fast query performance is essential, with an average time complexity of $O(1)$.
- Not suitable for scenarios needing ordered data or range searches, because hash tables cannot maintain data orderliness.
- High dependency on hash functions and hash collision handling strategies, with significant performance degradation risks.
- Not suitable for overly large data volumes, because hash tables need extra space to minimize collisions and provide good query performance.
