# Character Tokens {Output}

## Description

This is another method that can deal successfully with new words because it has the raw letters to fall back on.
While that makes the representation easier to tokenize, it makes the modeling more difficult.
Where a model with subword tokenization can represent `play` as one token, a model using character-level tokens needs to model the information to spell out `p-l-a-y` in addition to modeling the rest of the sequence.
Subword tokens present an advantage over character tokens in the ability to fit more text within the limited context length of a Transformer model.
So with a model with a context length of 1,024, you may be able to fit about three times as much text using subword tokenization than using character tokens.

## Example

Input: `Have the 🎵 bards who preceded`

Output: `H`, `a`, `v`, `e`, `<space>`, `t`, `h`, `e`, `<space>`, `🎵`, `<space>`, ...
