# Text Generation With T5 [NLP] [Augmentation]

## Description

T5 aids data augmentation through:

- **Paraphrasing**: Rephrasing sentences while preserving meaning, e.g., "The movie was boring." becomes "The film was dull."
- **Synonym replacement**: Substituting words with synonyms to create variations, e.g., "The movie was long and tedious." becomes "The film was lengthy and boring."
- **Sentiment-based transformation**: Changing sentence sentiment, e.g., given a negative sentence such as "The movie was very disappointing." can generate a neutral or positive version, such as "The movie had a slow start but improved later."
- **Text expansion**: Adding context or details to short sentences, e.g., "The event was great." becomes "The event was great, with excellent speakers and engaging discussions."

## Example

```python
def t5_augmentation(text, model, tokenizer, num_return_sequences=1):
    input_ids = tokenizer.encode(
        f"paraphrase: {text}",
        return_tensors="pt",
        max_length=512,
        truncation=True,
    )
    outputs = model.generate(
        input_ids=input_ids,
        max_length=150,
        num_return_sequences=num_return_sequences,
        num_beams=5,
        no_repeat_ngram_size=2,  # Prevents repetition of 2-grams
        top_k=50,
        top_p=0.95,
    )
    return [tokenizer.decode(o, skip_special_tokens=True) for o in outputs]
```
