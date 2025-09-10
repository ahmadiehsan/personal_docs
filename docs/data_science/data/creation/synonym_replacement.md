# Synonym Replacement [NLP] [Augmentation]

## Description

This technique involves replacing words in the original text with their synonyms.
We can use **WordNet**, a lexical database for the English language, to find synonyms:

## Example

```python
def synonym_replacement(text, n=1):
    words = text.split()
    new_words = words.copy()
    random_word_list = list(set([w for w in words if w.isalnum()]))
    random.shuffle(random_word_list)
    num_replaced = 0

    for random_word in random_word_list:
        synonyms = get_synonyms(random_word)
        if len(synonyms) >= 1:
            synonym = random.choice(list(synonyms))
            new_words = [synonym if w == random_word else w for w in new_words]
            num_replaced += 1

        if num_replaced >= n:
            break

    return " ".join(new_words)
```
