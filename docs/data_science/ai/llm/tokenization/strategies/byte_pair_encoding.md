# Byte Pair Encoding (BPE)

## Description

Byte Pair Encoding (BPE) is a Subword tokenization algorithm commonly used in natural language processing (NLP). It was originally designed for data compression but has since been adapted to tokenize text for tasks such as machine translation, language modeling, and more. BPE addresses the problem of word representation by splitting words into subword units, which can handle rare words and out-of-vocabulary (OOV) terms efficiently.

- Efficiently handles rare and OOV words by breaking them into subword units.
- Generates a compact vocabulary by balancing whole words and subwords.
- Easy to implement and widely used in NLP systems like OpenNMT and GPT models.
- Does not handle contextual dependencies as it operates purely on frequency.
- Fixed merges may lead to inefficiencies for some languages with complex morphology.
- BPE remains a popular tokenization method due to its simplicity and adaptability for many NLP tasks.

## Workflow

1. **Initialization**:

   - Start with a vocabulary containing all the unique characters of the dataset.
   - Treat each word as a sequence of characters.

2. **Frequency calculation**: Identify the most frequent pair of adjacent characters (or subwords) in the text.
3. **Merge**:

   - Merge the most frequent character pair into a new subword token.
   - Add the new subword token to the vocabulary.

4. **Repeat**: Continue the process of finding and merging the most frequent character pairs until the vocabulary reaches the desired size.
5. **Encoding**: Words are encoded as sequences of subwords from the final vocabulary.

## Example

Given the words in the dataset `low`, `lower`, and `newest`:

1. Start with the characters: `l, o, w, e, r, n, w, s, t`.
2. Compute frequencies of adjacent pairs (e.g., `l + o`, `o + w`, etc.).
3. Iteratively merge the most frequent pairs:

   - Merge `l + o = lo`
   - Merge `lo + w = low`
   - Merge `e + r = er`
   - Continue until reaching the desired vocabulary size.
