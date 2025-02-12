# TF-IDF

## Description

TF-IDF is a statistical measure used to determine the mathematical significance of words in documents.

The vectorization process is similar to One Hot Encoding. Alternatively, the value corresponding to the word is assigned a TF-IDF value instead of 1. The TF-IDF value is obtained by multiplying the TF and IDF values.

- **TF (Term Frequency)**: Is the ratio of the number of target terms in the document to the total number of terms in the document.
- **IDF (Inverse Document Frequency)**: Is the logarithm of the ratio of the total number of documents to the number of documents in which the target term occurs. At this stage, it does not matter how many times the term appears in the document. It is sufficient to determine whether it has passed or not.

## Formula

<img src="image1.png" style="width:4.00854in" />

## Example

As an example, let's find the TF-IDF values for 3 documents consisting of 1 sentence.

- He is Walter
- He is William
- He isn't Peter or September

In the above example, "He" is used in all 3 documents, "is" is in 2 documents, and "or" is in only one document. According to these, let's find the TF and then the IDF values, respectively.

TF: Values are calculated according to the above example, it will be:

- 0.33, 0.33, 0.33
- 0.33, 0.33, 0.33
- 0.20, 0.20, 0.20, 0.20, 0.20

IDF: In this example, the base value of the logarithm to be taken is determined as 10. However, there is no problem in using different values.

- "He": Log(3/3)= 0
- "is": Log(3/2):0.1761
- "or, Peter, ..": log(3/1) : 0.4771

Thus, both TF and IDF values were obtained. If vectorization is created with these values, firstly a vector consisting of elements equal to the number of unique words in all documents is created for each document (in this example, there are 8 terms). At this stage, there is a problem to be solved. As seen in the term "He", since the IDF value is 0, the TF-IDF value will also be zero. However, words that are not included in the document during the vectorization process (for example, the phrase "Peter" is not included in the 1st sentence) will be assigned a value of 0. In order to avoid confusion here, TF-IDF values are smoothed for vectorization. The most common method is to add 1 to the obtained values.

Depending on the purpose, normalization can be applied to these values later. If the vectorization process is created according to the above-mentioned:

- 1\. , 1.1761 , 1.4771 , 0. , 0. , 0. , 0. , 0.
- 1\. , 1.1761 , 0. , 1.4771 , 0. , 0. , 0. , 0.
- 1\. , 0. , 0. , 0. , 1.4771 , 1.4771, 1.4771 , 1.4771
