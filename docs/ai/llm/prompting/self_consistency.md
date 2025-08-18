# Self-Consistency

## Description

Using the same prompt multiple times can lead to different results if we allow for a degree of creativity through parameters like `temperature` and `top_p`.
As a result, the quality of the output might improve or degrade depending on the random selection of tokens.
In other words, luck!

To counteract this degree of randomness and improve the performance of generative models, self-consistency was introduced.
This method asks the generative model the same prompt multiple times and takes the majority result as the final answer.
During this process, each answer can be affected by different `temperature` and `top_p` values to increase the diversity of sampling.

Self-consistency is an advanced technique aimed at enhancing the effectiveness of prompt engineering.
It involves sampling multiple reasoning paths using few-shot examples to identify the most reliable answer.
This method significantly improves performance, particularly in tasks requiring arithmetic and commonsense reasoning.

!!! info

    This method can further be improved by adding chain-of-thought prompting to improve its reasoning while only using the answer for the voting procedure.

## Example

Consider a problem where a person is asked about their sister's age based on a past age relationship. Using self-consistency, various outputs are generated, and the most frequent answer is selected as the final response. This approach minimizes errors and increases accuracy.
