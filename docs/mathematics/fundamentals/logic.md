# Logic

## Propositional Logic

### Proposition

Is a declarative sentence (that is, a sentence that declares a fact) that is either true or false, but not both.

### Conjunction

$p \land q$ (and)

### Disjunction

$p \lor q$ (or)

### Exclusive or

<img src="image1.jpg" style="width:2.45455in" />

The exclusive or of $p$ and $q$, denoted by $p \oplus q$ (or $p$ XOR $q$), is the proposition that is true when exactly one of $p$ and $q$ is true and is false otherwise.

### Conditional Statements

<img src="image7.jpg" style="width:2.45455in" />

Let $p$ and $q$ be propositions. The conditional statement $p \rightarrow q$ is the proposition “if $p$, then $q$.” The conditional statement $p \rightarrow q$ is false when $p$ is true and $q$ is false, and true otherwise. In the conditional statement $p \rightarrow q$, $p$ is called the hypothesis (or antecedent or premise) and $q$ is called the conclusion (or consequence).

### Biconditional

<img src="image11.jpg" style="width:2.50064in" />

Let $p$ and $q$ be propositions. The biconditional statement $p \leftrightarrow q$ is the proposition “$p$ if and only if $q$.” The biconditional statement $p \leftrightarrow q$ is true when $p$ and $q$ have the same truth values and is false otherwise. Biconditional statements are also called bi-implications.

### Precedence of Operators

<img src="image2.jpg" style="width:1.87303in" />

### Logic Circuits

![](logic/image6.jpg)

## Propositional Equivalences

### Tautology and Contingency

<img src="image4.jpg" style="width:2.91721in" />

- A compound proposition that is always true, no matter what the truth values of the propositional variables that occur in it, is called a tautology.
- A compound proposition that is always false is called a contradiction.
- A compound proposition that is neither a tautology nor a contradiction is called a contingency.

### $\equiv$ mark

The compound propositions $p$ and $q$ are called logically equivalent if $p \leftrightarrow q$ is a tautology.

The notation $p \equiv q$ denotes that $p$ and $q$ are logically equivalent.

### De Morgan’s Laws

<img src="image10.jpg" style="width:1.77379in" />

### Conditional disjunction equivalence

that $p \rightarrow q$ and $\neg p \lor q$ are logically equivalent

### Distributive law of disjunction over conjunction

that $p \lor (q \land r)$ and $(p \lor q) \land (p \lor r)$ are logically equivalent

### Overall

<img src="image3.jpg" style="width:3.75397in" />

<img src="image8.jpg" style="width:2.71445in" />

<img src="image13.jpg" style="width:2.46185in" />

## Predicates and Quantiﬁers

### Predicate Logic

Statements involving variables, such as

“$x > 3$, $x = y + 3$, $x + y = z$”

and

Computer $X$ is under attack by an intruder

and

“Computer $X$ is functioning properly”

are often found in mathematical assertions, computer programs, and system speciﬁcations. These statements are neither true nor false when the values of the variables are not speciﬁed. In this section

### Quantifiers

Quantiﬁcation expresses the extent to which a predicate is true over a range of elements. In English, the words all, some, many, none, and few are used in quantiﬁcations. We will focus on two types of quantiﬁcationAssessment here: universal quantiﬁcation, which tells us that a predicate is true for every element under consideration, and existential quantiﬁcation, which tells us that there is one or more element under consideration for which the predicate is true

- **Universal quantiﬁer:** The universal quantiﬁcation of $P(x)$ is the statement “$P(x)$ for all values of $x$ in the domain.”

  The notation $\forall x P(x)$ denotes the universal quantiﬁcation of $P(x)$. Here $\forall$ is called the universal quantiﬁer. We read $\forall x P(x)$ as “for all $x P(x)$” or “for every $x P(x)$.” An element for which $P(x)$ is false is called a counterexample to $\forall x P(x)$.

- **Existential quantiﬁer:** The existential quantiﬁcation of $P(x)$ is the proposition “There exists an element x in the domain such that P(x).”

  We use the notation $\exists x P(x)$ for the existential quantiﬁcation of $P(x)$. Here $\exists$ is called the existential quantiﬁer.

- **De Morgan’s Laws for Quantiﬁers:**

  ![](logic/image5.jpg)

## Inference

### Arguments

An argument in propositional logic is a sequence of propositions. All but the ﬁnal proposition in the argument are called premises and the ﬁnal proposition is called the conclusion. An argument is valid if the truth of all its premises implies that the conclusion is true.

An argument form in propositional logic is a sequence of compound propositions involving propositional variables. An argument form is valid if no matter which particular propositions are substituted for the propositional variables in its premises, the conclusion is true if the premises are all true.

<span dir="rtl">حاشیه: منظور همان استدلال کردن است، مثلا اگر الف و ب پس پ</span>

<span dir="rtl">حاشیه ۲: در حاشیه بالا الف و ب همان premises هستند و پ همان conclusion </span>

- **premises:** All but the ﬁnal proposition in the argument are called
- **conclusion:** the ﬁnal proposition is called the conclusion.
- **$\therefore$ symbol:** denotes “therefore”

### Rules of Inference

<img src="image12.jpg" style="width:5.79713in" />

<img src="image9.jpg" style="width:4.55445in" />
