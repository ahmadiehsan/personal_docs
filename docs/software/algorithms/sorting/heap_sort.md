# Heap Sort {In-Place} {Non-Stable} {$O(n \log n)$}

## Description

Heap sort is an efficient sorting algorithm based on the heap data structure.
We can implement heap sort using the "heap creation" and "element extraction" operations we have already learned.

1. Input the array and construct a min-heap, where the smallest element is at the top of the heap.
2. Continuously perform the extraction operation, record the extracted elements sequentially to obtain a sorted list from smallest to largest.

!!! info

    Although the above method is feasible, it requires an additional array to store the popped elements, which is somewhat space-consuming. In practice, we usually use a more elegant implementation.

## Workflow

Suppose the array length is $n$, the heap sort process is as follows.

1. Input the array and establish a max-heap. After this step, the largest element is positioned at the top of the heap.
2. Swap the top element of the heap (the first element) with the heap's bottom element (the last element). Following this swap, reduce the heap's length by 1 and increase the sorted elements count by 1.
3. Starting from the heap top, perform the sift-down operation from top to bottom. After the sift-down, the heap's property is restored.
4. Repeat steps `2.` and `3.` Loop for $n - 1$ rounds to complete the sorting of the array.

!!! info

    In fact, the element extraction operation also includes steps `2.` and `3.`, with an additional step to pop (remove) the extracted element from the heap.

## Specifications

- **Time complexity is** $O(n \log n)$, **non-adaptive sort**: The heap creation uses $O(n)$ time. Extracting the largest element from the heap takes $O(\log n)$ time, looping for $n - 1$ rounds.
- **Space complexity is** $O(1)$, **in-place sort**: A few pointer variables use $O(1)$ space. The element swapping and heapifying operations are performed on the original array.
- **Non-stable sort**: The relative positions of equal elements may change during the swapping of the heap's top and bottom elements.
