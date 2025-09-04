# Corrective RAG [RAG]

## Description

![](corrective_rag/diagram.png)

Is designed to refine and improve the outputs of language models by incorporating corrective feedback loops.
Unlike standard RAG systems that generate responses based solely on initial retrievals, Corrective RAG iteratively evaluates and adjusts its answers, leveraging additional retrievals or user feedback to address inaccuracies or incomplete information.

This approach enhances the reliability and precision of generated content, making it particularly suitable for scenarios where high accuracy and iterative improvement are essential.

!!! info

    <span dir="rtl">مناسب جهت اصلاح و بهبود نتایج</span>

## Workflow

- **Step 1 - Initial Retrieval and Generation**: The process begins like Standard RAG, where the retriever fetches relevant information and the generative model creates a response.
- **Step 2 - Validation Process**: The generated response is then validated against a trusted dataset or source. This could involve comparing the generated content with data from authoritative sources (like medical databases, academic papers, or trusted news outlets).
- **Step 3 - Correction Mechanism**: If discrepancies or errors are detected during validation, the model uses the feedback to correct the response. This might involve generating a new response or refining the existing one.
- **Step 4 - Iteration and Feedback Loop**: The system iterates this process, continuously refining the response until it aligns with the correct information or falls within an acceptable error margin.
- **Step 5 - Final Output**: The validated and corrected response is provided to the user.
