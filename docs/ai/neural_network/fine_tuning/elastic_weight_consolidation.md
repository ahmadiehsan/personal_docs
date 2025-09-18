# Elastic Weight Consolidation (EWC) [Sup] [Catastrophic Forgetting]

## Description

EWC solves **catastrophic forgetting**, which is when a model forgets old tasks while learning new ones.
It helps the model accumulate knowledge instead of just replacing it.

The core idea is to apply an "elastic" constraint that **protects the most important weights from a past task**, while **allowing less important weights to change freely** to learn the new one.

EWC determines weight importance using the Fisher Information Matrix.
It then enforces its constraints by **adding a penalty term to the loss function**, making it computationally costly to significantly alter the parameters identified as critical for past tasks.

## Example

```python
import copy

def compute_importance(model, dataset):
    importance = {}
    model.eval()

    for batch in dataset:
        model.zero_grad()
        output = model(batch)
        loss = output.loss
        loss.backward()

        for n, p in model.named_parameters():
            if p.grad is not None:
                if n not in importance:
                    importance[n] = p.grad.data.clone().pow(2)
                else:
                    importance[n] += p.grad.data.clone().pow(2)

    return importance

def ewc_loss(model, old_model, importance, loss, ewc_lambda=0.01):
    for n, p in model.named_parameters():
        if n in importance:
            loss += ewc_lambda * importance[n] * (p - old_model[n]).pow(2).sum()
    return loss

def continual_fine_tune(model, tokenizer, old_dataset, new_dataset):
    old_model = copy.deepcopy(model)
    importance = compute_importance(old_model, old_dataset)

    def compute_loss(model, inputs, return_outputs=False):
        outputs = model(**inputs)
        loss = outputs.loss
        if i > 0 and importance is not None:
            loss = ewc_loss(model, old_model, importance, loss)
        return (loss, outputs) if return_outputs else loss

    trainer = Trainer(
        model=model,
        train_dataset=new_dataset["train"],
        eval_dataset=new_dataset["validation"],
        compute_loss=compute_loss,
        ...
    )
    trainer.train()
```

!!! info

    - `old_dataset` (The Past): Represents the old knowledge you want to preserve. It's used to calculate the importance of each weight—determining what to protect.
    - `new_dataset` (The Present): Represents the new skill you want to learn. It provides the main training objective and calculates the loss for the current task—defining what to learn.
