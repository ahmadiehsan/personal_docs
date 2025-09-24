# DPO (Direct Preference Optimization) [RLHF]

## Description

Direct Preference Optimization (DPO) is a fine-tuning method for aligning large language models (LLMs) with human preferences, **without the need for reinforcement learning or reward modeling**.
DPO directly optimizes the model to prefer outputs that are rated higher by humans, using pairs of preferred and less-preferred responses.

!!! info

    DPO is designed to be more efficient and easier to implement than RLHF, as it avoids the complexity of training a separate reward model and reinforcement learning loop.

## Workflow

1. **Collect Preference Data**: Gather pairs of model outputs for the same prompt, labeled as "preferred" and "less preferred" by humans.
2. **Initialize Model**: Start with a pretrained language model.
3. **Fine-Tune with DPO Loss**: Train the model using a loss function that increases the likelihood of preferred responses over less-preferred ones.
4. **Evaluate**: Assess alignment and performance on preference-based benchmarks.

!!! warning

    DPO requires high-quality preference data. Poorly labeled or inconsistent preferences can degrade model alignment.

## Example

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
