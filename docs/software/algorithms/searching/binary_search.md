# Binary Search [$O(\log n)$] [Adaptive]

## Description

Binary search is an efficient search algorithm that uses a divide-and-conquer strategy.
It takes advantage of the **sorted order** of elements in an array by reducing the search interval by half in each iteration, continuing until either the target element is found or the search interval becomes empty.

- **Time complexity**: $O(\log n)$ : In the binary loop, the interval decreases by half each round, hence the number of iterations is $\log_2 n$.
- **Space complexity**: $O(1)$ : Pointers $i$ and $j$ occupies constant size of space.

<img src="workflow_overview.jpg" style="width:3in" />

!!! info

    Using this algorithm often requires data preprocessing.
    For example, requires sorting the array in advance.
    Maintaining these structures also requires more overhead in terms of time and space.

## Workflow

=== "<1>"

    <img src="workflow_step_1.png"  />

=== "<2>"

    <img src="workflow_step_2.png"  />

=== "<3>"

    <img src="workflow_step_3.png"  />

=== "<4>"

    <img src="workflow_step_4.png"  />

=== "<5>"

    <img src="workflow_step_5.png"  />

=== "<6>"

    <img src="workflow_step_6.png"  />

=== "<7>"

    <img src="workflow_step_7.png"  />

## Advantages & Limitations

Binary search performs well in both time and space aspects.

- Binary search is time-efficient. With large dataset, the logarithmic time complexity offers a major advantage. For instance, given a dataset with size $n = 2^{20}$, linear search requires $2^{20} = 1048576$ iterations, while binary search only demands $\log_2 2^{20} = 20$ loops.
- Binary search does not need extra space. Compared to search algorithms that rely on additional space (like hash search), binary search is more space-efficient.

However, binary search may not be suitable for all scenarios due to the following concerns.

- Binary search can only be **applied to sorted data**. Unsorted data must be sorted before applying binary search, which may not be worthwhile as sorting algorithm typically has a time complexity of $O(n \log n)$. Such cost is even higher than linear search, not to mention binary search itself. For scenarios with frequent insertion, the cost of remaining the array in order is pretty high as the time complexity of inserting new elements into specific positions is $O(n)$.
- Binary search may **use array only**. Binary search requires non-continuous (jumping) element access, which is inefficient in linked list. As a result, linked list or data structures based on linked list may not be suitable for this algorithm.
- Linear search performs better on small dataset. In linear search, only 1 decision operation is required for each iteration; whereas in binary search, it involves 1 addition, 1 division, 1 to 3 decision operations, 1 addition (subtraction), totaling 4 to 6 operations. Therefore, if data size $n$ is small, linear search is faster than binary search.

## Use Cases

- Suitable for larger data volumes, with stable performance and a worst-case time complexity of $O(\log n)$.
- However, the data volume cannot be too large, because storing arrays requires contiguous memory space.
- Not suitable for scenarios with frequent additions and deletions, because maintaining an ordered array incurs a lot of overhead.
