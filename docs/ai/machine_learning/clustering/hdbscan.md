# HDBSCAN * [Unsup] [Density-Based]

## Description

Hierarchical Density-Based Spatial Clustering of Applications with Noise (HDBSCAN) is a hierarchical variation of a clustering algorithm that allows for dense (micro)-clusters to be found **without having to explicitly specify the number of clusters**.

!!! info

    As a density-based method, HDBSCAN can also detect outliers in the data, which are data points that do not belong to any cluster.
    These outliers will not be assigned or forced to belong to any cluster.

## Workflow

1. For each instance, the algorithm counts how many instances are located within a small distance $\epsilon$ (epsilon) from it. This region is called the instance's $\epsilon$-neighborhood.
2. If an instance has at least `min_samples` instances in its $\epsilon$-neighborhood (including itself), then it is considered a core instance. In other words, core instances are those that are located in dense regions.
3. All instances in the neighborhood of a core instance belong to the same cluster. This neighborhood may include other core instances; therefore, a long sequence of neighboring core instances forms a single cluster.
4. Any instance that is not a core instance and does not have one in its neighborhood is considered an anomaly.

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
len(set(clusters))  # 156
```

!!! info

    With HDBSCAN, we generated 156 clusters in our dataset. To create more clusters, we will need to reduce the value of `min_cluster_size` as it represents the minimum size that a cluster can take.
