# Subword Tokens {WordPiece} {BPE} {SentencePiece}

## Description

As the Word Token technique has a large vocabulary that has a lot of tokens with minimal differences between them (e.g., `apology`, `apologize`, `apologetic`, `apologist`) this challenge is resolved by subword tokenization as it has a token for apolog, and then suffix tokens (e.g., `-y`, `-ize`, `-etic`, `-ist`) that are common with many other tokens, resulting in a more expressive vocabulary.

This method contains full and partial words.
In addition to the vocabulary expressivity mentioned earlier, another benefit of the approach is its ability to represent new words by breaking down the new token into smaller characters, which tend to be a part of the vocabulary.

Input: `Have the 🎵 bards who preceded`

Output: `Have`, `the`, `🎵`, `bard`, `s`, `who`, `preced`, `ed`

!!! info

    Subword tokens often average three characters per token.

## Varieties

=== "WordPiece"

    WordPiece is a Subword tokenization algorithm **developed by Google** and heavily **used in models like BERT**.
    It improves upon Byte Pair Encoding (BPE) by using a probabilistic approach to determine subword units, optimizing for better handling of morphologically rich or low-resource languages.

    - Probabilistic merging accounts for more context than simple frequency-based approaches like BPE.
    - Handles unseen or rare words more gracefully with subword units.
    - Reduces vocabulary size while maintaining representation flexibility.
    - Slightly more complex and computationally intensive compared to BPE.
    - Training requires optimizing vocabulary for maximum likelihood, which can be time-consuming.
    - WordPiece tokenization, used in models like BERT and ALBERT, is highly effective for a variety of NLP tasks.

=== "BPE"

    Byte Pair Encoding (BPE) is a Subword tokenization algorithm commonly used in natural language processing (NLP).
    It was originally designed for data compression but has since been adapted to tokenize text for tasks such as machine translation, language modeling, and more.
    BPE addresses the problem of word representation by splitting words into subword units, which can handle rare words and out-of-vocabulary (OOV) terms efficiently.

    - Efficiently handles rare and OOV words by breaking them into subword units.
    - Generates a compact vocabulary by balancing whole words and subwords.
    - Easy to implement and widely used in NLP systems like OpenNMT and GPT models.
    - Does not handle contextual dependencies as it operates purely on frequency.
    - Fixed merges may lead to inefficiencies for some languages with complex morphology.
    - BPE remains a popular tokenization method due to its simplicity and adaptability for many NLP tasks.

=== "SentencePiece"

    SentencePiece is an unsupervised text tokenization tool that treats the input text as a raw stream of characters without requiring pre-tokenization.
    **Developed by Google**, it is particularly **well-suited for languages with no explicit word boundaries, such as Chinese, Japanese, and Thai**.
    SentencePiece is commonly used in Transformer-based models like **T5** and **XLM-R**.

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

=== "WordPiece"

    1. **Initialization**: Start with a vocabulary of individual characters (e.g., `a, b, c, ...`) and a special token like `[UNK]` for unknown words.
    2. **Corpus processing**: Split text into sequences based on the initial vocabulary.
    3. **Scoring and merging**: Merge subword units iteratively based on their statistical likelihood in the training corpus. WordPiece maximizes the likelihood of the training data, given the subword vocabulary.
    4. **Vocabulary capping**: Stop the process once the vocabulary size reaches a predefined limit.
    5. **Encoding**: Tokenize new text into subwords present in the vocabulary. If a word cannot be directly matched, it is split into the longest subwords that exist in the vocabulary (`longest match first` principle).

=== "BPE"

    1. **Initialization**:

       - Start with a vocabulary containing all the unique characters of the dataset.
       - Treat each word as a sequence of characters.

    2. **Frequency calculation**: Identify the most frequent pair of adjacent characters (or subwords) in the text.
    3. **Merge**:

       - Merge the most frequent character pair into a new subword token.
       - Add the new subword token to the vocabulary.

    4. **Repeat**: Continue the process of finding and merging the most frequent character pairs until the vocabulary reaches the desired size.
    5. **Encoding**: Words are encoded as sequences of subwords from the final vocabulary.

=== "SentencePiece"

    1. **Training**:

       - Train a model on raw text input, either using BPE or unigram language models.
       - Identify subwords and optimization rules directly from data.

    2. **Corpus Preparation**: Does not require language-specific preprocessing like punctuation removal or token splitting.
    3. **Tokenization**:

       - Encode a sentence as subword sequences based on the trained model.
       - Generate special tokens (e.g., `<unk>`, `<pad>`, etc.) as needed.

    4. **Inference**: Apply the trained tokenization model to new text.

## Example

=== "WordPiece"

    Given the word `playing`:

    1. Start with the characters: `p, l, a, y, i, n, g`.
    2. Merge frequently occurring character pairs:

       - Merge `pl` to `pla`
       - Merge `pla + y = play`
       - Merge `play + ing = playing`

    3. If `playing` is not in the vocabulary:

       - Encode as `play` + `##ing`. (Here, `##` denotes a continuation subword that cannot start a word.)

=== "BPE"

    Given the words in the dataset `low`, `lower`, and `newest`:

    1. Start with the characters: `l, o, w, e, r, n, w, s, t`.
    2. Compute frequencies of adjacent pairs (e.g., `l + o`, `o + w`, etc.).
    3. Iteratively merge the most frequent pairs:

       - Merge `l + o = lo`
       - Merge `lo + w = low`
       - Merge `e + r = er`
       - Continue until reaching the desired vocabulary size.

=== "SentencePiece"

    Input text: `this is a test`.

    Tokenization with SentencePiece might produce: `▁this ▁is ▁a ▁test`

    Here, the `▁` denotes a space, allowing the model to encode spaces as part of the tokenization schema.
