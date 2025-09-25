# Loss Behavior Analysis {Divergence}

## Description

Loss behavior analysis helps identify and understand patterns in how the loss function changes during model training.
Recognizing issues like divergence, oscillation, and plateauing is essential for diagnosing training problems and improving model performance.

## Varieties

=== "Divergence"

    Instead of decreasing, the loss suddenly increases (sometimes shooting up to very large values or NaN).

    - **Why it happens**: Learning rate too high, exploding gradients, bad initialization, or unstable optimization.
    - **What it looks like**: Loss keeps growing instead of shrinking.

=== "Oscillation"

    The loss goes up and down a lot instead of steadily trending downward.

    - **Why it happens**: Learning rate is slightly too high, optimizer struggles to converge, or the model is bouncing around local minima.
    - **What it looks like**: Loss decreases overall, but with sharp jumps up and down.

=== "Plateauing"

    The loss stops improving (gets "stuck") at some value.

    - **Why it happens**: Model has reached a local minimum, learning rate is too low, or the capacity of the model is too small for the task.
    - **What it looks like**: Loss curve flattens out and doesn't drop further.
