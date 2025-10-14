# Vs (PCA & LDA)

## Description

- PCA reduces dimensions by focusing on the genes with the most variation.

    - This is useful for plotting data with a lot of dimensions (or a lot of genes) onto a simple X/Y plot.
    - However, in this case we're not super interested in the genes with the most variation.
    - Instead, we're interested in maximizing the separability between the two groups so we can make the best decisions.

- Linear Discriminant Analysis (LDA) is like PCA, but it focuses on maximizing the separability among known categories.
- Both rank the new axes in order of importance.

    - PC1 (the first new axis that PCA creates) accounts for the most variation in the data.

        - PC2 (the second new axis) does the second best job...

    - LD1 (the first new axis that LDA creates) accounts for the most variation between the categories.

        - LD2 (the second new axis) does the second best job...

- Both can let you dig in and see which genes are driving the new axes.
- LDA is like PCA – both try to reduce dimensions

    - PCA looks at the genes with the most variation.
    - LDA tries to maximize the separation of known categories.
