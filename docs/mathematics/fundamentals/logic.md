# Logic

## Propositional Logic

### Proposition

Is a declarative sentence (that is, a sentence that declares a fact) that is either true or false, but not both.

### Conjunction

$p \land q$ (and)

### Disjunction

$p \lor q$ (or)

### Exclusive or

The truth table for the Exclusive Or of two propositions:

| $p$ | $q$ | $p \oplus q$ |
|-----|-----|--------------|
| T   | T   | F            |
| T   | F   | T            |
| F   | T   | T            |
| F   | F   | F            |

The exclusive or of $p$ and $q$, denoted by $p \oplus q$ (or $p$ XOR $q$), is the proposition that is true when exactly one of $p$ and $q$ is true and is false otherwise.

### Conditional Statements

The truth table for the Conditional Statement $p \rightarrow q$:

| $p$ | $q$ | $p \rightarrow q$ |
|-----|-----|-------------------|
| T   | T   | T                 |
| T   | F   | F                 |
| F   | T   | T                 |
| F   | F   | T                 |

Let $p$ and $q$ be propositions. The conditional statement $p \rightarrow q$ is the proposition "if $p$, then $q$." The conditional statement $p \rightarrow q$ is false when $p$ is true and $q$ is false, and true otherwise. In the conditional statement $p \rightarrow q$, $p$ is called the hypothesis (or antecedent or premise) and $q$ is called the conclusion (or consequence).

### Biconditional

The truth table for the Biconditional $p \leftrightarrow q$:

| $p$ | $q$ | $p \leftrightarrow q$  |
|-----|-----|------------------------|
| T   | T   | T                      |
| T   | F   | F                      |
| F   | T   | F                      |
| F   | F   | T                      |

Let $p$ and $q$ be propositions. The biconditional statement $p \leftrightarrow q$ is the proposition "$p$ if and only if $q$." The biconditional statement $p \leftrightarrow q$ is true when $p$ and $q$ have the same truth values and is false otherwise. Biconditional statements are also called bi-implications.

### Precedence of Operators

Precedence of logical operators:

| Operator          | Precedence |
|-------------------|------------|
| $\neg$            | 1          |
| $\land$           | 2          |
| $\lor$            | 3          |
| $\to$             | 4          |
| $\leftrightarrow$ | 5          |

### Logic Circuits

![](logic/image6.jpg)

## Propositional Equivalences

### Tautology and Contingency

Examples of a tautology and a contradiction:

| p | $\neg p$ | $p \lor \neg p$ | $p \land \neg p$ |
|---|----------|-----------------|------------------|
| T | F        | T               | F                |
| F | T        | T               | F                |

- A compound proposition that is always true, no matter what the truth values of the propositional variables that occur in it, is called a tautology.
- A compound proposition that is always false is called a contradiction.
- A compound proposition that is neither a tautology nor a contradiction is called a contingency.

### $\equiv$ mark

The compound propositions $p$ and $q$ are called logically equivalent if $p \leftrightarrow q$ is a tautology.

The notation $p \equiv q$ denotes that $p$ and $q$ are logically equivalent.

### De Morgan’s Laws

- $\neg(p \land q) \equiv \neg p \lor \neg q$
- $\neg(p \lor q) \equiv \neg p \land \neg q$

### Conditional disjunction equivalence

That $p \rightarrow q$ and $\neg p \lor q$ are logically equivalent

### Distributive law of disjunction over conjunction

That $p \lor (q \land r)$ and $(p \lor q) \land (p \lor r)$ are logically equivalent

### Overall

Logical equivalences:

