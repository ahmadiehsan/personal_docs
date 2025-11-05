# LLE [Manifold] [Unsup]

## Description

Locally Linear Embedding (LLE) is a Nonlinear Dimensionality Reduction (NLDR) technique.
It is a manifold learning technique that does not rely on projections.

In a nutshell, LLE first determines how each training instance linearly relates to its nearest neighbors, then it looks for a low-dimensional representation of the training set where these local relationships are best preserved.
This approach makes it particularly good at unrolling twisted manifolds, especially when there is not too much noise.

!!! info

    LLE does not scale well so it is mostly for small or medium sized datasets.

## Workflow

=== "Summary"

    It works in two main steps:

    1. Reconstructing each data point from its neighbors: Find how each point relates linearly to its neighbors.
    2. Mapping all points into a lower-dimensional space while preserving these relationships: Place all points into a smaller-dimensional space while keeping these local relationships intact.

=== "Reconstructing"

    For each training instance $x^{(i)}$, the algorithm first identifies its $k$ nearest neighbors.
    Then, it tries to reconstruct $x^{(i)}$ as a linear combination of these neighbors.

    In other words, LLE finds weights $w_{ij}$ that minimize the reconstruction error:

    $$
    \hat{\mathbf{W}} = \arg\min_{\mathbf{W}} \sum_{i=1}^{m} \left( x^{(i)} - \sum_{j=1}^{m} w_{ij} x^{(j)} \right)^2
    $$

    - $W$: Is the weight matrix containing all the weights $w_{ij}$

    Constraints:

    - $w_{ij} = 0$ if $x^{(j)}$ is not one of the $k$ nearest neighbors of $x^{(i)}$
    - $\sum_{j=1}^{m} w_{ij} = 1$ for each training instance $i$

    These constraints ensure that each point is expressed only in terms of its nearest neighbors and that the weights are normalized.

    After this step, we obtain the **weight matrix** $\hat{\mathbf{W}}$ (containing the weights $\hat{w}_{ij}$), which encodes the local linear structure of the dataset.

=== "Mapping"

    Next, LLE seeks a new representation of the data in a lower-dimensional space while preserving the relationships captured by $\mathbf{W}$.

    Let $z^{(i)}$ represent the lower-dimensional embedding of $x^{(i)}$.
    LLE finds the embeddings $\mathbf{Z}$ that minimize the following objective:

    $$
    \hat{\mathbf{Z}} = \arg\min_{\mathbf{Z}} \sum_{i=1}^{m} \left( z^{(i)} - \sum_{j=1}^{m} \hat{w}_{ij} z^{(j)} \right)^2
    $$

    - $\mathbf{Z}$: Is the matrix containing all $z^{(i)}$
    - $\hat{w}_{ij}$: Are the optimized weights obtained from Step 1

    This ensures that each embedded point $z^{(i)}$ is reconstructed by its neighbors using the same weights as in the original high-dimensional space.

## Example

```python
from sklearn.datasets import make_swiss_roll
from sklearn.manifold import LocallyLinearEmbedding

X_swiss, _ = make_swiss_roll(n_samples=1000, noise=0.2, random_state=42)  # A 3D dataset shaped like a spiral sheet

lle = LocallyLinearEmbedding(n_components=2, n_neighbors=10, random_state=42)
X_unrolled = lle.fit_transform(X_swiss)
```
