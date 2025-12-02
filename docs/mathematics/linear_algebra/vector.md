# Vector

## Description

![](vector/image16.jpg)

![](vector/image6.jpg)

- Starting point doesn't mean for Vectors
- Vectors will show by lowercase letters and an arrow on top of it or just with a bold lowercase letter
- Vector = Magnitude + Direction
- Velocity = Magnitude + Direction
- So indeed Velocity is a Vector
- Standard Position (Origin): $(0, 0)$ is the standard position so when one the tail of one Vector is in this position we will say that this Vector is in the standard position

## N Dimensional Real Coordinate Space

![](vector/image3.jpg)

![](vector/image8.jpg)

- **Tuple**: means a list of numbers.
- **Cartesian coordinate system**: is the specific name for 2-tuples.
- **3-tuples**: means 3 numbers in one matrix.

## Operations

### Addition

![](vector/image24.jpg)

- All the purple arrows are the same
- All the green arrows are the same
- The starting point doesn't matter in Vectors
- The blue arrow completely shows us how adding two Vectors to each other works in the background

### Multiplication

![](vector/image13.jpg)

### Subtraction

![](vector/image27.jpg)

### Dot Product

Will tell us how much our vectors are moving together.

![](vector/image26.jpg)

![](vector/image20.jpg)

$\vec{w} \cdot \vec{x}$  = $w_1x_1 + w_2x_2 + w_3x_3 + \dots + w_nx_n$

- The order doesn't matter in a dot product: $\vec{v} \cdot \vec{w} = \vec{w} \cdot \vec{v}$
- Distribution is applicable on the dot product:

  $(\vec{v} + \vec{w}) \cdot \vec{x} = (\vec{v} \cdot \vec{x} + \vec{w} \cdot \vec{x})$

  $(c \vec{v}) \cdot \vec{w} = c (\vec{v} \cdot \vec{w})$

### Cross Product

![](vector/image10.jpg)

Will give us the normal vector of the space (plane) of two other vectors ($\vec{a}$ and $\vec{b}$).

$$
\begin{bmatrix}
a_1 \\
a_2 \\
a_3
\end{bmatrix}
\times
\begin{bmatrix}
b_1 \\
b_2 \\
b_3
\end{bmatrix}
=
\begin{bmatrix}
a_2 b_3 - a_3 b_2 \\
a_3 b_1 - a_1 b_3 \\
a_1 b_2 - a_2 b_1
\end{bmatrix}
$$

The cross-product is only applicable in $R_3$.

### Length (Magnitude)

Let the vector $\vec{a}$ be represented as:

$$
\vec{a} = \begin{bmatrix}
a_1 \\
a_2 \\
\vdots \\
a_n
\end{bmatrix}
$$

The magnitude or length of vector $\vec{a}$ can be calculated as:

$$
\|\vec{a}\| = \sqrt{a_1^2 + a_2^2 + \dots + a_n^2}
$$

Alternatively, using the dot product, the magnitude can be expressed as:

$$
\|\vec{a}\| = \sqrt{\vec{a} \cdot \vec{a}}
$$

## Unit Vector

### Unit Vector of Axes

![](vector/image15.jpg)

### Unit Vector of a Vector

To find a unit vector, **u**, in the same direction of a vector, **v**, we divide the vector by its magnitude.

$$
\vec{u} = \frac{\vec{v}}{\|\vec{v}\|} = \frac{1}{\|\vec{v}\|} \vec{v}
$$

For a vector $\vec{v} = \begin{bmatrix} a & b \end{bmatrix}$ its magnitude is given by

$$
\|\vec{v}\| = \sqrt{a^2 + b^2}
$$

## Cauchy–Schwarz Inequality

$$
|\vec{x} \cdot \vec{y}| \leq \|\vec{x}\| \, \|\vec{y}\|
$$

$$
|\vec{x} \cdot \vec{y}| = \|\vec{x}\| \, \|\vec{y}\| \iff \vec{x} = c\vec{y}
$$

## Triangle inequality

$$
\|\vec{x} + \vec{y}\| \leq \|\vec{x}\| + \|\vec{y}\|
$$

## Perpendicular Vectors (Orthogonal Vectors)

![](vector/image7.png)

The vectors $\vec{x}$ and $\vec{y}$ are perpendicular if, and only if, their dot product is equal to zero: $\vec{x} . \vec{y} = 0$

## Normal Vector

![](vector/image5.jpg)

A normal is an object such as a line, ray, or vector that is perpendicular to a given object.

## Eigenvectors & Eigenvalues

Is a nonzero vector that changes at most by a scalar factor when that linear transformation is applied to it.
The corresponding eigenvalue, often denoted by lambda, is the factor by which the eigenvector is scaled.

![](vector/image12.jpg)

Matrix $A$ acts by stretching the vector $\vec{x}$, not changing its direction, so $\vec{x}$ is an eigenvector of $A$.

![](vector/image21.jpg)
