# Parameter-Efficient Ensembling [Tabular]

## Description

Parameter-efficient ensembling is a technique that combines multiple models to improve performance while using fewer parameters than traditional ensembling methods.
It achieves this by having the ensemble members share a large portion of their weights, effectively reducing the overall parameter count.
This approach aims to retain the benefits of ensembling (improved accuracy, robustness) while mitigating the computational overhead associated with training and deploying multiple full-sized models.

## Workflow

- **Shared Weights**: These methods, like TabM (which utilizes variations of BatchEnsemble), create models that produce multiple predictions using the same underlying architecture and a large portion of shared weights. This means that instead of training and storing separate models, you're effectively training one model that behaves like an ensemble.
- **Specialized Adapters**: Some approaches involve using specialized "adapters" for each task or dataset, fine-tuning them while keeping the majority of the pre-trained model's parameters frozen. These adapters are then combined to form an ensemble, often with a weighted combination of their outputs.
- **Adaptive Rank**: Methods like AdaLoRA adjust the rank of low-rank adaptations (like LoRA) during training, allowing for more efficient use of parameters and potentially better performance.

## Benefits

- **Reduced Computational Cost**: Training and deploying a single model with shared weights is significantly less expensive than training and deploying multiple independent models.
- **Improved Accuracy**: Ensembling, even in a parameter-efficient way, can lead to better accuracy and generalization performance compared to using a single model.
- **Enhanced Robustness**: Parameter-efficient ensembling can also improve the robustness of the model, making it less susceptible to overfitting or outliers in the data.
- **Increased Practicality**: By reducing the computational burden, parameter-efficient ensembling makes it more feasible to apply ensembling techniques in real-world scenarios, especially with large models.
