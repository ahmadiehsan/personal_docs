# max_token

## Description

The `max_token` parameter defines the maximum number of tokens that the model can process, including both the input (prompt) and the output (completion).
A higher `max_token` value allows the model to generate longer responses but also requires more RAM for execution.

It's important to note that some definitions of `max_token` only refer to the output tokens, while others include both input and output tokens in the total limit.
According to OpenAI's documentation, the limit applies to the combined total of both input and output tokens.

The exact `max_token` limit may vary depending on the model.
One token typically represents about 4 characters of standard English text.
