# Dynamic Programming [Bottom-Up] [Loop]

## Description

Dynamic programming is an important algorithmic paradigm that decomposes a problem into a series of smaller subproblems, and stores the solutions of these subproblems to avoid redundant computations, thereby significantly improving time efficiency.

!!! info

    Dynamic programming is a bottom-up method: starting with the solutions to the smallest subproblems, it iteratively constructs the solutions to larger subproblems until the original problem is solved.

## Workflow

Dynamic programming is commonly used to solve optimization problems, which not only include overlapping subproblems but also have two other major characteristics: optimal substructure and statelessness.

=== "Optimal Substructure"

    The optimal solution to the original problem is constructed from the optimal solutions of subproblems. This means:

    1. The problem can be broken down into smaller subproblems
    2. The optimal solution to the original problem contains optimal solutions to its subproblems
    3. Solutions to subproblems can be combined to form the solution to the larger problem

    For example, in the climbing stairs problem:

    - To find the number of ways to climb n stairs
    - We need the optimal solutions for (n-1) and (n-2) stairs
    - The total number of ways is the sum of these two subproblem solutions
    - Each subproblem solution is itself optimal and independent

=== "Statelessness"

    Statelessness is one of the important characteristics that make dynamic programming effective in solving problems.
    Its definition is: **Given a certain state, its future development is only related to the current state and unrelated to all past states experienced**.

    Taking the stair climbing problem as an example, given state $i$, it will develop into states $i+1$ and $i+2$, corresponding to jumping 1 step and 2 steps respectively.
    When making these two choices, we do not need to consider the states before state $i$, as they do not affect the future of state $i$.

## Example

=== "Climbing Stairs"

    !!! question

        Given a staircase with n steps, where you can climb 1 or 2 steps at a time, how many different ways are there to reach the top?

    ```python
    def climbing_stairs_dp(n: int) -> int:
        """Climbing stairs: Dynamic programming"""
        if n == 1 or n == 2:
            return n

        # Initialize dp table, used to store subproblem solutions
        dp = [0] * (n + 1)
        # Initial state: preset the smallest subproblem solution
        dp[1], dp[2] = 1, 2

        # State transition: gradually solve larger subproblems from smaller ones
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
    ```

    ![](dynamic_programming/example_stairs.png)

=== "Fibonacci"

    ```python
    def fibonacci(n):
        # Base cases
        if n <= 1:
            return n

        # Create an array to store results
        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, 1
        # Build the table bottom-up
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    print(fibonacci(10))  # Output: 55
    ```

=== "Fibonacci (Simple)"

    ```python
    def fibonacci(n):
        if n <= 1:
            return n

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    print(fibonacci(10))  # Output: 55
    ```

    !!! info

        Here we used simpler and more memory-efficient version of dynamic programming ($O(n)$ space)
