# Overview

## Glossary

- **Execution efficiency**: We expect the time complexity of sorting algorithms to be as low as possible, as well as a lower number of overall operations (lowering the constant term of time complexity). For large data volumes, execution efficiency is particularly important.
- **In-place property**: As the name implies, in-place sorting is achieved by directly manipulating the original array, without the need for additional helper arrays, thus saving memory. Generally, in-place sorting involves fewer data moving operations and is faster.
- **Adaptability**: Adaptive sorting leverages existing order information within the input data to reduce computational effort, achieving more optimal time efficiency. The best-case time complexity of adaptive sorting algorithms is typically better than their average-case time complexity.
- **Comparison**: Comparison-based sorting relies on comparison operators (<, =, >) to determine the relative order of elements and thus sort the entire array, with the theoretical optimal time complexity being $O(n \log n)$.
- **Non-Comparison**: Non-Comparison sorting does not use comparison operators and can achieve a time complexity of $O(n)$, but its versatility is relatively poor.
- **Stability**: Stable sorting ensures that the relative order of equal elements in the array does not change after sorting.

  Stable sorting is a necessary condition for multi-key sorting scenarios. Suppose we have a table storing student information, with the first and second columns being name and age, respectively. In this case, unstable sorting might lead to a loss of order in the input data:

  ```python
  # Input data is sorted by name
  # (name, age)
  ("A", 19)
  ("B", 18)
  ("C", 21)
  ("D", 19)
  ("E", 23)

  # Assuming an unstable sorting algorithm is used to sort the list by age,
  # the result changes the relative position of ("D", 19) and ("A", 19),
  # and the property of the input data being sorted by name is lost
  ("B", 18)
  ("D", 19)
  ("A", 19)
  ("C", 21)
  ("E", 23)
  ```
