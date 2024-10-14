# AVL Tree (Balanced Binary Search Tree)

## Description

In the "Binary Search Tree" section, we mentioned that after multiple insertions and removals, a binary search tree might degrade to a linked list. In such cases, the time complexity of all operations degrades from O(log n) to O(n).

For example, in the following picture, after two node removal operations, this binary search tree will degrade into a linked list:

<img src="image2.jpg" style="width:5.15733in" />

AVL tree is using the "rotation" operation to restore balance to an unbalanced node without affecting the in-order traversal sequence of the binary tree. In other words, the rotation operation can maintain the property of a "binary search tree" while also turning the tree back into a "balanced binary tree".

![](avl_tree/image1.jpg)

Typical applications of AVL trees:

- Organizing and storing large amounts of data, suitable for scenarios with high-frequency searches and low-frequency intertions and removals.
- Used to build index systems in databases.
- **Red-black** trees are also a common type of balanced binary search tree. Compared to AVL trees, red-black trees have more relaxed balancing conditions, require fewer rotations for node insertion and removal, and have a higher average efficiency for node addition and removal operations.
