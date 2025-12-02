# Backtracking [Top-Down] [Recursion]

## Description

Backtracking algorithm is a method to solve problems by exhaustive search.
Its core concept is to start from an initial state and brutally search for all possible solutions.
The algorithm records the correct ones until a solution is found or all possible solutions have been tried but no solution can be found.

Backtracking typically employs "depth-first search" to traverse the solution space.

!!! info

    Backtracking is an top-down approach that starts from the main problem and explores potential solution paths by recursively breaking it down into smaller subproblems. It systematically searches through possible options, backtracking whenever a path leads to a dead end or an invalid state.

## Workflow

- **Trial and retreat**: It is called a backtracking algorithm because it uses a "trial" and "retreat" strategy when searching the solution space. During the search, whenever it encounters a state where it can no longer proceed to obtain a satisfying solution, it undoes the previous choice and reverts to the previous state so that other possible choices can be chosen for the next attempt.
- **Prune**: Complex backtracking problems usually involve one or more constraints, which are often used for "pruning".

<img src="workflow.png" style="width:688px" />

## Advantages & Limitations

The backtracking algorithm is essentially a depth-first search algorithm that attempts all possible solutions until a satisfying solution is found.
The advantage of this method is that it can find all possible solutions, and with reasonable pruning operations, it can be highly efficient.

However, when dealing with large-scale or complex problems, **the running efficiency of backtracking algorithm may not be acceptable**.

- **Time complexity**: Backtracking algorithms usually need to traverse all possible states in the state space, which can reach exponential or factorial time complexity.
- **Space complexity**: In recursive calls, it is necessary to save the current state (such as paths, auxiliary variables for pruning, etc.). When the depth is very large, the space need may become significantly bigger.

Even so, **backtracking remains the best solution for certain search problems and constraint satisfaction problems**.
For these problems, there is no way to predict which choices can generate valid solutions.
We have to traverse all possible choices.
In this case, **the key is about how to optimize the efficiency**.
There are two common efficiency optimization methods.

- **Prune**: Avoid searching paths that definitely will not produce a solution, thus saving time and space.
- **Heuristic search**: Introduce some strategies or estimates during the search process to prioritize the paths that are most likely to produce valid solutions.

## Use Cases

=== "When to Use"

    Problems suitable for backtracking usually fit the **"decision tree model"**, which can be described using a tree structure, where each node represents a decision, and each path represents a sequence of decisions.

    Backtracking algorithms can be used to solve many search problems, constraint satisfaction problems, and combinatorial optimization problems.

=== "Search"

    The goal of Search problems is to find solutions that meet specific conditions.

    - Full permutation problem: Given a set, find all possible permutations and combinations of it.
    - Subset sum problem: Given a set and a target sum, find all subsets of the set that sum to the target.
    - Tower of Hanoi problem: Given three rods and a series of different-sized discs, the goal is to move all the discs from one rod to another, moving only one disc at a time, and never placing a larger disc on a smaller one.

=== "Constraint Satisfaction"

    The goal of Constraint satisfaction problems is to find solutions that satisfy all the constraints.

    - $n$ queens: Place $n$ queens on an $n \times n$ chessboard so that they do not attack each other.
    - Sudoku: Fill a $9 \times 9$ grid with the numbers $1$ to $9$, ensuring that the numbers do not repeat in each row, each column, and each $3 \times 3$ subgrid.
    - Graph coloring problem: Given an undirected graph, color each vertex with the fewest possible colors so that adjacent vertices have different colors.

=== "Combinatorial Optimization"

    The goal of Combinatorial optimization problems is to find the optimal solution within a combination space that meets certain conditions.

    - 0-1 knapsack problem: Given a set of items and a backpack, each item has a certain value and weight. The goal is to choose items to maximize the total value within the backpack's capacity limit.
    - Traveling salesman problem: In a graph, starting from one point, visit all other points exactly once and then return to the starting point, seeking the shortest path.
    - Maximum clique problem: Given an undirected graph, find the largest complete subgraph, i.e., a subgraph where any two vertices are connected by an edge.

    !!! warning

        Please note that for many combinatorial optimization problems, backtracking is not the optimal solution.

        - The 0-1 knapsack problem is usually solved using dynamic programming to achieve higher time efficiency.
        - The traveling salesman is a well-known NP-Hard problem, commonly solved using genetic algorithms and ant colony algorithms, among others.
        - The maximum clique problem is a classic problem in graph theory, which can be solved using greedy algorithms and other heuristic methods.

## Example

=== "Simple"

    !!! question

        In a binary tree, search for all nodes with a value of 7 and for all matching nodes, **please return the paths from the root node to that node**.

    ```python
    def pre_order(root: TreeNode):
        if root is None:
            return

        # Attempt
        path.append(root)
        if root.val == 7:
            # Record solution
            res.append(list(path))

        pre_order(root.left)
        pre_order(root.right)

        # Retract
        path.pop()
    ```

    <img src="example_simple.png" style="width:7in" />

=== "Pruning"

    !!! question

        In a binary tree, search for all nodes with a value of 7 and return the paths from the root to these nodes, **with restriction that the paths do not contain nodes with a value of 3**.

    ```python
    def pre_order(root: TreeNode):
        if root is None:
            return

        # Pruning
        if root.val == 3:
            return

        # Attempt
        path.append(root)
        if root.val == 7:
            # Record solution
            res.append(list(path))

        pre_order(root.left)
        pre_order(root.right)

        # Retract
        path.pop()
    ```

    <img src="example_pruning.png" style="width:6in" />

=== "Permutation"

    !!! question

        Given an integer array with no duplicate elements, return all possible permutations.

    ```python
    def backtrack(state: list[int], choices: list[int], selected: list[bool], res: list[list[int]]):
        # When the state length equals the number of elements, record the solution
        if len(state) == len(choices):
            res.append(list(state))
            return

        # Traverse all choices
        for i, choice in enumerate(choices):
            # Pruning: do not allow repeated selection of elements
            if not selected[i]:
                # Attempt: make a choice, update the state
                selected[i] = True
                state.append(choice)
                # Proceed to the next round of selection
                backtrack(state, choices, selected, res)
                # Retract: undo the choice, restore to the previous state
                selected[i] = False
                state.pop()

    def permutations_i(nums: list[int]) -> list[list[int]]:
        """Permutation I"""
        res = []
        backtrack(state=[], choices=nums, selected=[False] * len(nums), res=res)
        return res
    ```

    <img src="example_permutation.png" style="width:688px" />

=== "Fibonacci"

    ```python
    def fibonacci(n, memo={}):
        # If result already computed, return it
        if n in memo:
            return memo[n]

        # Base cases
        if n <= 1:
            return n

        # Recursively compute and store result
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]

    print(fibonacci(10))  # 55
    ```
