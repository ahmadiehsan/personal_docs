# Word Tokens

## Description

This approach was common with earlier methods like word2vec but is being used less and less in NLP. Its usefulness, however, led it to be used outside of NLP for use cases such as recommendation systems, as we'll see later in the chapter.

One challenge with word tokenization is that the tokenizer may be unable to deal with new words that enter the dataset after the tokenizer was trained. This also results in a vocabulary that has a lot of tokens with minimal differences between them (e.g., `apology`, `apologize`, `apologetic`, `apologist`).

## Example

Input: `Have the 🎵 bards who preceded`

Output: `Have`, `the`, `🎵`, `bards`, `who`, `preceded`
