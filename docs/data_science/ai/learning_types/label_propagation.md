# Label Propagation [Semi-Sup]

## Description

Label propagation is a graph-based semi-supervised learning algorithm. It builds a graph using both labeled and unlabeled data points, with each data point represented as a node and edges representing the similarity between nodes. The algorithm works by propagating the labels from the labeled nodes to the unlabeled nodes based on their similarity.

The key idea is that similar data points should have similar labels. The algorithm begins by assigning initial label probabilities to the unlabeled nodes, typically based on their similarity to labeled nodes. Then, an iterative process propagates these probabilities throughout the graph until convergence. The final label probabilities are used to classify the unlabeled data points.

## Example

To apply semi-supervised learning in a specific domain, let's consider a medical domain where we want to classify scientific articles into different categories such as cardiology, neurology, and oncology. Suppose we have a small set of labeled articles and a large set of unlabeled articles.

A possible approach could be to use label propagation by creating a graph of articles where the nodes represent the articles and the edges represent the similarity between the articles. The similarity could be based on various factors, such as the words used, the topics covered, or the citation networks between the articles. After propagating the labels, we can classify the unlabeled articles based on the final label probabilities.
