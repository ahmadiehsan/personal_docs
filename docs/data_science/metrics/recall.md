# Recall (TPR) [Classification] [Imbalance]

## Description

Recall, also recognized as sensitivity or the **true positive rate (TPR)**, assesses the ratio of correctly identified positive instances among the total **actual** positive instances.

Recall is useful when the cost of false negatives is high.

!!! info

    A higher Recall indicates that the retrieval component can find a larger proportion of the relevant documents.

## Formula

$$
\text{Recall} = \frac{\text{Number of relevant retrieved instances}}{\text{All relevant instances}}
$$

- **Relevant retrieved instances**: Total correctly identified positive instances (True Positives)
- **All relevant instances**: Total actual positive instances (True Positives + False Negative)

## Example

=== "Text"

    If 5 documents in the entire corpus contain information needed to answer a specific query, and the RAG system retrieves 3 of them within the top 10 results, then Recall for that query would be $3/5 = 0.6$

=== "Code"

    ```python
    from sklearn.metrics import recall_score

    y_true = [1, 0, 1, 1, 0]
    y_pred = [1, 0, 1, 0, 0]  # TP=2, FP=0, TN=2, FN=1

    print(recall_score(y_true, y_pred))  # 0.6666666666666666
    ```
