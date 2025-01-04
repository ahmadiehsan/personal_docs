# VADER [Sentiment Analysis]

## Description

VADER (alence Aware Dictionary for sEntiment Reasoning) is a model used for text sentiment analysis that is sensitive to both polarity (positive/negative) and intensity (strength) of emotion.

Primarily, VADER sentiment analysis relies on a dictionary which maps lexical features to emotion intensities called sentiment scores.

The sentiment score of a text can be obtained by summing up the intensity of each word in the text, for example:

- Words like "love", "like" "enjoy", "happy" all convey a positive sentiment.
- VADER is intelligent enough to understand the basic context of these words, such as "did not love" as a negative sentiment.
- It also understands capitalization and punctuation, such as LOVE!!!"

Sentiment Analysis on raw text is always challenging however, due to a variety of possible factors:

- Positive and Negative sentiment in the same text data.
- Sarcasm using positive words in a negative way.
