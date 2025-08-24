# Bubble Sort {Stable} {$O(n^2)$}

## Description

Bubble sort works by continuously comparing and swapping adjacent elements.
This process is like bubbles rising from the bottom to the top, hence the name "bubble sort."

## Workflow

Assume the array has length $n$. The steps of bubble sort are:

1. First, perform one "bubble" pass on $n$ elements, **swapping the largest element to its correct position**.
2. Next, perform a "bubble" pass on the remaining $n - 1$ elements, **swapping the second largest element to its correct position**.
3. Continue in this manner; after $n - 1$ such passes, **the largest $n - 1$ elements will have been moved to their correct positions**.
4. The only remaining element **must** be the smallest, so **no** further sorting is required. At this point, the array is sorted.

<img src="workflow.jpg" style="width:5in" />

## Specifications

- **Time complexity of $O(n^2)$, adaptive sorting.** Each round of "bubbling" traverses array segments of length $n - 1, n - 2, \ldots, 2, 1$, which sums to $\frac{(n - 1)n}{2}$. With a `flag` optimization, the best-case time complexity can reach $O(n)$ when the array is already sorted.
- **Space complexity of $O(1)$, in-place sorting.** Only a constant amount of extra space is used by pointers $i$ and $j$.
- **Stable sorting.** Because equal elements are not swapped during "bubbling," their original order is preserved, making this a stable sort.
