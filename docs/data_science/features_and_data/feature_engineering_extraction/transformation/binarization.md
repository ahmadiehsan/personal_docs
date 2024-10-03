# Binarization

## Specifications

- **Data Type:** Continuous numeric data

## Description

Often raw frequencies or counts may not be relevant for building a model based on the problem which is being solved. For instance if I’m building a recommendation system for song recommendations, I would just want to know if a person is interested or has listened to a particular song. This doesn’t require the number of times a song has been listened to since I am more concerned about the various songs he\\she has listened to. In this case, a binary feature is preferred as opposed to a count based feature.

## Example

With numpy

<img src="image1.jpg" style="width:4.8777in" />

With scikit-learn

<img src="image2.jpg" style="width:5.48228in" />
