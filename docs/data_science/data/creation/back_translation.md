# Back-Translation [NLP] [Augmentation]

## Description

This method involves translating the text to another language and then back to the original language.
It's particularly effective for introducing natural variations in sentence structure and word choice.

## Example

```python
def back_translation(text, target_lang="fr"):
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)
    back_translated = translator.translate(translated.text, dest="en")
    return back_translated.text
```
