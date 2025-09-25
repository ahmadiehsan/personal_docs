# Duplicates {LSH} {Shingling}

## Description

Eliminating duplicate records is a common preprocessing step to ensure data quality and reliable analysis.

## Techniques

=== "Exact Match Deduplication"

    Removes records that are identical. This is the simplest form of deduplication.

=== "Near-Duplicate Detection"

    Identifies records that are not exactly the same but are highly similar, often using text similarity measures or fuzzy matching algorithms.
    Useful for catching duplicates with minor differences.

    ```text
    Scenario: You have a collection of news articles:

    Data:
    - Article 1: "The company reported a significant increase in quarterly profits."
    - Article 2: "Quarterly profits saw a large increase, the company reports."

    Result: A near-duplicate detection algorithm determines that these articles are highly similar in content, even though the wording is slightly different. One of the articles is removed, based on a similarity threshold.
    ```

=== "Shingling"

    Breaks text into overlapping sequences (shingles) to represent documents. The sets of shingles are compared to measure similarity and detect near-duplicates in text data.

    ```text
    Scenario: You want to compare the similarity of text documents:

    Data:
    - Document 1: "The quick brown fox jumps over the lazy dog."
    - k=3 word shingle.

    Result: The shingles generated are as follows:
    - "The quick brown"
    - "quick brown fox"
    - "brown fox jumps"
    - "fox jumps over"
    - "jumps over the"
    - "over the lazy"
    - "the lazy dog"

    The document is then represented by the set of those shingles. Then another document could be turned into shingles, and the sets of shingles can be compared.
    ```

=== "Locality Sensitive Hashing (LSH)"

    Uses special hash functions to group similar records into buckets, so only records within the same bucket are compared in detail. This technique is efficient for large datasets and scalable near-duplicate detection.

    ```python
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    def deduplicate_corpus(corpus, similarity_threshold=0.9):
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(corpus)
        similarity_matrix = cosine_similarity(tfidf_matrix)

        duplicates = set()
        for i in range(len(corpus)):
            for j in range(i + 1, len(corpus)):
                if similarity_matrix[i, j] > similarity_threshold:
                    duplicates.add(j)

        deduplicated_corpus = [doc for i, doc in enumerate(corpus) if i not in duplicates]
        return deduplicated_corpus
    ```
