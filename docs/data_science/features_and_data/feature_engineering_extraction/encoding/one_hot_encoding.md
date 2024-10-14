# One-Hot Encoding

## Specifications

- **Good for:** Low number of values

## Description

Considering we have the numeric representation of any categorical attribute with m labels (after transformation), the one-hot encoding scheme encodes or transforms the attribute into m binary features which can only contain a value of 1 or 0. Each observation in the categorical feature is thus converted into a vector of size m with only one of the values as 1 (indicating it as active).

<img src="image4.jpg" style="width:2.66822in" />

## Example

```python
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# transform and map pokemon generations
gen_le = LabelEncoder()
gen_labels = gen_le.fit_transform(poke_df['Generation'])
poke_df['Gen_Label'] = gen_labels

# encode generation labels using one-hot encoding scheme
gen_ohe = OneHotEncoder()
gen_feature_arr = gen_ohe.fit_transform(poke_df[['Gen_Label']]).toarray()

gen_feature_labels = list(gen_le.classes_)
gen_features = pd.DataFrame(gen_feature_arr, columns=gen_feature_labels)

poke_df_ohe = pd.concat([poke_df_sub, gen_features, leg_features], axis=1)
columns = sum([
    ['Name', 'Generation', 'Gen_Label'],
    gen_feature_labels,
    ['Legendary', 'Lgnd_Label'],
    leg_feature_labels
], [])
```
