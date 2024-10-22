# Transformation

## Description

Mapping one vector from one vector space into another vector space by a function.

Function: $f: \vec{a} \rightarrow \vec{b}$

Domain: $f: R_n \rightarrow R_m$

## Transformations

### Linear Transformation (Linear Map)

A linear map (also called a linear mapping, linear transformation, vector space homomorphism, or in some contexts linear function) is a mapping $\vec{v}$ to $\vec{w}$ between two vector spaces that preserves the operations of vector addition and scalar multiplication.

Rules:

- $\vec{a}, \vec{b} \in \mathbb{R}^n$
- $T(\vec{a} + \vec{b}) = T(\vec{a}) + T(\vec{b})$
- $T(c \vec{a}) = c \, T(\vec{a})$

We can always show a linear transformation via a matrix-vector product, like this: $T(\vec{x}) = A\vec{x}$

### Rotation Transformation

<img src="image9.jpg" style="width:3in" />

$R = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}$

$Rv = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} x \cos \theta - y \sin \theta \\ x \sin \theta + y \cos \theta \end{bmatrix}$

## Transformation Types

- **Onto:** If $T(\vec{x}) = A_{m \times n} \vec{x}$ then $Rank(A) = m$
- **One-to-One:** If $T(\vec{x}) = A_{m \times n} \vec{x}$ then $Rank(A) = n$
- **Invertible:** There should be a onto and one-to-one transformation

## Operations

### Addition

- $T(u+v) = T(u) + T(v)$
- $(T+S)(\vec{x}) = T(x) + S(x) = Ax + Bx = (A+B)x$

### Multiplication

- $T(cu) = cT(u)$
- $(cT)(\vec{x}) = c(T(x)) = c(Ax) = (cA)x$
