# Vs (Insertion & Quick Sort)

## Description

The time complexity of insertion sort is $O(n^2)$, while the time complexity of quicksort is $O(n \log n)$.
Although insertion sort has a higher time complexity, **it is usually faster in small input sizes**.

This conclusion is similar to that for linear and binary search.
Algorithms like quicksort that have a time complexity of $O(n \log n)$ and are based on the divide-and-conquer strategy often involve more unit operations.
For small input sizes, the numerical values of $n^2$ and $n \log n$ are close, and complexity does not dominate, with the number of unit operations per round playing a decisive role.

!!! info

    The general approach is: for long arrays, use sorting algorithms based on divide-and-conquer strategies, such as quicksort; for short arrays, use insertion sort directly.

!!! info

    In fact, many programming languages (such as Java) use insertion sort within their built-in sorting functions.
