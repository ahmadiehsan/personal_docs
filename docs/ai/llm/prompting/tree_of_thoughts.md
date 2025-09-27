# Tree-of-Thoughts (ToT)

## Descriptions

The "Tree of Thoughts" (ToT) framework enhances complex problem-solving by maintaining a tree of thoughts, allowing language models to explore and evaluate intermediate steps.

![](tree_of_thoughts/image2.png)

It combines thought generation with search algorithms like breadth-first and depth-first search for systematic exploration.
This approach helps identify potential solutions by categorizing thoughts as "sure," "maybe," or "impossible," promoting effective partial solutions while eliminating unfeasible ones.

![](tree_of_thoughts/image1.png)

## Zero-Shot Tree-of-Thoughts

A disadvantage of ToT method is that it requires many calls to the generative models, which slows the application significantly.
Fortunately, there has been a successful attempt to convert the tree-of-thought framework into a simple prompting technique.

Instead of calling the generative model multiple times, we ask the model to mimic that behavior by emulating a conversation between multiple experts.
These experts will question each other until they reach a consensus.

## Example

=== "Prompt"

    ```python
    def tot_prompt(problem):
        prompt = f"""
        Solve the following problem using a Tree-of-Thoughts approach:

        Problem: {problem}

        Let's explore multiple reasoning paths:

        Path 1:
        1) First, we could...
        2) Then, we might...
        3) This leads us to...

        Path 2:
        1) Alternatively, we could start by...
        2) Following this approach...
        3) This results in...

        Path 3:
        1) Another perspective is...
        2) If we consider this...
        3) The outcome would be...

        Now, let's evaluate these paths and determine the most promising solution:

        Evaluation:
        1) Path 1: ...
        2) Path 2: ...
        3) Path 3: ...

        Based on this evaluation, the most promising solution is...

        Therefore, the final answer is...

        Now, apply this Tree-of-Thoughts approach to solve the given problem:

        {problem}

        Let's explore multiple reasoning paths:
        """
        return prompt

    problem = "What is the most efficient way to sort a list of a million integers?"
    prompt = tot_prompt(problem)
    print(prompt)
    ```

=== "Depth-first search"

    ```python
    from transformers import AutoModelForCausalLM, AutoTokenizer

    def dfs_tot(model, tokenizer, problem, max_depth=3, max_branches=3, prune_threshold=0.5):
        def explore_branch(current_thought, current_depth):
            if current_depth == max_depth:
                return current_thought

            prompt = f"{current_thought}\n\nLet's explore further:\n"
            inputs = tokenizer(prompt, return_tensors="pt")
            outputs = model.generate(
                inputs,
                max_length=len(prompt) + 100,
                num_return_sequences=max_branches
            )

            branches = [
                tokenizer.decode(
                    output[len(inputs["input_ids"][0]):],
                    skip_special_tokens=True
                )
                for output in outputs
            ]

            evaluated_branches = [
                (branch, evaluate_thought(current_thought + branch))
                for branch in branches
            ]
            pruned_branches = [
                branch for branch, score in evaluated_branches
                if score > prune_threshold
            ]

            if not pruned_branches:
                return current_thought  # If all branches are pruned, return current thought

            results = [
                explore_branch(current_thought + branch, current_depth + 1)
                for branch in pruned_branches
            ]
            return max(results, key=lambda x: evaluate_thought(x))

        initial_prompt = tot_prompt(problem)
        return explore_branch(initial_prompt, 0)

    def evaluate_thought(thought):
        # Implement logic to evaluate the quality of a thought
        # This could involve coherence, relevance, depth of reasoning, etc.
        # And return a float number as evaluation score
        pass

    model_name = "gpt2-large"
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    problem = "What are the potential long-term effects of artificial intelligence on employment?"
    solution = dfs_tot(model, tokenizer, problem)
    print(solution)
    ```

=== "Multi-step problem"

    ```python
    def multi_step_tot(model, tokenizer, problem_steps):
        full_solution = ""
        for step, question in enumerate(problem_steps):
            prompt = f"""Step {step + 1} of the problem:
            {question}

            Previous steps solution:
            {full_solution}

            Let's use Tree-of-Thoughts to solve this step:
            """

            step_solution = dfs_tot(model, tokenizer, prompt)
            full_solution += (
                f"\n\nStep {step + 1} Solution:\n"
                f"{step_solution}"
            )

        return full_solution

    problem_steps = [
        "What are the main factors contributing to climate change?",
        "How do these factors interact with each other?",
        "What are potential solutions to mitigate climate change?",
        "What are the challenges in implementing these solutions?"
    ]
    solution = multi_step_tot(model, tokenizer, problem_steps)
    print(solution)
    ```

=== "Dynamic"

    ```python
    def dynamic_tot(model, tokenizer, problem, max_depth=5):
        def adapt_structure(current_thought, current_depth):
            if current_depth == max_depth:
                return current_thought

            complexity = assess_complexity(current_thought)
            num_branches = determine_branches(complexity)
            branches = generate_branches(model, tokenizer, current_thought, num_branches)

            results = []
            for branch in branches:
                results.append(adapt_structure(current_thought + branch, current_depth + 1))

            return max(results, key=lambda x: evaluate_thought(x))

        def assess_complexity(thought):
            # Implement logic to assess the complexity of the current thought
            pass

        def determine_branches(complexity):
            # Determine the number of branches based on complexity
            return max(2, min(5, int(complexity * 10)))

        def generate_branches(model, tokenizer, thought, num_branches):
            # Generate branches using the model
            pass

        initial_prompt = tot_prompt(problem)
        return adapt_structure(initial_prompt, 0)
    ```

=== "Zero-Shot"

    ```python
    prompt = """
    Imagine three different experts are answering this question.

    All experts will write down 1 step of their thinking, then share it with the group.
    Then all experts will go on to the next step, etc.

    If any expert realizes they're wrong at any point then they leave.

    The question is: 'The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have?'

    Make sure to discuss the results.
    """
    zeroshot_tot_prompt = [{"role": "user", "content": prompt}]
    outputs = pipe(zeroshot_tot_prompt)
    print(outputs[0]["generated_text"])

    # Output:
    # Expert 1: Step 1 - Start with the initial number of apples: 23 apples.
    # Expert 2: Step 1 - Subtract the apples used for lunch: 23 - 20 = 3 apples remaining.
    # Expert 3: Step 1 - Add the newly bought apples: 3 + 6 = 9 apples.
    # Expert 1: Step 2 - Confirm the final count: The cafeteria has 9 apples.
    # Expert 2: Step 2 - Review the calculations: 23 - 20 = 3, then 3 + 6 = 9. The calculations are correct.
    # Expert 3: Step 2 - Agree with the result: The cafeteria indeed has 9 apples.
    # All experts agree on the final count: The cafeteria has 9 apples.
    ```