| Equivalence                                                                                                           | Name                |
|-----------------------------------------------------------------------------------------------------------------------|---------------------|
| $p \land \mathbf{T} \equiv p$ <br> $p \lor \mathbf{F} \equiv p$                                                       | Identity laws       |
| $p \lor \mathbf{T} \equiv \mathbf{T}$ <br> $p \land \mathbf{F} \equiv \mathbf{F}$                                     | Domination laws     |
| $p \lor p \equiv p$ <br> $p \land p \equiv p$                                                                         | Idempotent laws     |
| $\neg(\neg p) \equiv p$                                                                                               | Double negation law |
| $p \lor q \equiv q \lor p$ <br> $p \land q \equiv q \land p$                                                          | Commutative laws    |
| $(p \lor q) \lor r \equiv p \lor (q \lor r)$ <br> $(p \land q) \land r \equiv p \land (q \land r)$                    | Associative laws    |
| $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$ <br> $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$ | Distributive laws   |
| $\neg(p \land q) \equiv \neg p \lor \neg q$ <br> $\neg(p \lor q) \equiv \neg p \land \neg q$                          | De Morgan’s laws    |
| $p \lor (p \land q) \equiv p$ <br> $p \land (p \lor q) \equiv p$                                                      | Absorption laws     |
| $p \lor \neg p \equiv \mathbf{T}$ <br> $p \land \neg p \equiv \mathbf{F}$                                             | Negation laws       |

Logical equivalences involving conditional statements:

| Equivalence                                          |
|------------------------------------------------------|
| $p \to q \equiv \neg p \lor q$                       |
| $p \to q \equiv \neg q \to \neg p$                   |
| $p \lor q \equiv \neg p \to q$                       |
| $p \land q \equiv \neg(p \to \neg q)$                |
| $\neg(p \to q) \equiv p \land \neg q$                |
| $(p \to q) \land (p \to r) \equiv p \to (q \land r)$ |
| $(p \to r) \land (q \to r) \equiv (p \lor q) \to r$  |
| $(p \to q) \lor (p \to r) \equiv p \to (q \lor r)$   |
| $(p \to r) \lor (q \to r) \equiv (p \land q) \to r$  |

Logical equivalences involving biconditional statements:

| Equivalence                                                         |
|---------------------------------------------------------------------|
| $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$              |
| $p \leftrightarrow q \equiv \neg p \leftrightarrow \neg q$          |
| $p \leftrightarrow q \equiv (p \land q) \lor (\neg p \land \neg q)$ |
| $\neg(p \leftrightarrow q) \equiv p \leftrightarrow \neg q$         |

## Predicates and Quantiﬁers

### Predicate Logic

Statements involving variables, such as "$x > 3$, $x = y + 3$, $x + y = z$" and "Computer $X$ is under attack by an intruder" and "Computer $X$ is functioning properly" are often found in mathematical assertions, computer programs, and system speciﬁcations. These statements are neither true nor false when the values of the variables are not speciﬁed.

### Quantifiers

Quantiﬁcation expresses the extent to which a predicate is true over a range of elements. In English, the words all, some, many, none, and few are used in quantiﬁcations. We will focus on two types of quantiﬁcationAssessment here: universal quantiﬁcation, which tells us that a predicate is true for every element under consideration, and existential quantiﬁcation, which tells us that there is one or more element under consideration for which the predicate is true

- **Universal quantiﬁer:** The universal quantiﬁcation of $P(x)$ is the statement "$P(x)$ for all values of $x$ in the domain."

  The notation $\forall x P(x)$ denotes the universal quantiﬁcation of $P(x)$. Here $\forall$ is called the universal quantiﬁer. We read $\forall x P(x)$ as "for all $x P(x)$" or "for every $x P(x)$." An element for which $P(x)$ is false is called a counterexample to $\forall x P(x)$.

- **Existential quantiﬁer:** The existential quantiﬁcation of $P(x)$ is the proposition "There exists an element x in the domain such that P(x)."

  We use the notation $\exists x P(x)$ for the existential quantiﬁcation of $P(x)$. Here $\exists$ is called the existential quantiﬁer.

