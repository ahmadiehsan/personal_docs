# Functions

## Description

Let A and B be nonempty sets. A function f from A to B is an assignment of exactly one element of B to each element of A. We write f(a) = b if b is the unique element of B assigned by the function f to the element a of A. If f is a function from A to B, we write f: A → B

## Result of Set Under a Function

### Image

Let f be a function from A to B and let S be a subset of A. The image of S under the function f is the subset of B that consists of the images of the elements of S. We denote the image of S by f(S), so

f(S) = {t ∣∃s∈S (t = f(s))}.

We also use the shorthand {f(s) ∣ s ∈ S} to denote this set.

The image of a function is the set of all output values it may produce.

<img src="image1.jpg" style="width:1.90163in" />

### Preimage

For a given function, the set of all elements of the domain that are mapped into a given subset of the codomain.

<img src="image6.png" style="width:0.63031in" />

## Function Types

### One to One Function (Injective)

A function f is said to be one-to-one, or an injection, if and only if f(x) = f(y) implies that x = y for all x and y in the domain of f.

A function is said to be injective if it is one-to-one.

<img src="image3.jpg" style="width:1.13368in" />

### Increasing and Decreasing Function

A function f whose domain and codomain are subsets of the set of real numbers is called increasing if f(x) ≤ f(y), and strictly increasing if f(x) &lt; f(y), whenever x &lt; y and x and y are in the domain of f. Similarly, f is called decreasing if f(x) ≥ f(y), and strictly decreasing if f(x) &gt; f(y), whenever x &lt; y and x and y are in the domain of f. (The word strictly in this deﬁnition indicates a strict inequality.)

### Onto Function (Surjective)

A function f from X to Y is called onto, or a surjection, if and only if for every element y ∈ Y there is at least an element x ∈ X with f(x) = y.

A function f is called surjective if it is onto.

<img src="image2.jpg" style="width:1.02559in" />

### Identity Function

Is a function that always returns the value that was used as its argument, unchanged. That is, when f is the identity function, the equality f(X) = X is true for all values of X to which f can be applied.

We will show this function by I (capital i).

### Invertible Function

A function is invertible if and only if is a onto and one-to-one function.

## Composition

Let g be a function from the set A to the set B and let f be a function from the set B to the set C. The composition of the functions f and g, denoted for all a ∈ A by f◦g, is the function from A to C deﬁned by

(f◦g)(a) = f(g(a))

<img src="image4.jpg" style="width:5.83498in" />