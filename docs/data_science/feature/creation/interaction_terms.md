# Interaction Terms

## Description

In feature construction, interaction terms refer to creating new features by combining two or more existing features in a dataset through multiplication, division, or other mathematical operations.
These new features capture the interaction or relationship between the original features, and they can help improve the accuracy of machine learning models.

When creating interaction terms, it is important to consider which features to combine and how to combine them.
Here are some common techniques:

- **Domain knowledge**: Use domain knowledge or expert intuition to identify which features are likely to interact and how they might interact.
- **Pairwise combinations**: Create interaction terms by pairwise combining all pairs of features in the dataset. This can be computationally expensive, but it can help identify potential interaction effects.
- **PCA**: Use PCA to identify the most important combinations of features, and create interaction terms based on these combinations.

## Example

For example, in a dataset of real estate prices, you might have features such as the number of bedrooms, the number of bathrooms, and the square footage of the property.
By themselves, these features provide some information about the price of the property, but they do not capture any interaction effects between the features.
However, by creating an interaction term between the number of bedrooms and the square footage, you can capture the idea that larger properties with more bedrooms tend to be more expensive than smaller ones with the same number of bedrooms.

---

```python
from sklearn.preprocessing import PolynomialFeatures

pf = PolynomialFeatures(degree=2, interaction_only=False, include_bias=False)
res = pf.fit_transform(atk_def)
intr_features = pd.DataFrame(
    res,
    columns=['Attack', 'Defense', 'Attack^2', 'Attack x Defense', 'Defense^2']
)
intr_features.head(5)
```
