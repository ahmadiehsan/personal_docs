# Knowledge Distillation

## Description

Is a technique where a smaller, less complex AI model (the "student") learns from a larger, more complex AI model (the "teacher").
This allows for the creation of efficient, resource-friendly models that retain much of the performance of their larger counterparts.

The process involves training the student model on data generated or influenced by the teacher model, essentially transferring the "knowledge" of the larger model to the smaller one.

## Workflow

- **Teacher Model**: A larger, pre-trained model (e.g., a LLM) serves as the teacher.
- **Student Model**: A smaller model, often with fewer parameters and less computational complexity, is the student.
- **Knowledge Transfer**: The teacher model is used to generate predictions or other outputs (sometimes called "soft targets") that the student model learns to mimic. This could involve using the teacher's output probabilities, intermediate layer activations, or even step-by-step reasoning.
- **Loss Function**: The student model is trained using a loss function that compares its outputs to the teacher's outputs, encouraging it to learn the teacher's behavior.
