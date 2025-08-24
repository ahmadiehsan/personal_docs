# Vs (Linear & Binary & Tree & Hash search)

## Description

|                    | Linear search | Binary search         | Tree search                 | Hash search                |
| ------------------ | ------------- | --------------------- | --------------------------- | -------------------------- |
| Search element     | $O(n)$        | $O(\log n)$           | $O(\log n)$                 | $O(1)$                     |
| Insert element     | $O(1)$        | $O(n)$                | $O(\log n)$                 | $O(1)$                     |
| Delete element     | $O(n)$        | $O(n)$                | $O(\log n)$                 | $O(1)$                     |
| Extra space        | $O(1)$        | $O(1)$                | $O(n)$                      | $O(n)$                     |
| Data preprocessing | /             | Sorting $O(n \log n)$ | Building tree $O(n \log n)$ | Building hash table $O(n)$ |
| Data orderliness   | Unordered     | Ordered               | Ordered                     | Unordered                  |

- **Linear search**: Is ideal for small or frequently updated (volatile) data.
- **Binary search**: Works well for large and sorted data.
- **Hash search**: Is suitable for data that requires high query efficiency and does not need range queries.
- **Tree search**: Is best suited for large dynamic data that require maintaining order and need to support range queries.