- **De Morgan’s Laws for Quantiﬁers:**

   | Negation              | Equivalent Statement  | When Is Negation True?                     | When False?                               |
   |-----------------------|-----------------------|--------------------------------------------|-------------------------------------------|
   | $\neg \exists x P(x)$ | $\forall x \neg P(x)$ | For every $x$, $P(x)$ is false.            | There is an $x$ for which $P(x)$ is true. |
   | $\neg \forall x P(x)$ | $\exists x \neg P(x)$ | There is an $x$ for which $P(x)$ is false. | $P(x)$ is true for every $x$.             |

## Inference

### Arguments

An argument in propositional logic is a sequence of propositions. All but the ﬁnal proposition in the argument are called premises and the ﬁnal proposition is called the conclusion. An argument is valid if the truth of all its premises implies that the conclusion is true.

An argument form in propositional logic is a sequence of compound propositions involving propositional variables. An argument form is valid if no matter which particular propositions are substituted for the propositional variables in its premises, the conclusion is true if the premises are all true.

<span dir="rtl">حاشیه: منظور همان استدلال کردن است، مثلا اگر الف و ب پس پ</span>

<span dir="rtl">حاشیه ۲: در حاشیه بالا الف و ب همان premises هستند و پ همان conclusion </span>

- **premises:** All but the ﬁnal proposition in the argument are called
- **conclusion:** the ﬁnal proposition is called the conclusion.
- **$\therefore$ symbol:** denotes "therefore"

### Rules of Inference

Rules of inference:

| Rule of Inference                                                                         | Tautology                                           | Name                   |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------|------------------------|
| $p$ <br> $p \to q$ <br> $\rule{2cm}{0.4pt}$ <br> $\therefore q$                     | $(p \land (p \to q)) \to q$                         | Modus ponens           |
| $\neg q$ <br> $p \to q$ <br> $\rule{2cm}{0.4pt}$ <br> $\therefore \neg p$           | $(\neg q \land (p \to q)) \to \neg p$               | Modus tollens          |
| $p \to q$ <br> $q \to r$ <br> $\rule{2cm}{0.4pt}$ <br> $\therefore p \to r$         | $((p \to q) \land (q \to r)) \to (p \to r)$         | Hypothetical syllogism |
| $p \lor q$ <br> $\neg p$ <br> $\rule{2cm}{0.4pt}$ <br> $\therefore q$               | $((p \lor q) \land \neg p) \to q$                   | Disjunctive syllogism  |
| $p$ <br> $\rule{2cm}{0.4pt}$ <br> $\therefore p \lor q$                             | $p \to (p \lor q)$                                  | Addition               |
| $p \land q$ <br> $\rule{2cm}{0.4pt}$ <br> $\therefore p$                            | $(p \land q) \to p$                                 | Simplification         |
| $p$ <br> $q$ <br> $\rule{2cm}{0.4pt}$ <br> $\therefore p \land q$                   | $((p) \land (q)) \to (p \land q)$                   | Conjunction            |
| $p \lor q$ <br> $\neg p \lor r$ <br> $\rule{2cm}{0.4pt}$ <br> $\therefore q \lor r$ | $((p \lor q) \land (\neg p \lor r)) \to (q \lor r)$ | Resolution             |

Rules of inference for quantified statements:

| Rule of Inference                                                                           | Name                       |
|---------------------------------------------------------------------------------------------|----------------------------|
| $\forall x P(x)$ <br> $\rule{2cm}{0.4pt}$ <br> $\therefore P(c)$                      | Universal instantiation    |
| $P(c)$ for an arbitrary $c$ <br> $\rule{2cm}{0.4pt}$ <br> $\therefore \forall x P(x)$ | Universal generalization   |
| $\exists x P(x)$ <br> $\rule{2cm}{0.4pt}$ <br> $\therefore P(c)$ for some element $c$ | Existential instantiation  |
| $P(c)$ for some element $c$ <br> $\rule{2cm}{0.4pt}$ <br> $\therefore \exists x P(x)$ | Existential generalization |
