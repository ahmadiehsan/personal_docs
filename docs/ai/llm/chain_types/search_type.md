# Search Type

## Similarity Search

Selects text chunk vectors that are most similar to the question vector.
This approach is straightforward and effective for retrieving documents closest to the query.

Limitation: It may sometimes return documents that are not directly relevant to the question.

## Maximum Marginal Relevance (MMR)

Balances similarity to the query and diversity among the retrieved documents.
Documents are selected based on their closeness to the query as well as their difference from one another.

Advantage: Helps ensure the results are both relevant and varied, providing more informative outputs.

Important hyperparameters:

- **k**: The number of documents to return.
- **top_k**: The number of documents to consider for each iteration of the MMR algorithm.
- **alpha**: The relevance decay factor.
- **beta**: The diversity penalty factor.

## Vs

| Feature       | Similarity Search | MMR Search   |
| ------------- | ----------------- | ------------ |
| **Accuracy**  | Lower             | Higher       |
| **Speed**     | Faster            | Slower       |
| **Diversity** | Less diverse      | More diverse |
