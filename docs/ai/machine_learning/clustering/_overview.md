# Overview

## Description

Centroid-based clustering and density-based clustering are two popular approaches used for grouping data into clusters:

<img src="centroid_vs_density_based.png" style="width:500px" />

Centroid-Based Clustering:

- Relies on defining clusters around central points (centroids).
- Assigns data points to the nearest centroid based on distance (e.g., Euclidean distance).
- Common algorithm: **k-means**.
- Works well with spherical, evenly sized clusters.
- Sensitive to initialization (choice of initial centroids) and outliers.
- Requires specifying the number of clusters (k) in advance.

Density-Based Clustering:

- Groups data based on areas of high density separated by areas of low density.
- Identifies clusters of arbitrary shapes and sizes.
- Can detect noise and outliers as points not belonging to any cluster.
- Common algorithm: **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise).
- Does not require specifying the number of clusters but requires density parameters like `eps` (distance threshold) and `minPts` (minimum points per cluster).

Key Difference:

- Centroid-based clustering depends on distance to a central point, while density-based clustering focuses on the density of data points.
- Density-based methods are better for handling complex shapes and outliers, whereas centroid-based methods are computationally simpler and suited for compact clusters.
