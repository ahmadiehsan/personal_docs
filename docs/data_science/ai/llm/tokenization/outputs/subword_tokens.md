# Subword Tokens

## Description

As the Word Token technique has a large vocabulary that has a lot of tokens with minimal differences between them (e.g., `apology`, `apologize`, `apologetic`, `apologist`) this challenge is resolved by subword tokenization as it has a token for apolog, and then suffix tokens (e.g., `-y`, `-ize`, `-etic`, `-ist`) that are common with many other tokens, resulting in a more expressive vocabulary.

This method contains full and partial words. In addition to the vocabulary expressivity mentioned earlier, another benefit of the approach is its ability to represent new words by breaking down the new token into smaller characters, which tend to be a part of the vocabulary.

Subword tokens often average three characters per token.

## Example

Input: `Have the 🎵 bards who preceded`

Output: `Have`, `the`, `🎵`, `bard`, `s`, `who`, `preced`, `ed`
