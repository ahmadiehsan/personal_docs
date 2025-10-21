# Cohen's Kappa [2 Annotators]

## Description

Cohen's Kappa is a statistical measure that evaluates inter-rater reliability between two annotators by comparing their observed agreement to what would be expected by chance, accounting for the possibility of random agreements and producing a score between -1 and 1, where 1 indicates perfect agreement, 0 indicates agreement equivalent to chance, and negative values indicate agreement less than chance.

## Example

```python
from sklearn.metrics import cohen_kappa_score

annotator1 = [0, 1, 2, 0, 1]
annotator2 = [0, 1, 1, 0, 1]

kappa = cohen_kappa_score(annotator1, annotator2)
print(kappa)  # 0.6666666666666667
```
