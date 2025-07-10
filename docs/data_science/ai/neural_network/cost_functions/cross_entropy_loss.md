# Cross-Entropy Loss {Multi-Class Classification}

## Description

- **Use case**: Classification problems (Multi-class problems)
- **When to use**: Is used in multi-class classification tasks where the output represents the predicted probability distribution over multiple classes (softmax probabilities). It measures the dissimilarity between the predicted probability distribution and the actual distribution (one-hot encoded true labels).
- **Key property**: Pushes the model to assign high probability to the correct class while minimizing the probability of other classes.
- **Example applications**:

   - Image classification tasks (e.g., identifying objects like cars, cats, or trees in an image)
   - Natural Language Processing (e.g., sentiment analysis, text classification)

## Formula

$$
\text{Cross-Entropy Loss} = - \frac{1}{N} \sum_{i=1}^N \sum_{c=1}^C y_{i,c} \log(\hat{y}_{i,c})
$$

- $C$ is the number of classes
- $y_{i,c}$ is the true label (1 for the correct class, 0 otherwise)
- $\hat{y}_{i,c}$ is the predicted probability for class $c$ for the $i$-th example
