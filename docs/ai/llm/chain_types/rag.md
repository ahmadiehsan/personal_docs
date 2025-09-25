# RAG

## Description

Retrieval Augmented Generation (RAG) enhances language model capabilities by integrating an information retrieval component with a text generator.
This combination enables models to access external knowledge sources, improving factual accuracy and reliability.

- **Dynamic Knowledge Access**: RAG allows models to adapt to new information without needing complete retraining.
- **Factual Consistency**: By leveraging external data, RAG reduces the chances of generating incorrect or "hallucinated" content.

## Varieties

=== "Naive (Standard)"

    ![](rag/naive_rag.jpg)

    Naive RAG is the simplest form of retrieval-augmented generation, where a language model retrieves documents based on the user's query and generates a response using the retrieved information.
    This approach typically relies on basic similarity search (such as vector embeddings or keyword matching) to find relevant passages, without incorporating advanced reasoning, feedback loops, or multi-hop retrieval.
    Naive RAG serves as a baseline for more sophisticated RAG frameworks, offering straightforward integration and fast response times.

    While effective for direct and well-specified queries, Naive RAG may struggle with ambiguous questions, complex reasoning, or scenarios requiring iterative refinement.
    It is best suited for applications where simplicity and speed are prioritized over depth and accuracy.

    Use cases include FAQ bots, basic document search, and situations where quick retrieval and generation are sufficient.

    !!! info

        <span dir="rtl">مناسب برای جستجوی ساده و پاسخ‌های سریع</span>

=== "Hybrid"

    ![](rag/hybrid_rag.jpg)

    Is a retrieval-augmented generation framework that combines multiple retrieval strategies—such as dense and sparse retrieval—to enhance the quality and relevance of information provided to language models.
    Unlike traditional RAG systems that rely on a single retrieval method, Hybrid RAG dynamically selects or fuses results from different retrieval approaches, leveraging their complementary strengths.

    This enables the model to access a broader and more diverse set of knowledge, improving accuracy, robustness, and adaptability across a wide range of tasks and domains.

=== "Graph"

    ![](rag/graph_rag.png)

    Is a retrieval-augmented generation framework that leverages graph-based structures to enhance information retrieval and reasoning.
    Unlike traditional RAG systems that operate in a linear fashion, Graph RAG organizes retrieved knowledge as interconnected nodes and edges, enabling the model to traverse, aggregate, and reason over complex relationships between pieces of information.

    This approach allows for more nuanced, multi-hop reasoning and supports workflows where understanding the connections between facts is crucial, making it especially effective for tasks requiring structured knowledge integration and advanced contextual understanding.

=== "Multimodal"

    ![](rag/multimodal_rag.jpg)

    Multimodal RAG is a retrieval-augmented generation framework that integrates multiple data modalities—such as text, images, audio, and video—into the retrieval and generation process.
    Unlike traditional RAG systems that focus solely on textual information, Multimodal RAG leverages embeddings and retrieval techniques across diverse formats, enabling richer and more contextually relevant responses.

    !!! info

        <span dir="rtl">مناسب برای ترکیب اطلاعات متنی و تصویری یا چندرسانه‌ای</span>

=== "Agentic"

    ![](rag/agentic_rag.png)

    Is an advanced retrieval-augmented generation framework that empowers language models with agent-like capabilities.
    Unlike standard RAG systems, Agentic RAG enables the model to autonomously plan, decide, and execute multiple retrieval and reasoning steps, adapting its strategy based on the evolving context and task requirements.
    This approach allows for more flexible, interactive, and goal-driven workflows, making it highly effective for complex problem-solving and dynamic information gathering.

=== "Corrective"

    ![](rag/corrective_rag.png)

    Is designed to refine and improve the outputs of language models by incorporating corrective feedback loops.
    Unlike standard RAG systems that generate responses based solely on initial retrievals, Corrective RAG iteratively evaluates and adjusts its answers, leveraging additional retrievals or user feedback to address inaccuracies or incomplete information.

    This approach enhances the reliability and precision of generated content, making it particularly suitable for scenarios where high accuracy and iterative improvement are essential.

    !!! info

        <span dir="rtl">مناسب جهت اصلاح و بهبود نتایج</span>

=== "Adaptive"

    ![](rag/adaptive_rag.png)

    Is an advanced framework that enhances language models by integrating dynamic retrieval and reasoning processes.
    Unlike traditional RAG systems that use a fixed number of retrieval steps, Adaptive RAG intelligently determines how many retrieval and generation cycles are needed based on the complexity of the task.

    This approach enables the model to efficiently handle multi-stage reasoning, adapt to diverse information needs, and provide more accurate and context-aware responses, making it especially effective for complex, multi-step workflows.

    !!! info

        <span dir="rtl">مناسب برای زنجیره‌های چندمرحله‌ای</span>

