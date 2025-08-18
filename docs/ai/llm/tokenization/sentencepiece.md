# SentencePiece {Strategy}

## Description

SentencePiece is an unsupervised text tokenization tool that treats the input text as a raw stream of characters without requiring pre-tokenization.
Developed by Google, it is particularly well-suited for languages with no explicit word boundaries, such as Chinese, Japanese, and Thai.
SentencePiece is commonly used in Transformer-based models like T5 and XLM-R.

- Does not assume spaces signify word boundaries, allowing it to work across multiple languages seamlessly.
- Can train tokenization models using character-based approaches like BPE or unigram language models.
- Encodes text as subword units, including subword prefixes and suffixes when needed.
- Language-agnostic approach works well for multilingual models.
- Fully unsupervised, it learns tokenization rules directly from data without relying on pre-tokenized input.
- Flexible integration with BPE or Unigram-based models.
- May result in slightly less human-readable tokens (e.g., `▁` or unknown special tokens).
- Training can be more complex compared to simpler algorithms.
- SentencePiece is widely adopted in research and production settings for its robustness, flexibility, and effectiveness in multilingual and zero-shot NLP tasks.

## Workflow

1. **Training**:

   - Train a model on raw text input, either using BPE or unigram language models.
   - Identify subwords and optimization rules directly from data.

2. **Corpus Preparation**: Does not require language-specific preprocessing like punctuation removal or token splitting.
3. **Tokenization**:

   - Encode a sentence as subword sequences based on the trained model.
   - Generate special tokens (e.g., `<unk>`, `<pad>`, etc.) as needed.

4. **Inference**: Apply the trained tokenization model to new text.

## Example

Input text: `this is a test`.

Tokenization with SentencePiece might produce: `▁this ▁is ▁a ▁test`

Here, the `▁` denotes a space, allowing the model to encode spaces as part of the tokenization schema.
