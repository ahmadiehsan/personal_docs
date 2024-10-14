# Matrix

## Description

<img src="image11.jpg" style="width:5.77917in" />

We can show a matrix with multiple vectors:

<img src="image10.jpg" style="width:1.79278in" />

## Operations

### Multiplication With Another Matrix

<img src="image1.jpg" style="width:2.39597in" />

We will use this for transformation composition, like this:

$(f◦g)(\vec{x}) = f(g(a)) = f(Ax) = B(Ax) = BA(x)$

### Multiplication With Vector (Matrix-Vector Product)

<img src="image5.jpg" style="width:4.22663in" />

<img src="image7.jpg" style="width:4.21005in" />

Matrix-vector product is always a linear transformation.

### Transpose

<img src="image2.jpg" style="width:3.38194in" />

### Reduced Row Echelon Form (RREF)

<img src="image3.jpg" style="width:2.40803in" />

### Determinant

<img src="image6.jpg" style="width:4.93333in" />

<img src="image4.jpg" style="width:3.56919in" />

- The determinant is nonzero if and only if the matrix is invertible and the linear map represented by the matrix is an isomorphism.
- The determinant of a matrix is equal to the determinant of its transpose

## Null Space

The null space of any matrix $A$ consists of all the vectors $B$ such that $AB=0$ and $B$ is not zero.

We will show the null space of $\mathbf{A}$ with $N(\mathbf{A})$.

<img src="image8.jpg" style="width:2.73467in" />

- It can also be thought of as the solution obtained from $AB=0$ where $A$ is a known matrix of size $m x n$ and $B$ is a matrix to be found of size $n x k$.
- $N(\mathbf{A}) = N(RREF(\mathbf{A}))$

## Column Space

We will show the nullspace of $\mathbf{A}$ with $C(\mathbf{A})$.

<img src="image9.jpg" style="width:3.15928in" />

## Identity Matrix

<img src="image12.jpg" style="width:3.975in" />
