# top_k

## Description

`top_k` is similar to `top_p`, but instead of selecting tokens based on cumulative probability, it selects the top k tokens with the highest probabilities. After sorting the tokens by their probabilities, only the top k are considered for sampling. This increases the diversity of words used in the generated text. The value of `top_k` is an integer between 1 and n (n being a natural number).

These parameters are used for sampling in next-word prediction. If a model doesn't use them, the model defaults to the greedy approach, where it always selects the token with the highest probability. While this greedy method might seem logical, it can have some drawbacks.
