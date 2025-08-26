# Linear Search [$O(n)$] [Brute-Force]

## Description

Linear Search locates the target element by traversing every element of the data structure.

Is suitable for linear data structures such as **arrays** and **linked lists**.
It starts from one end of the data structure and accesses each element one by one until the target element is found or the other end is reached without finding the target element.

**Time complexity:** $O(n)$, where $n$ is the number of elements, so the performance is poor with large data sets.

<img src="workflow.jpg" style="width:3in" />

!!! info

    The advantage is its simplicity and versatility, **no need for data preprocessing or the help of additional data structures**.

!!! info

    Replacing linear search with hash search is a common strategy to optimize runtime performance, reducing the time complexity from $O(n)$ to $O(1)$.

## Use Cases

- Good versatility, no need for any data preprocessing operations.
- Suitable for small volumes of data, where time complexity has a smaller impact on efficiency.
- Suitable for scenarios with very frequent data updates, because this method does not require any additional maintenance of the data.
