# Word Error Rate (WER) [STT]

## Description

Is a common metric of the performance of a **speech recognition** or **machine translation** system.

The WER metric typically ranges from 0 to 1, where 0 indicates that the compared pieces of text are exactly identical, and 1 (or larger) indicates that they are completely different with no similarity.
This way, a WER of 0.8 means that there is an 80% error rate for compared sentences.

## Formula

$$
WER = \frac{S + D + I}{N}
$$

- $S$ = number of substitutions
- $D$ = number of deletions
- $I$ = number of insertions
- $N$ = number of words in the reference (ground truth)

## Example

```python
from jiwer import wer

reference = "the quick brown fox jumps over the lazy dog"
hypothesis = "the quick brown fox jump over lazy dog"

error_rate = wer(reference, hypothesis)
print(f"WER: {error_rate:.2f}")  # WER: 0.22
```
