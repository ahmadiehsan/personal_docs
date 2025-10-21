# Fleiss' Kappa [+3 Annotators]

## Description

Fleiss' kappa is a statistical measure that **assesses the reliability of agreement among a fixed number of raters who classify items into a set of categories**.

It is a chance-corrected measure, meaning it accounts for agreement that would occur simply by random chance.
The value ranges from -1 to +1, where +1 is perfect agreement, 0 is agreement no better than chance, and negative values indicate worse-than-chance agreement.

Key features:

- **Number of raters**: Fleiss' kappa is used when there are three or more raters. For two raters, Cohen's kappa is more appropriate.
- **Data type**: It is used for categorical (nominal) data. If the data is ordinal, other measures like Kendall's W or Krippendorff's alpha may be better suited.
- **Application**: It measures inter-rater reliability, or how consistently different raters classify the same set of items. It can also be used for intra-rater reliability if the same rater measures items at different times.

!!! warning

    Some studies have identified that Fleiss' kappa can be affected by a paradoxical behavior where it yields very low values even with high agreement, depending on the specific category assignments.

## Example

```python
import numpy as np
from statsmodels.stats.inter_rater import fleiss_kappa

# Example data: 10 subjects, 3 categories, 3 raters for each subject
# The values in the matrix represent the number of raters who assigned the subject to that category.
# Each row must sum to the number of raters (3 in this case).
ratings = np.array([
    [3, 0, 0],  # Subject 1: All 3 raters agree on category 1
    [1, 2, 0],  # Subject 2: 1 rater for cat 1, 2 for cat 2
    [0, 3, 0],  # Subject 3: All 3 raters agree on category 2
    [0, 1, 2],  # Subject 4: 1 rater for cat 2, 2 for cat 3
    [1, 1, 1],  # Subject 5: Each rater chose a different category
    [3, 0, 0],
    [0, 0, 3],
    [1, 0, 2],
    [2, 1, 0],
    [1, 1, 1]
])

kappa = fleiss_kappa(ratings, method="fleiss")
print(kappa)  # 0.2571428571428571
```
