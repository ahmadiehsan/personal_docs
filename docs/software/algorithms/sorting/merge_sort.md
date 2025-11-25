# Merge Sort [$O(n \log n)$] [Stable] [Non-In-Place]

## Description

Merge sort is a sorting algorithm based on the divide-and-conquer strategy, involving the "divide" and "merge" phases.

1. **Divide phase**: Recursively split the array from the midpoint, transforming the sorting problem of a long array into shorter arrays.
2. **Merge phase**: Stop dividing when the length of the sub-array is 1, and then begin merging. The two shorter sorted arrays are continuously merged into a longer sorted array until the process is complete.

!!! info

    For linked lists, merge sort has significant advantages over other sorting algorithms. It can optimize the space complexity of the linked list sorting task to $O(1)$.

## Workflow

As shown in the following picture, the "divide phase" recursively splits the array from the midpoint into two sub-arrays from top to bottom.

1. Calculate the midpoint `mid`, recursively divide the left sub-array (interval `[left, mid]`) and the right sub-array (interval `[mid + 1, right]`).
2. Continue with step `1.` recursively until sub-array length becomes 1, then stops.

The "merge phase" combines the left and right sub-arrays into a sorted array from bottom to top.
It is important to note that, merging starts with sub-arrays of length 1, and each sub-array is sorted during the merge phase.

=== "Overview"

    ![](merge_sort/workflow_overview.png)

=== "<1>"

    ![](merge_sort/workflow_step_1.png)

=== "<2>"

    ![](merge_sort/workflow_step_2.png)

=== "<3>"

    ![](merge_sort/workflow_step_3.png)

=== "<4>"

    ![](merge_sort/workflow_step_4.png)

=== "<5>"

    ![](merge_sort/workflow_step_5.png)

=== "<6>"

    ![](merge_sort/workflow_step_6.png)

=== "<7>"

    ![](merge_sort/workflow_step_7.png)

=== "<8>"

    ![](merge_sort/workflow_step_8.png)

=== "<9>"

    ![](merge_sort/workflow_step_9.png)

=== "<10>"

    ![](merge_sort/workflow_step_10.png)

## Specifications

- **Time complexity of $O(n \log n)$, non-adaptive sort**: The division creates a recursion tree of height $\log n$, with each layer merging a total of $n$ operations, resulting in an overall time complexity of $O(n \log n)$.
- **Space complexity of $O(n)$, non-in-place sort**: The recursion depth is $\log n$, using $O(\log n)$ stack frame space. The merging operation requires auxiliary arrays, using an additional space of $O(n)$.
- **Stable sort**: During the merging process, the order of equal elements remains unchanged.
