# Log Loss [Binary Classification]

## Description

- **Use case**: Classification problems (Binary classification)
- **When to use**: Is specifically used for binary classification problems where the output is a probability (e.g., logistic regression). It quantifies the difference between the predicted probability and the true label (0 or 1).
- **Key property**: Encourages probabilistic models to predict values that are closer to the true label (e.g., probability of 0 or 1). Assigning a higher predicted probability to the wrong class results in higher penalties.
- **Example applications**:

    - Predicting whether an email is spam or not
    - Determining if a customer will churn (leave)

## Formula

=== "Training Shape"

    <img src="image1.png" style="width:4in" />

    <span dir="rtl">نمودار loss function:</span>

    <img src="image5.png" style="width:5.5in" />

    <img src="image6.png" style="width:5.5in" />

    <span dir="rtl">چون مقادیر این مدل حتما بین 0 تا 1 است از بخش های بزرگتر از 1 در دو تصویر بالا صرف نظر شد</span>

=== "Simplified Shape (Normal)"

    <img src="image3.png" style="width:5in" />

=== "Simplified Shape (Regularized)"

    <img src="image4.jpg" style="width:5.5in" />

## Gradient Descent

<img src="image2.png" style="width:4in" />
