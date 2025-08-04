# Recursive Feature Elimination (RFE) {Wrapper}

## Description

Functioning as a backward elimination approach, RFE systematically removes the least important feature until a predetermined number of features remains. **During each iteration, a machine learning model is trained on the existing features**, and the least important feature is pruned based on its feature importance score. This sequential process persists until the specified number of features is attained. The feature importance score can be extracted from diverse methods, including coefficient values from linear models or feature importance scores derived from decision trees. **RFE is a computationally expensive method**, but **it can be useful when the number of features is very large and there is a need to reduce the feature space**. An alternative approach is to have feature selection during the training process, something that's done via embedding methods.
