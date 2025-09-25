# Encoding {One-Hot} {TF-IDF}

## Description

Encoding is the process of converting categorical data into numerical formats so that machine learning models can interpret and use them effectively.

## Varieties

=== "One-Hot"

    Considering we have the numeric representation of any categorical attribute with m labels (after transformation), the one-hot encoding scheme encodes or transforms the attribute into m binary features which can only contain a value of 1 or 0.
    Each observation in the categorical feature is thus converted into a vector of size m with only one of the values as 1 (indicating it as active).

    <img src="one_hot_encoding.jpg" style="width:3.5in" />

=== "Dummy Coding"

    The dummy coding scheme is similar to the one-hot encoding scheme, except in the case of the dummy coding scheme, when applied on a categorical feature with m distinct labels, we get m - 1 binary features.
    Thus each value of the categorical variable gets converted into a vector of size m - 1.
    The extra feature is completely disregarded and thus if the category values range from {0, 1, …, m-1} the 0th or the m - 1th feature column is dropped and corresponding category values are usually represented by a vector of all zeros (0).

    <img src="dummy_coding.jpg" style="width:3.5in" />

=== "Effect Coding"

    The effect coding scheme is actually very similar to the dummy coding scheme, except during the encoding process, the encoded features or feature vector, for the category values which represent all 0 in the dummy coding scheme, is replaced by -1 in the effect coding scheme.

=== "TF-IDF"

    TF-IDF is a statistical measure used to determine the mathematical significance of words in documents.

    The vectorization process is similar to One Hot Encoding.
    Alternatively, the value corresponding to the word is assigned a TF-IDF value instead of 1.
    The TF-IDF value is obtained by multiplying the TF and IDF values.

    - **TF (Term Frequency)**: Is the ratio of the number of target terms in the document to the total number of terms in the document.
    - **IDF (Inverse Document Frequency)**: Is the logarithm of the ratio of the total number of documents to the number of documents in which the target term occurs. At this stage, it does not matter how many times the term appears in the document. It is sufficient to determine whether it has passed or not.

    <img src="tf_idf.png" style="width:4in" />

=== "Feature Hashing"

    The feature hashing scheme is another useful feature engineering scheme for dealing with large scale categorical features.
    In this scheme, a hash function is typically used with the number of encoded features pre-set (as a vector of predefined length) such that the hashed values of the features are used as indices in this predefined vector and values are updated accordingly.
    Since a hash function maps a large number of values into a small finite set of values, multiple different values might create the same hash which is termed as collisions.
    Typically, a signed hash function is used so that the sign of the value obtained from the hash is used as the sign of the value which is stored in the final feature vector at the appropriate index.
    This should ensure lesser collisions and lesser accumulation of error due to collisions.

    Hashing schemes work on strings, numbers and other structures like vectors.
    **You can think of hashed outputs as a finite set of b bins such that when the hash function is applied on the same values\\categories, they get assigned to the same bin (or subset of bins) out of the b bins based on the hash value.** We can pre-define the value of b which becomes the final size of the encoded feature vector for each categorical attribute that we encode using the feature hashing scheme.

    Thus even if we have over 1000 distinct categories in a feature and we set b=10 as the final feature vector size, the output feature set will still have only 10 features as compared to 1000 binary features if we used a one-hot encoding scheme.

=== "Bin-Counting"

    The encoding schemes like One-Hot Encoding Scheme, work quite well on categorical data in general, but they start causing problems when the number of distinct categories in any feature becomes very large.
    Essential for any categorical feature of m distinct labels, you get m separate features.
    This can easily increase the size of the feature set causing problems like storage issues, and model training problems concerning time, space, and memory.
    Besides this, we also have to deal with what is popularly known as the "curse of dimensionality" where basically with an enormous number of features and not enough representative samples, model performance starts getting affected often leading to overfitting.

    Hence we need to look towards other categorical data feature engineering schemes for features having a large number of possible categories (like IP addresses).
    The bin-counting scheme is a useful scheme for dealing with categorical variables having many categories.
    **In this scheme, instead of using the actual label values for encoding, we use probability-based statistical information about the value and the actual target or response value which we aim to predict in our modeling efforts.**

=== "Nominal"

    Nominal attributes consist of discrete categorical values with no notion or sense of order amongst them.

    The idea here is to transform these attributes into a more representative numerical format that can be easily understood by downstream code and pipelines.

    Movie, music, and video game genres, country names, food, and cuisine types are examples of nominal categorical attributes.

=== "Ordinal"

    Ordinal attributes are categorical attributes with a sense of order among the values.

    Shoe sizes, education levels, and employment roles are some examples of ordinal categorical attributes.

## Example

