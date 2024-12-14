# WordPiece

## Description

WordPiece is a Subword tokenization algorithm developed by Google and heavily used in models like BERT. It improves upon Byte Pair Encoding (BPE) by using a probabilistic approach to determine subword units, optimizing for better handling of morphologically rich or low-resource languages.

- Probabilistic merging accounts for more context than simple frequency-based approaches like BPE.
- Handles unseen or rare words more gracefully with subword units.
- Reduces vocabulary size while maintaining representation flexibility.
- Slightly more complex and computationally intensive compared to BPE.
- Training requires optimizing vocabulary for maximum likelihood, which can be time-consuming.
- WordPiece tokenization, used in models like BERT and ALBERT, is highly effective for a variety of NLP tasks.

## Workflow

1. **Initialization**: Start with a vocabulary of individual characters (e.g., `a, b, c, ...`) and a special token like `[UNK]` for unknown words.
2. **Corpus processing**: Split text into sequences based on the initial vocabulary.
3. **Scoring and merging**: Merge subword units iteratively based on their statistical likelihood in the training corpus. WordPiece maximizes the likelihood of the training data, given the subword vocabulary.
4. **Vocabulary capping**: Stop the process once the vocabulary size reaches a predefined limit.
5. **Encoding**: Tokenize new text into subwords present in the vocabulary. If a word cannot be directly matched, it is split into the longest subwords that exist in the vocabulary (`longest match first` principle).

## Example

Given the word `playing`:

1. Start with the characters: `p, l, a, y, i, n, g`.
2. Merge frequently occurring character pairs:

   - Merge `pl` to `pla`
   - Merge `pla + y = play`
   - Merge `play + ing = playing`

3. If `playing` is not in the vocabulary:

   - Encode as `play` + `##ing`. (Here, `##` denotes a continuation subword that cannot start a word.)