=== "Speculative"

    Speculative RAG is an approach that involves generating multiple possible responses or outputs for a given input query, using a retrieval model to provide relevant information.
    The generated responses are then evaluated using a feedback mechanism to select the most plausible or relevant one.
    The goal is to enhance the model's ability to produce accurate and contextually appropriate answers, especially when there is ambiguity or multiple potential interpretations of a query.

=== "Query Expansion"

    Query expansion (QE) is a technique in information retrieval (IR) that improves search engine performance by adding relevant terms to a user's initial query.
    This reformulation addresses the "vocabulary mismatch" problem, where users don't always use the exact words found in relevant documents.

    QE enhances search recall by retrieving documents that share similar meaning with the original query but might use different keywords, leading to more comprehensive results.

=== "Query Rewriting"

    Query rewriting is the process of transforming user queries to improve retrieval accuracy and performance, either by enhancing the query for a database or by generating multiple query variations for a search engine to improve information retrieval.

    This technique is used in both traditional database optimization and modern Retrieval-Augmented Generation (RAG) systems, where large language models (LLMs) rephrase vague questions, add keywords, and remove irrelevant details to better match document content, ultimately leading to more precise search results.

=== "HyDE"

    ![](rag/hyde.jpg)

    HyDE (Hypothetical Document Embeddings) is a retrieval-augmented generation framework that enhances language models by generating hypothetical answers to a query before retrieving supporting documents.
    Instead of directly searching for relevant passages, HyDE first prompts the model to create a plausible answer to the user's question.
    This hypothetical answer is then used as a query to retrieve documents that are semantically aligned with the generated response.
    By leveraging the model's generative capabilities to guide retrieval, HyDE can surface more contextually relevant information, especially in cases where the original query is ambiguous or under-specified.
    This approach is particularly effective for tasks requiring creative reasoning or when direct evidence is sparse, making it suitable for generating informed and context-aware responses.

    !!! info

        <span dir="rtl">مناسب برای تولید پاسخ‌های فرضی</span>

## Workflow

=== "Naive (Standard)"

    - **Step 1 - Query Input**: A user query or input is provided to the retrieval component of the system.
    - **Step 2 - Retrieval Process**: The retriever searches a large corpus or database for documents or text passages that are most relevant to the query. This is often done using vector search or dense retrieval methods, where both the query and documents are encoded into high-dimensional vectors.
    - **Step 3 - Selection of Top Documents**: The retriever ranks the documents based on their relevance to the query and selects the top-k documents (e.g., the top 5 most relevant passages).
    - **Step 4 - Generative Response**: The selected documents are then passed to the generative model (like GPT). The model uses this context to generate a coherent response that directly answers the query while incorporating the retrieved information.
    - **Step 5 - Output**: The final response is presented to the user, leveraging the retrieved content to enhance accuracy and detail.

=== "Corrective"

    - **Step 1 - Initial Retrieval and Generation**: The process begins like Standard RAG, where the retriever fetches relevant information and the generative model creates a response.
    - **Step 2 - Validation Process**: The generated response is then validated against a trusted dataset or source. This could involve comparing the generated content with data from authoritative sources (like medical databases, academic papers, or trusted news outlets).
    - **Step 3 - Correction Mechanism**: If discrepancies or errors are detected during validation, the model uses the feedback to correct the response. This might involve generating a new response or refining the existing one.
    - **Step 4 - Iteration and Feedback Loop**: The system iterates this process, continuously refining the response until it aligns with the correct information or falls within an acceptable error margin.
    - **Step 5 - Final Output**: The validated and corrected response is provided to the user.

=== "Speculative"

    - **Step 1 - Retrieval**: Similar to Standard RAG, it starts by retrieving multiple documents relevant to the query.
    - **Step 2 - Generative Speculation**: The generative model creates multiple speculative responses based on the retrieved documents. Instead of producing a single answer, it explores several possible outputs.
    - **Step 3 - Feedback and Ranking**: Each of the generated responses is evaluated using a feedback mechanism that scores them based on various criteria like relevance, coherence, completeness, and factual accuracy. This could involve comparing the responses against additional retrieved documents or using scoring models.
    - **Step 4 - Selection Process**: The model ranks all possible responses and selects the highest-scoring one as the final output.
    - **Step 5 - Presentation**: The chosen response is then presented to the user as the final answer.
