# Word2Vec [NLP: Embedding] [Unsup]

## Description

Is a technique in natural language processing (NLP) for obtaining vector representations of words. These vectors capture information about the meaning of the word based on the surrounding words. The word2vec algorithm estimates these representations by modelling text in a large corpus. Once trained, such a model can detect synonymous words or suggest additional words for a partial sentence.

Word2vec represents a word as a high-dimension vector of numbers which capture relationships between words. In particular, words which appear in similar contexts are mapped to vectors which are nearby as measured by cosine similarity. This indicates the level of semantic similarity between the words, so for example the vectors for walk and ran are nearby, as are those for but and however, and Berlin and Germany.

This means we can also perform vector arithmetic with the word vectors. For example:

Queen = King - Man + Woman

<img src="image1.jpg" style="width:2.75in" />

## Varieties

It does so in one of two ways, either using context to predict a target word (a method known as continuous bag of words, or **CBOW**), or using a word to predict a target context, which is called **skip-gram**.

<img src="image2.png" style="width:5.77114in" />

## Vs TF-IDF & One Hot Encoding

In the Word2Vec method, unlike One Hot Encoding and TF-IDF methods, an unsupervised learning process is performed. Unlabeled data is trained via artificial neural networks to create the Word2Vec model that generates word vectors. Unlike other methods, the vector size is less than the number of unique words in the corpus. The vector size can be selected according to the corpus size and the type of project. This is particularly beneficial for huge data. For example, if we assume that there are 300,000 unique words in a large corpus when vector creation is performed with One Hot Encoding, a vector of 300,000 size is created for each word, with the value of only one element of 1, and the others 0. However, by choosing the vector size 300 (it can be more or less depending on the user’s choice) on the Word2Vec side, unnecessary large-size vector operations are avoided.