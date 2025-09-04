# Naive RAG [RAG]

## Description

![](naive_rag/diagram.jpg)

Naive RAG is the simplest form of retrieval-augmented generation, where a language model retrieves documents based on the user's query and generates a response using the retrieved information.
This approach typically relies on basic similarity search (such as vector embeddings or keyword matching) to find relevant passages, without incorporating advanced reasoning, feedback loops, or multi-hop retrieval.
Naive RAG serves as a baseline for more sophisticated RAG frameworks, offering straightforward integration and fast response times.

While effective for direct and well-specified queries, Naive RAG may struggle with ambiguous questions, complex reasoning, or scenarios requiring iterative refinement.
It is best suited for applications where simplicity and speed are prioritized over depth and accuracy.

Use cases include FAQ bots, basic document search, and situations where quick retrieval and generation are sufficient.

!!! info

    <span dir="rtl">مناسب برای جستجوی ساده و پاسخ‌های سریع</span>
