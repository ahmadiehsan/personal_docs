# Red-Black Tree (Balanced Binary Search Tree)

## Description

Red-black trees are a type of balanced binary search tree that ensures the tree remains approximately balanced during insertions and deletions. They maintain balance through a set of properties that dictate the color (red or black) of each node, ensuring that no path from the root to a leaf is more than twice as long as any other such path.

Properties of Red-Black Trees:

These properties ensure that the **longest path from the root to the leaf is no more than twice the length of the shortest path**, maintaining a balanced structure.

- **Node Color**: Every node is colored either red or black.
- **Root Property**: The root of the tree is always black.
- **Red Property**: Red nodes cannot have red children (no two red nodes can be adjacent).
- **Black Property**: Every path from a node to its descendant leaves must contain the same number of black nodes.
- **Leaf Property**: All leaves (NIL nodes) are considered black.

Benefits of Red-Black Trees:

- **Efficient Insertions and Deletions**: Compared to AVL trees, red-black trees perform fewer rotations during insertions and deletions, leading to better average-case efficiency.
- **Balanced Structure**: The balancing properties allow red-black trees to maintain a time complexity of O(log n) for search, insert, and delete operations, even after a series of modifications.
- **Versatility**: Red-black trees are used in various applications, including:

   - Implementation of associative arrays and dictionaries in programming libraries.
   - Managing data in systems where frequent insertions and deletions occur, such as in memory management.
