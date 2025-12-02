# Counting Sort [$O(n + m)$] [Stable] [Non-In-Place]

## Description

Counting sort achieves sorting by counting the number of elements, usually applied to integer arrays.

## Workflow

Given an array `nums` of length $n$, where all elements are "non-negative integers", the overall process of counting sort is shown in the figure below.

1. Traverse the array to find the maximum number, denoted as $m$, then create an auxiliary array `counter` of length $m + 1$.
2. **Use `counter` to count the occurrence of each number in `nums`**, where `counter[num]` corresponds to the occurrence of the number `num`. The counting method is simple, just traverse `nums` (suppose the current number is `num`), and increase `counter[num]` by $1$ each round.
3. **Since the indices of `counter` are naturally ordered, all numbers are essentially sorted already**. Next, we traverse `counter`, and fill in `nums` in ascending order of occurrence.

!!! info

    From the perspective of bucket sort, we can consider each index of the counting array `counter` in counting sort as a bucket, and the process of counting as distributing elements into the corresponding buckets. Essentially, counting sort is a special case of bucket sort for integer data.

=== "Overview"

    <img src="workflow_overview.png"  />

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

=== "<8>"

    <img src="workflow_step_8.png"  />

## Specifications

- **Time complexity is $O(n + m)$, non-adaptive sort**: It involves traversing `nums` and `counter`, both using linear time. Generally, $n \gg m$, and the time complexity tends towards $O(n)$.
- **Space complexity is $O(n + m)$, non-in-place sort**: It uses array `res` of lengths $n$ and array `counter` of length $m$ respectively.
- **Stable sort**: Since elements are filled into `res` in a "right-to-left" order, reversing the traversal of `nums` can prevent changing the relative position between equal elements, thereby achieving a stable sort. Actually, traversing `nums` in order can also produce the correct sorting result, but the outcome is unstable.

## Limitations

- **Counting sort is only suitable for non-negative integers**: If you want to apply it to other types of data, you need to ensure that these data can be converted to non-negative integers without changing the original order of the elements. For example, for an array containing negative integers, you can first add a constant to all numbers, converting them all to positive numbers, and then convert them back after sorting is complete.
- **Counting sort is suitable for large datasets with a small range of values**: For example, in the above example, $m$ should not be too large, otherwise, it will occupy too much space. And when $n \ll m$, counting sort uses $O(m)$ time, which may be slower than $O(n \log n)$ sorting algorithms.
