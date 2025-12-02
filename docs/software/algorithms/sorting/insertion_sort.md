# Insertion Sort * [$O(n^2)$] [Stable] [In-Place]

## Description

Insertion sort is a simple sorting algorithm that works very much like the process of manually sorting a deck of cards.

Specifically, we select a base element from the unsorted interval, compare it with the elements in the sorted interval to its left, and insert the element into the correct position.

## Workflow

1. Consider the first element of the array as sorted.
2. Select the second element as `base`, insert it into its correct position, **leaving the first two elements sorted**.
3. Select the third element as `base`, insert it into its correct position, **leaving the first three elements sorted**.
4. Continuing in this manner, in the final iteration, the last element is taken as `base`, and after inserting it into the correct position, **all elements are sorted**.

<img src="workflow.jpg" style="width:5.25in" />

## Specifications

- **Time complexity is** $O(n^2)$, **adaptive sorting**: In the worst case, each insertion operation requires $n - 1, n - 2, ..., 2, 1$ loops, summing up to $(n - 1)n / 2$, thus the time complexity is $O(n^2)$. In the case of ordered data, the insertion operation will terminate early. When the input array is completely ordered, insertion sort achieves the best time complexity of $O(n)$.
- **Space complexity is** $O(1)$, **in-place sorting**: Pointers $i$ and $j$ use a constant amount of extra space.
- **Stable sorting**: During the insertion operation, we insert elements to the right of equal elements,
  not changing their order.
