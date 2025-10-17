# Semantic Similarity [Augmentation]

## Description

By comparing the **sentence embeddings** of the original and augmented texts, we can ensure semantic similarity.

## Example

```python
def semantic_similarity(original, augmented):
    original_embedding = model.encode(original)
    augmented_embedding = model.encode(augmented)
    similarity = cosine_similarity([original_embedding], [augmented_embedding])[0][0]
    return similarity

def filter_by_semantic_similarity(original, augmented_list, threshold=0.8):
    return [
        a for a in augmented_list
        if semantic_similarity(original, a) >= threshold
    ]
```
