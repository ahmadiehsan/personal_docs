# Early Stopping Regularization

## Description

Early stopping is a technique that's used to stop the training process when the performance of the model on the validation data starts to degrade.
This helps to prevent overfitting by stopping the model from continuing to learn from the training data when it has already reached its maximum performance.
This technique is usually used in iterative algorithms such as deep learning methods, where the model is being trained for multiple iterations (epochs).

To use early stopping, we usually train the model while evaluating the model performance on the training and validation subsets.
The model's performance usually improves on the training set with more training, but since the model has not seen the validation set, the validation error usually decreases initially and at some point, starts increasing again.
This point is where the model starts overfitting.

By visualizing the training and validation error of the model during training, we can identify and stop the model at this point.

<img src="image1.jpg" style="width:3.2899in" />

!!! info

    <span dir="rtl">بعضی وقت ها هر چقدر سیستم بیشتر با training set آموزش ببینه روی test set بدتر جواب میده، بخاطر همین با این تکنیک یه جایی از آموزش که جواب معقولی روی dev set های میده آنوزش رو متوقف میکنیم و با این کار از overfit شدن جلوگیری میکنیم.</span>
