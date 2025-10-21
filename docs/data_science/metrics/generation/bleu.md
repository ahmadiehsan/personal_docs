# BLEU [NLP]

## Description

Bilingual Evaluation Understudy (BLEU) is an automated metric that evaluates the quality of machine-translated text by measuring its similarity to one or more high-quality human reference translations.
It works by comparing sequences of words (n-grams) in the machine output against the reference texts, producing a score between 0 and 1, where higher values indicate a closer match.

!!! info

    BLEU is widely used due to its low cost and correlation with human judgment, though it does not consider grammatical correctness or semantics.

Strengths:

- **Widely adopted**: It is a standard and popular metric in the field of machine translation.
- **Automated and inexpensive**: It provides a fast, automated way to evaluate translation quality without human review for every sentence.
- **High correlation**: It correlates well with human judgment of quality on average, especially over a large number of sentences.

Limitations:

- **Ignores semantics**: BLEU does not consider the meaning of the text, focusing only on word overlap. A translation could have a high score but be semantically incorrect.
- **Grammatical errors**: It does not explicitly penalize grammatical errors.
- **Tokenization dependency**: Early versions relied on specific tokenization methods, which could make it hard to compare models that used different tokenizers. Modern implementations often handle this better.

## Workflow

- **N-gram comparison**: The algorithm compares consecutive phrases, or n-grams, of the machine translation against the human references.
- **Precision**: It calculates the precision of these matches, which is the percentage of n-grams in the machine's output that are also found in the reference translations.
- **Corpus-level calculation**: BLEU averages the n-gram matches over an entire corpus of sentences to get a more stable score than evaluating individual sentences.
- **Brevity penalty**: A penalty is applied to machine translations that are too short compared to the reference translations, ensuring that a high score isn't achieved by being overly brief.
- **Score range**: The final score is a number between 0 and 1 (or 0% and 100%).

## Example

```python
from nltk.translate.bleu_score import sentence_bleu

candidate_translation = "the cat sat on the mat"
reference_translations = [
    "a cat is on the mat",
    "the cat is on the mat"
]

# Convert strings to lists of words
candidate = candidate_translation.split()
references = [ref.split() for ref in reference_translations]

score = sentence_bleu(references, candidate)
print(f"BLEU score with multiple references: {score:.3f}")
```
