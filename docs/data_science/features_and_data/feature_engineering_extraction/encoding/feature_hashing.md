# Feature Hashing

## Specifications

- **Good for:** Large number of values

## Description

The feature hashing scheme is another useful feature engineering scheme for dealing with large scale categorical features. In this scheme, a hash function is typically used with the number of encoded features pre-set (as a vector of predefined length) such that the hashed values of the features are used as indices in this predefined vector and values are updated accordingly. Since a hash function maps a large number of values into a small finite set of values, multiple different values might create the same hash which is termed as collisions. Typically, a signed hash function is used so that the sign of the value obtained from the hash is used as the sign of the value which is stored in the final feature vector at the appropriate index. This should ensure lesser collisions and lesser accumulation of error due to collisions.

Hashing schemes work on strings, numbers and other structures like vectors. **You can think of hashed outputs as a finite set of b bins such that when the hash function is applied on the same values\\categories, they get assigned to the same bin (or subset of bins) out of the b bins based on the hash value.** We can pre-define the value of b which becomes the final size of the encoded feature vector for each categorical attribute that we encode using the feature hashing scheme.

Thus even if we have over 1000 distinct categories in a feature and we set b=10 as the final feature vector size, the output feature set will still have only 10 features as compared to 1000 binary features if we used a one-hot encoding scheme.

## Example

We will now use a feature hashing scheme by leveraging scikit-learn’s FeatureHasher class, which uses a signed 32-bit version of the Murmurhash3 hash function. We will pre-define the final feature vector size to be 6 in this case.

```python
from sklearn.feature_extraction import FeatureHasher

fh = FeatureHasher(n_features=6, input_type='string')
hashed_features = fh.fit_transform(vg_df['Genre'])
hashed_features = hashed_features.toarray()
pd.concat([vg_df[['Name', 'Genre']], pd.DataFrame(hashed_features)], axis=1).iloc[1:7]
```
