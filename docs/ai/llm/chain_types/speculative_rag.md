# Speculative RAG [RAG]

## Description

Speculative RAG is an approach that involves generating multiple possible responses or outputs for a given input query, using a retrieval model to provide relevant information.
The generated responses are then evaluated using a feedback mechanism to select the most plausible or relevant one.
The goal is to enhance the model’s ability to produce accurate and contextually appropriate answers, especially when there is ambiguity or multiple potential interpretations of a query.

## Workflow

- **Step 1 - Retrieval**: Similar to Standard RAG, it starts by retrieving multiple documents relevant to the query.
- **Step 2 - Generative Speculation**: The generative model creates multiple speculative responses based on the retrieved documents. Instead of producing a single answer, it explores several possible outputs.
- **Step 3 - Feedback and Ranking**: Each of the generated responses is evaluated using a feedback mechanism that scores them based on various criteria like relevance, coherence, completeness, and factual accuracy. This could involve comparing the responses against additional retrieved documents or using scoring models.
- **Step 4 - Selection Process**: The model ranks all possible responses and selects the highest-scoring one as the final output.
- **Step 5 - Presentation**: The chosen response is then presented to the user as the final answer.
