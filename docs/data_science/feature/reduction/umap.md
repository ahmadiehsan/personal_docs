# UMAP * [Manifold] [Unsup]

## Description

Uniform Manifold Approximation and Projection (UMAP) handles nonlinear relationships and structures a bit better than PCA.

## Example

```python
from umap import UMAP

# We reduce the input embeddings from 384 dimensions to 5 dimensions
umap_model = UMAP(n_components=5, min_dist=0.0, metric="cosine", random_state=42)
reduced_embeddings = umap_model.fit_transform(embeddings)
```

!!! info

    - We can use the `n_components` parameter to decide the shape of the lower-dimensional space, namely 5 dimensions. Generally, values between 5 and 10 work well to capture high-dimensional global structures.
    - The `min_dist` parameter is the minimum distance between embedded points. We are setting this to 0 as that generally results in tighter clusters. We set `metric` to `cosine` as Euclidean-based methods have issues dealing with high-dimensional data.
