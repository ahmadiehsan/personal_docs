# ROUGE [NLP]

## Description

Recall-Oriented Understudy for Gisting Evaluation (ROUGE) is a set of metrics used for evaluating automatic summarization and machine translation.
It works by comparing a machine-generated text (the candidate) against one or more human-created reference texts.

The primary ROUGE scores include:

- **ROUGE-N**: Measures the overlap of n-grams (sequences of N words) between the candidate and reference texts.

    - **ROUGE-1** considers the overlap of unigrams (single words).
    - **ROUGE-2** considers the overlap of bigrams (pairs of adjacent words).

- **ROUGE-L**: Is based on the Longest Common Subsequence (LCS). It measures the longest sequence of words that appears in both the candidate and reference texts in the same order, though not necessarily contiguously.

These metrics provide a way to quantify the quality of a generated text by measuring how much of the information from the reference texts is captured.
The scores are typically reported as precision, recall, and F1-score.
As the name suggests, ROUGE is recall-oriented, meaning it primarily measures how many of the n-grams from the reference text are found in the candidate text.

## Example

=== "Translation"

    ```python
    from rouge_score import rouge_scorer

    candidate_translation = "the cat sat on the mat"
    reference_translation = "a cat is on the mat"

    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference_translation, candidate_translation)

    print(f"ROUGE-1: {scores['rouge1'].fmeasure:.3f}")
    print(f"ROUGE-2: {scores['rouge2'].fmeasure:.3f}")
    print(f"ROUGE-L: {scores['rougeL'].fmeasure:.3f}")
    ```

=== "RAG"

    ```python
    from rouge_score import rouge_scorer

    query = "What is the capital of France?"
    answer = "The capital of France is Paris."
    retrieved_documents = [
        "Paris is the capital city of France.",
        "France is a country in Europe.",
        "The Eiffel Tower is a famous landmark in Paris.",
        "London is the capital of the United Kingdom."
    ]

    def calculate_rouge_scores(answer, documents):
        scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
        scores = []
        for doc in documents:
            score = scorer.score(answer, doc)
            scores.append(score)
        return scores

    rouge_scores = calculate_rouge_scores(answer, retrieved_documents)

    for i, score in enumerate(rouge_scores):
        print(f"Document {i+1}:")
        print(f" ROUGE-1: {score['rouge1'].fmeasure:.3f}")
        print(f" ROUGE-2: {score['rouge2'].fmeasure:.3f}")
        print(f" ROUGE-L: {score['rougeL'].fmeasure:.3f}")

    avg_rouge1 = sum([score['rouge1'].fmeasure for score in rouge_scores]) / len(rouge_scores)
    avg_rouge2 = sum([score['rouge2'].fmeasure for score in rouge_scores]) / len(rouge_scores)
    avg_rougeL = sum([score['rougeL'].fmeasure for score in rouge_scores]) / len(rouge_scores)

    print(f"\nAverage ROUGE Scores:")
    print(f" Average ROUGE-1: {avg_rouge1:.3f}")
    print(f" Average ROUGE-2: {avg_rouge2:.3f}")
    print(f" Average ROUGE-L: {avg_rougeL:.3f}")
    ```
