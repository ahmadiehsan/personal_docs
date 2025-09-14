# Active learning

## Description

This technique involves iteratively selecting the most informative samples for human labeling, based on model uncertainty or expected impact.

Starting with a small, labeled dataset, it trains a model, uses it to identify valuable unlabeled samples, has humans annotate these, and then updates the model.

This cycle repeats, optimizing annotation efforts and improving model performance efficiently.

## Example

```python
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

# Step 1: Create a toy dataset
X, y = make_classification(n_samples=100, n_features=2, n_classes=2, random_state=42)

# Split into unlabeled pool and a small labeled set
X_labeled, y_labeled = X[:5], y[:5]      # start with 5 labeled
X_pool, y_pool = X[5:], y[5:]            # the rest unlabeled

model = LogisticRegression()

for i in range(5):  # do 5 rounds of "active learning"
    # Train on current labeled data
    model.fit(X_labeled, y_labeled)

    # Pick the most uncertain sample (closest to 0.5 probability)
    probs = model.predict_proba(X_pool)[:,1]
    uncertainty = np.abs(probs - 0.5)
    query_idx = np.argmin(uncertainty)

    # Simulate oracle: reveal true label
    X_new, y_new = X_pool[query_idx].reshape(1, -1), [y_pool[query_idx]]
    print(f"Round {i+1}: Model asked for label of one sample -> got {y_new[0]}")

    # Add this new data to labeled set
    X_labeled = np.vstack([X_labeled, X_new])
    y_labeled = np.append(y_labeled, y_new)

    # Remove it from the pool
    X_pool = np.delete(X_pool, query_idx, axis=0)
    y_pool = np.delete(y_pool, query_idx, axis=0)

y_pred = model.predict(X)  # Final accuracy on all data
print("Final accuracy:", accuracy_score(y, y_pred))
```
