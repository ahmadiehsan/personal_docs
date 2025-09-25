# RLHF [RL] {DPO} {Online RL}

## Description

=== "RLHF"

    **RLHF (Reinforcement Learning from Human Feedback)** is a fine-tuning technique for large language models (LLMs) that leverages human feedback to align model outputs with human preferences.
    It is widely used to improve safety, helpfulness, and alignment of generative models.

    **Pros:**

    - Aligns models with human values and preferences.
    - Reduces harmful or undesirable outputs.

    **Cons:**

    - Requires significant human annotation effort.
    - Computationally expensive (especially RL phase).
    - Reward hacking and misalignment risks.

=== "DPO"

    **Direct Preference Optimization (DPO)** is a fine-tuning method for aligning large language models (LLMs) with human preferences, **without the need for reinforcement learning or reward modeling**.
    DPO directly optimizes the model to prefer outputs that are rated higher by humans, using pairs of preferred and less-preferred responses.

    !!! info

        DPO is designed to be more efficient and easier to implement than RLHF, as it avoids the complexity of training a separate reward model and reinforcement learning loop.

=== "Online RL"

    **Online Reinforcement Learning** is a method for continuously improving language models by gathering **real-time** feedback and updating the model in a loop.
    Unlike static datasets, Online RL allows a model to learn from **its own deployed outputs**, incorporating fresh human (or synthetic) feedback into the training process.
    This enables adaptive alignment with evolving user preferences and tasks.

    <img src="overview.png" style="width:4.5in" />

## Workflow

=== "RLHF"

    1. **Supervised Fine-Tuning (SFT):**

       - Start with a pre-trained model.
       - Fine-tune on a dataset of human demonstrations (input-output pairs).

    2. **Reward Model Training:**

       - Collect human preferences by asking annotators to rank or compare model outputs.
       - Train a reward model to predict human preference scores.

    3. **Reinforcement Learning (RL):**

       - Use the reward model as a proxy for human feedback.
       - Fine-tune the language model using RL algorithms (e.g., PPO) to maximize the reward.

=== "DPO"

    1. **Collect Preference Data**: Gather pairs of model outputs for the same prompt, labeled as "preferred" and "less preferred" by humans.
    2. **Initialize Model**: Start with a pretrained language model.
    3. **Fine-Tune with DPO Loss**: Train the model using a loss function that increases the likelihood of preferred responses over less-preferred ones.
    4. **Evaluate**: Assess alignment and performance on preference-based benchmarks.

    !!! warning

        DPO requires high-quality preference data. Poorly labeled or inconsistent preferences can degrade model alignment.

=== "Online RL"

    1. **Deployment & Feedback Loop**: Deploy the model and collect interaction data from users, including implicit or explicit preference signals (e.g., thumbs up/down, rankings).
    2. **Reward Model Updates**: Continuously update or retrain the reward model using new preference data.
    3. **Policy Optimization:**

       - Use algorithms like **Proximal Policy Optimization (PPO)** to fine-tune the language model against the reward model.
       - Optionally use **Generalized Reward Policy Optimization (GRPO)** to better handle non-stationary rewards and long-horizon feedback.

    4. **Evaluation**: Periodically assess model behavior using alignment metrics, task performance, and user satisfaction.

## Optimization Policies

- **PPO (Proximal Policy Optimization)**: A stable, widely-used RL algorithm that prevents large policy updates, reducing training instability.
- **GRPO (Generalized Reward Policy Optimization)**: Extends PPO by incorporating reward generalization techniques, making it more robust to sparse, delayed, or shifting feedback.

<img src="ppo_and_grpo.png" style="width:6in" />

## Example

=== "RLHF"

=== "DPO"

    ```python
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from trl import DPOTrainer

    # Load a pre-trained language model and tokenizer
    model_name = "gpt2"
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Define the dataset containing human preference pairs
    # Each entry in the dataset is a tuple (prompt, preferred_completion,
    # dispreferred_completion)
    dataset = [
        ("Prompt 1", "Preferred Completion 1", "Dispreferred Completion 1"),
        ("Prompt 2", "Preferred Completion 2", "Dispreferred Completion 2"),
        # Add more data as needed
    ]

    # Initialize the DPO Trainer
    trainer = DPOTrainer(
        model=model,
        tokenizer=tokenizer,
        dataset=dataset,
        beta=0.1  # Hyperparameter controlling the strength of preference optimization
    )

    # Train the model using DPO
    trainer.train()

    # Save the fine-tuned model
    model.save_pretrained("fine-tuned-model")
    tokenizer.save_pretrained("fine-tuned-model")
    ```

=== "Online RL"

    ```python
    def ppo_step(base_model, reward_model, optimizer, prompt, num_iterations=5):
        for _ in range(num_iterations):
            # Generate text
            outputs = base_model.generate(prompt, max_length=100, return_dict_in_generate=True, output_scores=True)
            generated_text = tokenizer.decode(outputs.sequences[0],skip_special_tokens=True)

            # Get reward
            reward = reward_model(generated_text)

            # Compute policy loss
            log_probs = outputs.scores[0].log_softmax(dim=-1)
            policy_loss = -log_probs * reward

            # Update model
            optimizer.zero_grad()
            policy_loss.mean().backward()
            optimizer.step()

        return base_model
    ```
