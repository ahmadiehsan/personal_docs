# Vs (Selection & Bubble & Insertion Sort)

## Description

Although bubble sort, selection sort, and insertion sort all have a time complexity of $O(n^2)$, in practice, **insertion sort is commonly used than bubble sort and selection sort**, mainly for the following reasons.

- Bubble sort is based on element swapping, which requires the use of a temporary variable, involving 3 unit operations; insertion sort is based on element assignment, requiring only 1 unit operation. Therefore, **the computational overhead of bubble sort is generally higher than that of insertion sort**.
- The time complexity of selection sort is always $O(n^2)$. **Given a set of partially ordered data, insertion sort is usually more efficient than selection sort.**
- Selection sort is unstable and cannot be applied to multi-level sorting.
