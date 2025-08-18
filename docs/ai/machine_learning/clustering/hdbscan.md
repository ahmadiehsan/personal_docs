# HDBSCAN

## Description

A common density-based model is Hierarchical Density-Based Spatial Clustering of Applications with Noise (HDBSCAN).
HDBSCAN is a hierarchical variation of a clustering algorithm called DBSCAN that allows for dense (micro)-clusters to be found without having to explicitly specify the number of clusters.
As a density-based method, HDBSCAN can also detect outliers in the data, which are data points that do not belong to any cluster.
These outliers will not be assigned or forced to belong to any cluster.

## Example

```python
from hdbscan import HDBSCAN

# We fit the model and extract the clusters
hdbscan_model = HDBSCAN(
    min_cluster_size=50,
    metric="euclidean",
    cluster_selection_method="eom"
).fit(reduced_embeddings)

clusters = hdbscan_model.labels_

# How many clusters did we generate?
len(set(clusters))
# Output: 156
```

!!! info

    With HDBSCAN, we generated 156 clusters in our dataset. To create more clusters, we will need to reduce the value of `min_cluster_size` as it represents the minimum size that a cluster can take.
