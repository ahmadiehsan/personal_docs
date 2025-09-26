# Augmentation

## Description

Is a method that we can use to artificially expand the training data size by applying transformations, such as rotation, scaling, and flipping, to the existing dataset, which helps us to extend our training data.
This strategy aids in mitigating overfitting by offering the model a more diverse set of examples to learn from.

<img src="image3.png" style="width:4.64746in" />

<img src="image2.png" style="width:4.74969in" />

<img src="image1.png" style="width:4.62584in" />

!!! info

    <span dir="rtl">نکته خیلی مهم تو این تکنیک اینه که نباید به شکل رندم فقط دیتاهای فیک جنریت کرد، باید توجه کنیم که تو تست دیتا ست چه مدل ناهنجاری هایی وجود داره، سعی کنیم اون هارو بسط بدیم به ترینینگ دیتا ست و فیک دیتا های جدید و با هدف تولید کنیم.</span>

## Varieties

=== "Back-Translation"

    Back-Translation involves translating the text to another language and then back to the original language.
    It's particularly effective for introducing natural variations in sentence structure and word choice.

=== "Synonym Replacement"

    Synonym Replacement involves replacing words in the original text with their synonyms.
    We can use **WordNet**, a lexical database for the English language, to find synonyms.

=== "T5"

    Text Generation With T5 aids data augmentation through:

    - **Paraphrasing**: Rephrasing sentences while preserving meaning, e.g., "The movie was boring." becomes "The film was dull."
    - **Synonym replacement**: Substituting words with synonyms to create variations, e.g., "The movie was long and tedious." becomes "The film was lengthy and boring."
    - **Sentiment-based transformation**: Changing sentence sentiment, e.g., given a negative sentence such as "The movie was very disappointing." can generate a neutral or positive version, such as "The movie had a slow start but improved later."
    - **Text expansion**: Adding context or details to short sentences, e.g., "The event was great." becomes "The event was great, with excellent speakers and engaging discussions."

## Example

=== "Back-Translation"

    ```python
    def back_translation(text, target_lang="fr"):
        translator = Translator()
        translated = translator.translate(text, dest=target_lang)
        back_translated = translator.translate(translated.text, dest="en")
        return back_translated.text
    ```

=== "Synonym Replacement"

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

=== "T5"

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
