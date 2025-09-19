# Transforming Nominal Attributes [Encoding]

## Description

Nominal attributes consist of discrete categorical values with no notion or sense of order amongst them.

The idea here is to transform these attributes into a more representative numerical format that can be easily understood by downstream code and pipelines.

Movie, music, and video game genres, country names, food, and cuisine types are examples of nominal categorical attributes.

## Example

```python
from sklearn.preprocessing import LabelEncoder

gle = LabelEncoder()
genre_labels = gle.fit_transform(vg_df["Genre"])
```
