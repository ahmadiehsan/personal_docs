# Effect Coding [Encoding]

## Specifications

- **Good for**: Low number of values

## Description

The effect coding scheme is actually very similar to the dummy coding scheme, except during the encoding process, the encoded features or feature vector, for the category values which represent all 0 in the dummy coding scheme, is replaced by -1 in the effect coding scheme.

## Example

```python
gen_onehot_features = pd.get_dummies(poke_df["Generation"])
gen_effect_features = gen_onehot_features.iloc[:, :-1]
gen_effect_features.loc[np.all(gen_effect_features == 0, axis=1)] = -1.

pd.concat([poke_df[["Name", "Generation"]], gen_effect_features], axis=1).iloc[4:10]
```
