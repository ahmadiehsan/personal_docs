# Rounding

## Specifications

- **Data Type**: Continuous numeric data

## Description

Often when dealing with continuous numeric attributes like proportions or percentages, we may not need the raw values to have a high amount of precision.
Hence it often makes sense to round off these high-precision percentages into numeric integers.
These integers can then be directly used as raw values or even as categorical (discrete-class-based) features.
Let's try applying this concept in a dummy dataset depicting store items and their popularity percentages.

## Example

```python
items_popularity = pd.read_csv("datasets/item_popularity.csv", encoding="utf-8")

items_popularity["popularity_scale_10"] = np.array(
    np.round((items_popularity["pop_percent"] * 10)),
    dtype="int"
)

items_popularity["popularity_scale_100"] = np.array(
    np.round((items_popularity["pop_percent"] * 100)),
    dtype="int"
)

items_popularity
```

We tried two forms of rounding.
The features depict the item popularities now both on a scale of 1–10 and on a scale of 1–100.
You can use these values both as numerical or categorical features based on the scenario and problem.
