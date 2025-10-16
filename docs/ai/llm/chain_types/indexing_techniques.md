# Indexing Techniques [RAG] {HNSW} {IVF}

## Description

Indexing techniques are methods used to organize and search large collections of vector embeddings efficiently.
They determine how data is stored and how queries are processed to find the most similar items quickly and accurately, balancing speed, memory usage, and accuracy depending on the dataset size and requirements.

## Varieties

=== "Brute Force (Flat)"

    Brute Force is one of the Flat indexing techniques that stores all embeddings in a list, array, or vector store.
    During a search, it calculates the distance (e.g., cosine similarity) between the query embedding and every embedding in the index.

    - **Pros**: Simple to implement and perfect accuracy (finds the true nearest neighbors).
    - **Cons**: Slow and computationally expensive for large datasets, as it requires an exhaustive search.
    - **Suitable for**: Very small datasets or when perfect accuracy is an absolute requirement.

=== "HNSW (Graph)"

    Hierarchical Navigable Small World (HNSW) is one of the Graph indexing techniques that organizes embeddings in a multi-layered graph structure, allowing efficient navigation and search for nearest neighbors through graph traversal.

    - **Pros**: Very fast and accurate; often considered the state of the art for ANN search.
    - **Cons**: More complex to implement than IVF, and higher memory overhead due to the graph structure.
    - **Suitable for**: Large datasets where both speed and accuracy are crucial.

=== "IVF (Inverted)"

    Inverted File (IVF) is one of the Inverted indexing techniques that partitions the embedding space into clusters and only searches within the most relevant clusters for a given query, rather than the entire dataset.

    - **Pros**: Faster than a flat index; relatively simple to implement.
    - **Cons**: Approximate (might not always find the true nearest neighbors); accuracy depends on the number of clusters.
    - **Suitable for**: Medium-sized datasets where a good balance between speed and accuracy is needed.

=== "PQ (Inverted)"

    Product Quantization (PQ) is one of the Inverted indexing techniques that compresses embeddings into compact codes using quantization, allowing for efficient storage and fast approximate nearest neighbor search by comparing compressed representations.

    - **Pros**: Significantly reduces memory usage by compressing embeddings; fast search.
    - **Cons**: Approximate, and accuracy depends on the number of subvectors and the size of the codebooks.
    - **Suitable for**: Very large datasets where memory efficiency is a primary concern.

=== "LSH (Hash)"

    Locality sensitive hashing (LSH) is one of the Hash indexing techniques that uses hash functions to map similar embeddings into the same buckets, enabling fast approximate search by only comparing items within the same bucket.

    - **Pros**: Relatively simple; can be distributed across multiple machines
    - **Cons**: Approximate, and performance depends on the choice of hash functions and the number of buckets
    - **Suitable for**: Very large, high-dimensional datasets

## Workflow

=== "Brute Force (Flat)"

    1. **Store**: Saves all embeddings in a list, array, or vector store.
    2. **Search**: For a query, computes the distance (e.g., cosine similarity) between the query embedding and every embedding in the index.
    3. **Sort**: Ranks all results by distance to find the nearest neighbors.

=== "HNSW (Graph)"

    1. **Graph-based**: Constructs a hierarchical graph where each node represents an embedding.
    2. **Layers**: The graph has multiple layers, with the top layer having long-range connections (for faster traversal) and the bottom layer having short-range connections (for accurate search).
    3. **Search**: Starts at a random node in the top layer and greedily moves towards the query embedding by exploring connections. The search progresses down the layers, refining the results.

=== "IVF (Inverted)"

    1. **Clustering**: Divides the embedding space into clusters using algorithms such as k-means.
    2. **Inverted index**: Creates an inverted index that maps each cluster centroid to a list of the embeddings belonging to that cluster.
    3. **Search**: Finds the nearest cluster centroid(s) to the query embedding (Only searches within those clusters, significantly reducing the search space).

=== "PQ (Inverted)"

    1. **Subvectors**: Divides each embedding into multiple subvectors.
    2. **Codebooks**: Creates separate codebooks for each subvector using clustering. Each codebook contains a set of representative subvectors (centroids).
    3. **Encoding**: Encodes each embedding by replacing its subvectors with the closest centroids from the corresponding codebooks. This creates a compressed representation of the embedding.
    4. **Search**: Calculates the approximate distance between the query and the encoded embeddings using pre-computed distances between the query’s subvectors and the codebook centroids.

=== "LSH (Hash)"

    Uses hash functions to map similar embeddings to the same "bucket" with high probability

## Vs

| Requirement                | Suitable Technique |
| -------------------------- | ------------------ |
| Dataset (Small)            | Brute Force        |
| Dataset (Large)            | HNSW, IVF, PQ      |
| Speed                      | HNSW               |
| Accuracy (Excellent)       | Brute Force        |
| Accuracy (Good) with speed | HNSW               |
| Memory constraints         | PQ                 |

## Example

=== "Brute Force (Flat)"

    ```python
    import faiss

    # 1. Create vector store
    dimension = embeddings.shape[1]  # Get the dimensionality of the embeddings
    index = faiss.IndexFlatL2(dimension)  # or faiss.IndexFlatIP
    index.add(embeddings)

    # 2. Search for the k nearest neighbors
    k = 2
    distances, indices = index.search(query_embedding, k)

    print("Nearest neighbors:")
    for i, idx in enumerate(indices[0]):
        print(f" Index: {idx}, Distance: {distances[0][i]}, Sentence: {sentences[idx]}")
    ```

=== "HNSW (Graph)"

    ```python
    import faiss

    # 1. Create vector store
    dimension = embeddings.shape[1]  # Get the dimensionality of the embeddings
    n_neighbors = 32  # Number of neighbors per node (controls speed/accuracy tradeoff)
    index = faiss.IndexHNSWFlat(dimension, n_neighbors)
    index.add(embeddings)

    # 2. Search for the k nearest neighbors
    k = 2
    distances, indices = index.search(query_embedding, k)

    print("Nearest neighbors:")
    for i, idx in enumerate(indices[0]):
        print(f" Index: {idx}, Distance: {distances[0][i]}, Sentence: {sentences[idx]}")
    ```

=== "IVF (Inverted)"

    ```python
    import faiss

    # 1. Create vector store
    dimension = embeddings.shape[1]  # Get the dimensionality of the embeddings
    n_clusters = 100  # Number of clusters (centroids)
    quantizer = faiss.IndexFlatL2(dimension)  # Base quantizer (is used to assign vectors to clusters during training)
    index = faiss.IndexIVFFlat(quantizer, dimension, n_clusters)
    index.train(embeddings)  # IVF indexes must be trained before adding vectors
    index.add(embeddings)

    # 2. Search for the k nearest neighbors
    k = 2
    distances, indices = index.search(query_embedding, k)

    print("Nearest neighbors:")
    for i, idx in enumerate(indices[0]):
        print(f" Index: {idx}, Distance: {distances[0][i]}, Sentence: {sentences[idx]}")
    ```
