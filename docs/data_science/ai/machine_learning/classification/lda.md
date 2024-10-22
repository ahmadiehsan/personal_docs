# LDA [NLP: Topic Modeling] [Unsup]

## Description

Latent Dirichlet Allocation (LDA) is a generative statistical model used in NLP and machine learning to uncover the underlying topics in a collection of documents. It helps if we have **unlabeled data**, we can attempt to "discover" labels.

## Assumptions of LDA

- Documents with similar topics use similar groups of words
- Latent topics can then be found by searching for groups of words that frequently occur together in documents across the corpus
- Documents are probability distributions over latent topics

  <img src="image2.jpg" style="width:2.75006in" />

  <img src="image1.jpg" style="width:2.74655in" />

- Topics themselves are probability distributions over words

  <img src="image3.jpg" style="width:3.49953in" />

- LDA represents documents as mixtures of topics that spit out words with certain probabilities

## How It Works

- **Initial Assignment:** Randomly assign each word in each document to a topic
- This random assignment already gives you both topic representations of all the documents and word distributions of all the topics (note: these initial random topics won't make sense)
- Iterative refinement:

   - For each word in each document, compute the probability of each topic given the current state of topic assignments
   - Reassign the word to a new topic based on these probabilities, considering:

      - How prevalent the word is in each topic across the entire corpus.
      - How prevalent the topic is in the current document

- This process leverages the dependencies and co-occurrences in the data, gradually improving the topic assignments and leading to a coherent topic structure
- At the end we have each document assigned to a topic
- We also can search for the words that have the highest probability of being assigned to a topic
- For example, most common words (highest probability) for topic \#4 is: cat, vet, birds, dog ... food, home
- It is up to the user to interpret these topics and assign a meaningful name to them

## Example

Suppose we have a collection of three documents:

- Document 1: "I love playing football with my friends."
- Document 2: "The football match was intense and exciting."
- Document 3: "My new laptop has an amazing battery life and performance."

We want to discover two topics (K = 2) in this document collection.

After the algorithm converges or reaches the maximum number of iterations, we can interpret the discovered topics by looking at the most probable words for each topic and the most probable topics for each document.

For our example, LDA might discover the following topics:

- Topic 1: {"football", "playing", "friends", "match", "intense", "exciting"}
- Topic 2: {"laptop", "battery", "life", "performance"}

With these topics, the document-topic distribution (θ) might look like this:

- ​​θ​ 1 = \[0.9, 0.1\] (Document 1 is 90% about Topic 1 and 10% about Topic 2)
- ​​θ​ 2 = \[0.8, 0.2\] (Document 2 is 80% about Topic 1 and 20% about Topic 2)
- ​​θ​ 3 = \[0.1, 0.9\] (Document 3 is 10% about Topic 1 and 90% about Topic 2)

In this example, topic 1 seems to be related to football and sports, while topic 2 seems to be related to technology and gadgets
