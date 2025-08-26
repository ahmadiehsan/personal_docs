# Byte Tokens [Output]

## Description

This method breaks down tokens into the individual bytes that are used to represent unicode characters.

!!! info

    Some Subword tokenizers also include bytes as tokens in their vocabulary as the final building block to fall back to when they encounter characters they can't otherwise represent. The GPT-2 and RoBERTa tokenizers do this, for example.

## Example

Input: `Have the 🎵 bards who preceded`

Output: `1001000`, `1100001`, `1110110`, `1100101`, `0100000`, `1110100`, `1101000`, ...
