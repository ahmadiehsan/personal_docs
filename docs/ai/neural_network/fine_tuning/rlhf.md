# RLHF (Reinforcement Learning from Human Feedback) [RL]

## Overview

**RLHF** is a fine-tuning technique for large language models (LLMs) that leverages human feedback to align model outputs with human preferences.
It is widely used to improve safety, helpfulness, and alignment of generative models.

**Pros:**

- Aligns models with human values and preferences.
- Reduces harmful or undesirable outputs.

**Cons:**

- Requires significant human annotation effort.
- Computationally expensive (especially RL phase).
- Reward hacking and misalignment risks.

## Key Steps

1. **Supervised Fine-Tuning (SFT):**
   - Start with a pre-trained model.
   - Fine-tune on a dataset of human demonstrations (input-output pairs).

2. **Reward Model Training:**
   - Collect human preferences by asking annotators to rank or compare model outputs.
   - Train a reward model to predict human preference scores.

3. **Reinforcement Learning (RL):**
   - Use the reward model as a proxy for human feedback.
   - Fine-tune the language model using RL algorithms (e.g., PPO) to maximize the reward.

## Typical Workflow

1. **Data Collection**: Gather human-labeled data (demonstrations and preferences).
2. **SFT**: Fine-tune the base model on demonstration data.
3. **Reward Model**: Train a model to score outputs based on human preferences.
4. **RL Fine-Tuning**: Optimize the model using RL (commonly Proximal Policy Optimization, PPO).

## Use Cases

- Chatbots and conversational agents (e.g., ChatGPT)
- Content moderation
- Instruction-following models
