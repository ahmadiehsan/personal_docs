# FastText [NLP: Embedding] [Unsup]

## Description

The working logic of the FastText algorithm is similar to **Word2Vec**, but the biggest difference is that it also uses **N-grams** of words during training. While this increases the size and processing time of the model, it also gives the model the ability to predict different variations of words.

For example, let’s say that the word “Windows” is in the training dataset and we want to get the vector of the word “Wndows” after the training is finished. If the Word2Vec model is used for these operations, it will give an error that the word “Wndows” does not exist in the dictionary and will not return any vectors. However, if the FastText model is used for this process, both the vector will return and the word of “Windows” will be among the closest words.

As explained above, not only the word itself but also N-gram variations are included in training (Example 3-gram expressions for the word “Windows” -&gt; Win, ind, ndo, dow, ows).

Although the FastText model is used in many different areas today, it is frequently preferred especially when word embedding techniques are needed in OCR works. Especially compared to other techniques that do not tolerate the slightest OCR error, FastText provides a great advantage in obtaining vectors of even words that are not directly in their vocabulary. For this reason, it is one step ahead of other alternatives in problems where word mistakes may occur.