=== "One-Hot"

    ```python
    from sklearn.preprocessing import OneHotEncoder, LabelEncoder

    # transform and map pokemon generations
    gen_le = LabelEncoder()
    gen_labels = gen_le.fit_transform(poke_df["Generation"])
    poke_df["Gen_Label"] = gen_labels

    # encode generation labels using one-hot encoding scheme
    gen_ohe = OneHotEncoder()
    gen_feature_arr = gen_ohe.fit_transform(poke_df[["Gen_Label"]]).toarray()

    gen_feature_labels = list(gen_le.classes_)
    gen_features = pd.DataFrame(gen_feature_arr, columns=gen_feature_labels)

    poke_df_ohe = pd.concat([poke_df_sub, gen_features, leg_features], axis=1)
    columns = sum([
        ["Name", "Generation", "Gen_Label"],
        gen_feature_labels,
        ["Legendary", "Lgnd_Label"],
        leg_feature_labels
    ], [])
    ```

=== "Dummy Coding"

    ```python
    gen_dummy_features = pd.get_dummies(poke_df["Generation"], drop_first=True)

    pd.concat([poke_df[["Name", "Generation"]], gen_dummy_features], axis=1).iloc[4:10]
    ```

=== "Effect Coding"

    ```python
    gen_onehot_features = pd.get_dummies(poke_df["Generation"])
    gen_effect_features = gen_onehot_features.iloc[:, :-1]
    gen_effect_features.loc[np.all(gen_effect_features == 0, axis=1)] = -1.

    pd.concat([poke_df[["Name", "Generation"]], gen_effect_features], axis=1).iloc[4:10]
    ```

=== "TF-IDF"

    As an example, let's find the TF-IDF values for 3 documents consisting of 1 sentence.

    - He is Walter
    - He is William
    - He isn't Peter or September

    In the above example, "He" is used in all 3 documents, "is" is in 2 documents, and "or" is in only one document.
    According to these, let's find the TF and then the IDF values, respectively.

    TF: Values are calculated according to the above example, it will be:

    - 0.33, 0.33, 0.33
    - 0.33, 0.33, 0.33
    - 0.20, 0.20, 0.20, 0.20, 0.20

    IDF: In this example, the base value of the logarithm to be taken is determined as 10.
    However, there is no problem in using different values.

    - "He": Log(3/3)= 0
    - "is": Log(3/2):0.1761
    - "or, Peter, ..": log(3/1) : 0.4771

    Thus, both TF and IDF values were obtained.
    If vectorization is created with these values, firstly a vector consisting of elements equal to the number of unique words in all documents is created for each document (in this example, there are 8 terms).
    At this stage, there is a problem to be solved.
    As seen in the term "He", since the IDF value is 0, the TF-IDF value will also be zero.
    However, words that are not included in the document during the vectorization process (for example, the phrase "Peter" is not included in the 1st sentence) will be assigned a value of 0.
    In order to avoid confusion here, TF-IDF values are smoothed for vectorization.
    The most common method is to add 1 to the obtained values.

    Depending on the purpose, normalization can be applied to these values later.
    If the vectorization process is created according to the above-mentioned:

    - 1\. , 1.1761 , 1.4771 , 0. , 0. , 0. , 0. , 0.
    - 1\. , 1.1761 , 0. , 1.4771 , 0. , 0. , 0. , 0.
    - 1\. , 0. , 0. , 0. , 1.4771 , 1.4771, 1.4771 , 1.4771

=== "Feature Hashing"

    We will now use a feature hashing scheme by leveraging scikit-learn's FeatureHasher class, which uses a signed 32-bit version of the Murmurhash3 hash function.
    We will pre-define the final feature vector size to be 6 in this case.

    ```python
    from sklearn.feature_extraction import FeatureHasher

    fh = FeatureHasher(n_features=6, input_type="string")
    hashed_features = fh.fit_transform(vg_df["Genre"])
    hashed_features = hashed_features.toarray()
    pd.concat([vg_df[["Name", "Genre"]], pd.DataFrame(hashed_features)], axis=1).iloc[1:7]
    ```

=== "Bin-Counting"

    A simple example would be based on past historical data for IP addresses and the ones that were used in DDOS attacks; we can build probability values for a DDOS attack being caused by any of the IP addresses.
    Using this information, we can encode an input feature that depicts that if the same IP address comes in the future, what is the probability value of a DDOS attack being caused?
    This scheme needs historical data as a prerequisite and is an elaborate one.

=== "Nominal"

    ```python
    from sklearn.preprocessing import LabelEncoder

    gle = LabelEncoder()
    genre_labels = gle.fit_transform(vg_df["Genre"])
    ```

=== "Ordinal"

    In general, there is no generic module or function to map and transform these features into numeric representations based on order automatically.

    Hence we can use a custom encoding/mapping scheme.

    ```python
    gen_ord_map = {"Gen 1": 1, "Gen 2": 2, "Gen 3": 3,
                "Gen 4": 4, "Gen 5": 5, "Gen 6": 6}

    poke_df["GenerationLabel"] = poke_df["Generation"].map(gen_ord_map)
    ```
