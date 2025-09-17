# Active learning [Sup]

## Description

This technique involves iteratively selecting the most informative samples for human labeling, based on model uncertainty or expected impact.

Starting with a small, labeled dataset, it trains a model, uses it to identify valuable unlabeled samples, has humans annotate these, and then updates the model.

This cycle repeats, optimizing annotation efforts and improving model performance efficiently.

## Example

```python
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from modAL.models import ActiveLearner
import numpy as np

# Step 1: Create toy dataset
X, y = make_classification(n_samples=100, n_features=5, n_classes=2, random_state=42)

# Step 2: Initial small labeled set + unlabeled pool
X_labeled, y_labeled = X[:5], y[:5]
X_pool, y_pool = X[5:], y[5:]

# Step 3: Define ActiveLearner with RandomForest
learner = ActiveLearner(
    estimator=RandomForestClassifier(),
    X_training=X_labeled,
    y_training=y_labeled,
)

# Step 4: Active learning loop
for i in range(5):  # 5 queries
    query_idx, query_inst = learner.query(X_pool)
    print(f"Round {i+1}: Model asked for label of sample {query_idx[0]}")

    # "Oracle/Human" gives true label
    learner.teach(X_pool[query_idx], y_pool[query_idx])

    # Remove from pool
    X_pool = np.delete(X_pool, query_idx, axis=0)
    y_pool = np.delete(y_pool, query_idx, axis=0)

print("Final training complete!")
```
