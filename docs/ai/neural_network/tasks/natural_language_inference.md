# Natural Language Inference (NLI)

## Description

Natural Language Inference (NLI), also known as Recognizing Textual Entailment (RTE), is a core NLP task that determines the logical relationship between a pair of texts: a "premise" and a "hypothesis".

The goal is to classify the hypothesis as either **entailment (true), contradiction (false), or neutral (undetermined)** given the premise.

## Use Cases

- Question-answering systems
- Chatbots
- Sentiment analysis
- Machine translation
- Automating requirements analysis

## Workflow

- **Premise**: The given text or piece of information.
- **Hypothesis**: The statement that needs to be evaluated against the premise.
- **Classification**: An NLI model reads the premise and hypothesis and outputs one of three labels:

    - **Entailment**: The hypothesis is true given the premise.
    - **Contradiction**: The hypothesis is false given the premise.
    - **Neutral**: The hypothesis's truth value cannot be determined from the premise alone.

## Example

=== "Text"

    Premise: "A man is riding a bicycle."

    Hypothesis: "A person is riding a bike."

    Prediction: Entailment

=== "Code"

    ```python
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    import torch

    query = "What is the capital of France?"
    answer = "The capital of France is Paris. It is a global center for art, fashion, gastronomy, and culture."
    context = """
    Paris is the capital city of France. It is situated on the River Seine, in northern France.
    Paris has an area of 105 square kilometers and a population of over 2 million people.
    France is a country located in Western Europe.
    """

    model_name = "roberta-large-mnli"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    def calculate_claim_groundedness(context, claim):
        inputs = tokenizer(context, claim, truncation=True, return_tensors="pt")
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)
        entailment_prob = probs[0][2].item()  # Assuming label 2 corresponds to entailment
        return entailment_prob

    def calculate_groundedness(context, answer):
        """Calculates the overall groundedness score for the generated answer."""
        claims = answer.split(". ")  # Simple sentence splitting
        if not claims:
            return 0
        claim_scores = []
        for claim in claims:
            if claim:
                score = calculate_claim_groundedness(context, claim)
                claim_scores.append(score)
        return sum(claim_scores) / len(claim_scores) if claim_scores else 0

    groundedness_score = calculate_groundedness(context, answer)
    print(f"Groundedness Score: {groundedness_score:.3f}")
    ```
