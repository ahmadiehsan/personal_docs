# Brute-Force Search [BFS] [DFS] [Linear]

## Description

A Brute-force search locates the target element by traversing every element of the data structure.

- **"Linear search"** is suitable for linear data structures such as arrays and linked lists. It starts from one end of the data structure and accesses each element one by one until the target element is found or the other end is reached without finding the target element.
- **"Breadth-first search"** and **"Depth-first search"** are two traversal strategies for graphs and trees.

   - Breadth-first search starts from the initial node and searches layer by layer (left to right), accessing nodes from near to far.
   - Depth-first search starts from the initial node, follows a path until the end (top to bottom), then backtracks and tries other paths until the entire data structure is traversed.

The advantage of brute-force search is its simplicity and versatility, **no need for data preprocessing or the help of additional data structures**.

However, **the time complexity of this type of algorithm is** $O(n)$, where $n$ is the number of elements, so the performance is poor with large data sets.
