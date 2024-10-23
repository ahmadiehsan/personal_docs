# Binarization

## Specifications

- **Data Type:** Continuous numeric data

## Description

Often raw frequencies or counts may not be relevant for building a model based on the problem which is being solved. For instance if I'm building a recommendation system for song recommendations, I would just want to know if a person is interested or has listened to a particular song. This doesn't require the number of times a song has been listened to since I am more concerned about the various songs he\\she has listened to. In this case, a binary feature is preferred as opposed to a count based feature.

## Example

With numpy:

```python
watched = np.array(popsong_df['listen_count'])
watched[watched >= 1] = 1
popsong_df['watched'] = watched
```

With scikit-learn:

```python
from sklearn.preprocessing import Binarizer

bn = Binarizer(threshold=0.9)
pd_watched = bn.transform([popsong_df['listen_count']])[0]
popsong_df['pd_watched'] = pd_watched
popsong_df.head(11)
```
