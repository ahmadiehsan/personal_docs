# Transformers [NLP]

## Description

Transformers rely on a mechanism called self-attention, which allows the model to weigh the importance of different parts of the input data dynamically.
This enables efficient parallelization and handling of long-range dependencies more effectively than previous models, such as RNNs and LSTMs.

![](transformers/image1.jpg)

## Workflow

Encoder Part:

```text
Token Encodings = (One Hot Encodings . Token Embeddings) + Position Encodings

Query = Token Encodings . Query Weights
Key   = Token Encodings . Key Weights
Value = Token Encodings . Value Weights

Token Similarities    = Query . Key
Self Attention Scores = Tokens Similarities . Value

Encoder Part Output = Self Attention Scores + Token Encodings
```

Decoder Part:

```text
Token Encodings = (One Hot Encodings . Token Embeddings) + Position Encodings

Query = Token Encodings . Query Weights
Key   = Token Encodings . Key Weights
Value = Token Encodings . Value Weights

Token Similarities    = (Query . Key) + Next Tokens Mask
Self Attention Scores = Tokens Similarities . Value

Decoder Part Output = Self Attention Scores + Token Encodings
```

Encoder-Decoder Part:

```text
Query = Decoder Part Output . Query Weights
Key   = Encoder Part Output . Key Weights
Value = Encoder Part Output . Value Weights

Token Similarities               = Query . Key
Encoder-Decoder Attention Scores = Tokens Similarities . Value

Encoder-Decoder Part Output = Encoder-Decoder Attention Scores + Decoder Part Output

Fully Connected Layer Output = (Encoder-Decoder Part Output . Fully Connected Layer Weights) + Fully Connected Layer Bias
Next Token Probabilities     = SoftMax(Fully Connected Layer Output)
```

## Components

=== "Self-Attention"

    Self-Attention: The core mechanism that allows transformers to weigh the importance of different words in a sentence relative to each other.
    Each word attends to all other words in the sentence to gather context.

    Scaled Dot-Product Attention: This involves three matrices - Query (Q), Key (K), and Value (V).
    The attention scores are calculated as the dot product of the query and key vectors, scaled, and passed through a softmax function to get weights.
    These weights are then used to combine the value vectors.

=== "Multi-Head Attention"

    Instead of performing a single attention function, the model runs multiple attention mechanisms (heads) in parallel.
    Each head focuses on different parts of the sentence, capturing various aspects of the relationships between words.

=== "Feed-Forward NN"

    After the attention mechanism, the output is passed through a position-wise fully connected feed-forward network, which is the same for each position.

=== "Positional Encoding"

    Since transformers do not have a sequential nature like RNNs, they need some way to capture the order of words.
    Positional encodings are added to the input embeddings to give the model information about the position of each word in the sequence.

=== "Layer Normalization and Residual Connections"

    Each sub-layer (attention and feed-forward) is followed by a layer normalization and a residual connection to ensure stability during training.

## Types

=== "Decoder-Only"

    Generative Models (Decoder-Only) models are a class of transformer architectures designed primarily for generating sequential data.
    They are often referred to as **autoregressive models**, as they predict the next token in a sequence based on previous tokens.
    This makes them well-suited for tasks like text generation, language modeling, and code autocompletion.

    - One of the most popular examples of decoder-only models is **GPT (Generative Pre-trained Transformer)**, which has revolutionized the field of Natural Language Processing (NLP).
    - The **decoder-only architecture** is based on the transformer block but contains a few key differences compared to encoder-decoder or encoder-only models:
    - It **does not use an encoder**; instead, it processes input sequences directly in the decoder.
    - It utilizes **masked self-attention** to prevent the model from "seeing" future tokens during training. This ensures that predictions are made based solely on past information.
    - Decoder-only models predict one token at a time. For each step, they generate the next token in the sequence by conditioning on all previous tokens.
    - These models process information from left to right (in natural language). As a result, they are unable to consider future tokens during generation.

    Applications:

    - **Text Generation**: Produce coherent and contextually relevant text (e.g., ChatGPT).
    - **Dialogue Systems**: Power conversational agents like chatbots.
    - **Code Generation**: Support use cases like autocompletion for programming (e.g., OpenAI Codex).
    - **Creative Content**: Generate poems, stories, or other creative writing.
    - **Autoregressive Language Modeling**: Model language distributions effectively for downstream tasks.

=== "Encoder-Only"

    Representation Models (Encoder-Only) models are transformer architectures tailored for learning rich representations of input sequences.
    These models focus on understanding and encoding the input into highly contextualized embeddings, making them ideal for tasks that require comprehension but not generation.

    - One of the most well-known examples of encoder-only models is **BERT (Bidirectional Encoder Representations from Transformers)**, which introduced the concept of bidirectional contextual understanding to NLP.
    - The **encoder-only architecture** processes the entire input sequence at once using bidirectional self-attention. This allows the model to capture dependencies between tokens in both directions (left-to-right and right-to-left).
    - Encoder-only models consider the entire input simultaneously, leveraging left and right context for richer representations.
    - These models do not predict one token at a time but instead encode the whole sequence into meaningful vectors in one step.

    Applications:

    - **Text Classification**: Sentiment analysis, topic categorization, etc.
    - **Named Entity Recognition (NER)**: Identify entities like names, locations, and dates in text.
    - **Question Answering (QA)**: Extract answers from passages of text.
    - **Semantic Search**: Encode sentences to enable semantic similarity matching.
    - **Coreference Resolution**: Resolve pronouns to their corresponding entities in a document.

=== "Encoder-Decoder"

    Sequence-to-Sequence Models (Encoder-Decoder) models, also known as **sequence-to-sequence (seq2seq) architectures**, are a type of transformer designed for mapping one sequence to another.
    The architecture consists of two separate components: an **encoder** to process and understand the input sequence, and a **decoder** to generate the output sequence.

    - Examples of encoder-decoder-based transformers include **T5 (Text-to-Text Transfer Transformer)**, **BART (Bidirectional and Auto-Regressive Transformers)**, and **mT5 (multilingual T5)**.
    - The encoder-decoder architecture can be visualized as two connected transformers:

       - **Encoder**: Reads and processes the input sequence, generating a latent representation of the input.
       - **Decoder**: Consumes the encoder's latent representation while generating the output sequence autoregressively (one token at a time).

    - Uses bidirectional self-attention to produce contextualized representations of the input sequence.
    - Captures holistic meaning by attending to relations between tokens in the input.
    - Combines autoregressive decoding with encoder cross-attention to generate target tokens.
    - Uses both its own generated tokens (from self-attention) and the encoder's processed information (via encoder-decoder cross-attention).
    - Both encoder and decoder embed input tokens and enrich them with positional information.
    - The decoder uses cross-attention mechanisms to attend to the encoder's output representations, ensuring that the generated output remains aligned with the input sequence.

    Applications:

    - **Machine Translation**: Translate from one language to another.
    - **Text Summarization**: Generate concise summaries of long documents or articles.
    - **Text Generation with Context**: Generate output conditioned on input (e.g., rewriting text, question generation).
    - **Question Answering (QA)**: Provide a textual answer to a question given relevant contexts.
    - **Closed-Ended Transformation Tasks**:

       - Data-to-text generation (e.g., converting tables into sentences).
       - Grammar correction (e.g., fixing spelling and grammatical errors).
       - Format transformation (e.g., converting JSON to text).
