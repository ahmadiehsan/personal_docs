# Isomap [Manifold] [Unsup]

## Description

Isometric Feature Mapping (Isomap) creates a graph by connecting each instance to its nearest neighbors, then reduces dimensionality while trying to preserve the geodesic distances between the instances.

The geodesic distance between two nodes in a graph is the number of nodes on the shortest path between these nodes.

!!! info

    This approach works best when the data lies on a fairly smooth and low-dimensional manifold with a single global structure (e.g., the Swiss roll).
