# Binary Search Tree [Binary Tree]

## Description

The sorted version of a Binary Tree is called Binary Search Tree, which means:

1. For the root node, the value of all nodes in the left subtree < the value of the root node < the value of all nodes in the right subtree.
2. The left and right subtrees of any node are also binary search trees, i.e., they satisfy condition 1. as well.

<img src="image4.jpg" style="width:3in" />

## Operations

=== "Overview"

    | Operation             | Complexity (Average) | Complexity (Worst) |
    | --------------------- | -------------------- | ------------------ |
    | Search                | $O(\log n)$          | $O(n)$             |
    | Insert                | $O(\log n)$          | $O(n)$             |
    | Delete                | $O(\log n)$          | $O(n)$             |
    | Find min/max          | $O(\log n)$          | $O(n)$             |
    | Successor/Predecessor | $O(\log n)$          | $O(n)$             |
    | Memory space usage    | $O(n)$               | $O(n)$             |

=== "Searching a Node"

    When we are looking for num, we declare a node cur, start from the binary tree's root node root, and loop to compare the size between the node value cur.val and num.

    - If `cur.val < num`, it means the target node is in cur's right subtreep.
    - If `cur.val > num`, it means the target node is in cur's left subtree.
    - If `cur.val = num`, it means the target node is found, exit the loop, and return the node.

    <img src="image1.jpg" style="width:3in" />

=== "Inserting a Node"

    It works like this:

    - **Finding insertion position**: Similar to the search operation, start from the root node, loop downwards according to the size relationship between the current node value and num, until the leaf node is passed (traversed to None), then exit the loop.
    - **Insert the node at this position**: Initialize the node num and place it where None was.

    <img src="image2.jpg" style="width:7in" />

=== "Removing a Node"

    First, find the target node in the binary tree, then remove it.
    Similar to inserting a node, we need to ensure that after the removal operation is completed, the property of the binary search tree "left subtree < root node < right subtree" is still satisfied.

    <img src="image5.jpg" style="width:7in" />

## Vs Binary Tree

| Operation      | Binary Tree (Unsorted tree) | Binary search tree |
| -------------- | --------------------------- | ------------------ |
| Search element | $O(n)$                      | $O(\log n)$        |
| Insert element | $O(1)$                      | $O(\log n)$        |
| Remove element | $O(n)$                      | $O(\log n)$        |
