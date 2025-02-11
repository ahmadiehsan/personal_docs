# Repetition Penalty

## Description

The **Repetition Penalty** is used to reduce repetitive and redundant outputs. When applied, it penalizes previously generated tokens, decreasing their likelihood of being selected again during subsequent token generation. This helps improve text diversity and ensures more coherent outputs.

Large language models often produce repetitive phrases or sentences, especially when generating longer outputs. This happens because the model tends to assign higher probabilities to words or phrases that have already appeared, as they seem contextually more relevant. Without repetition penalty, models may create loops, continuously generating the same tokens with high probability.

To address this issue, the repetition penalty lowers the probability of previously generated tokens. The penalty rate is usually set higher than 1 (often between 1.2 and 1.5), which helps prevent repetitive output. Mathematically, the penalty rate can range from 1 to infinity.

## Workflow

The model divides the probability of generating a previously produced token by the repetition penalty rate, effectively lowering its likelihood of being selected again.

## Example

**Without Repetition Penalty**:

Prompt: "The sky is blue and the sea is ....
Answer: The sky is blue and the sea is blue. The sky is blue and the sea is blue.

**With Repetition Penalty (1.2 - 1.5)**:

Prompt: "The sky is blue and the sea is
Answer: The sky is blue and the sea is calm and vast under the bright sun.
