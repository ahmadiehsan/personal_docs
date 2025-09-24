# Weight Initialization

## Description

<span dir="rtl">با استفاده از تکنیک های زیر میتونیم یه عدد اولیه خوب برای w انتخاب کنیم که از exploding/vanishing تو deep neural network جلوگیری کنه.</span>

For RELU activation function:

$$\sqrt{\frac{2}{size^{[l-1]}}}$$

```python
W = np.random.randn(size_l, size_l-1) * np.sqrt(2/size_l-1)
```

For tanh activation function :

$$\sqrt{\frac{1}{size^{[l-1]}}}$$

```python
W = np.random.randn(size_l, size_l-1) * np.sqrt(1/size_l-1)
```

Another commonly used heuristic is:

$$\sqrt{\frac{2}{size^{[l-1]} + size^{[l]}}}$$

```python
W = np.random.randn(size_l, size_l-1) * np.sqrt(2 / (size_l-1 + size_l))
```
