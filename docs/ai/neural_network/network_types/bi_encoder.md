# Bi-Encoders (Dense Retrieval)

## Description

Dense retrieval systems rely on the concept of embeddings and turn the search problem into retrieving the nearest neighbors of the search query (after both the query and the documents are converted into embeddings).

The following picture shows how dense retrieval takes a search query, consults its archive of texts, and outputs a set of relevant results.

<img src="overview.png" style="width:4.5in" />

!!! info

    Although a bi-encoder is quite fast and creates accurate sentence representations, cross-encoders generally perform better than a bi-encoder but do not generate embeddings

## Architecture

Uses a Siamese architecture.
In this architecture, we have two identical BERT models that share the same weights and neural architecture.
These models are fed the sentences from which embeddings are generated through the pooling of token embeddings.
Then, models are optimized through the similarity of the sentence embeddings.
Since the weights are identical for both BERT models, we can use a single model and feed it the sentences one after the other.

<img src="architecture.png" style="width:3.5in" />

## Vs RAG

RAG is essentially Bi-Encoders (Dense Retrieval) + LLM where:

1. Bi-Encoders retrieve relevant documents (instead of just keyword search).
2. Instead of returning a list of docs, these are passed to an LLM.
3. The LLM generates a human-like response based on the retrieved docs.
