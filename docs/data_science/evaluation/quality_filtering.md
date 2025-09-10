# Quality Filtering [NLP] [Augmentation]

## Description

We can implement quality checks to filter out low-quality augmented samples.

## Example

```python
def quality_filter(
    augmented_texts,
    original_text,
    similarity_threshold=0.8,
    perplexity_threshold=100
):
    filtered_texts = []

    for candidate_text in augmented_texts:
        similarity_score = semantic_similarity(original_text, candidate_text)
        perplexity_score = calculate_perplexity(candidate_text)

        if similarity_score >= similarity_threshold and perplexity_score <= perplexity_threshold:
            filtered_texts.append(candidate_text)

    return filtered_texts
```
