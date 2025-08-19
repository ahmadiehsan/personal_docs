# Mapping

## Dynamic/Explicit Field Mapping

- **Dynamic**: Elasticsearch dynamically adds the field to the type mapping by default when it detects a new field in a document.
- **Explicit**: Explicitly defining all possible fields in an index and their types

## Normalizer

A normalizer in Elasticsearch ensures consistent indexing and searching for exact matching in fields.
It preprocesses text, making it suitable for scenarios like case-insensitive sorting and aggregations.

- It produces only **one output**
- It **doesn't change** the main value in the document
- For the **aggregations**, ES uses the result of it
- Use normalizers with **keyword** fields for exact matching
- Avoid normalizers for **text** fields, as normalizers are designed for keyword fields

Elasticsearch doesn't apply a default normalizer for **keyword** fields if none is specified.
If you don't explicitly define a normalizer for a **keyword** field, it essentially means that no normalization will be applied, and the exact values will be indexed as they are.

## Analyzer

An analyzer defines how text fields are processed during indexing and searching, allowing customization for language-specific stemming, synonym handling, and other transformations.

- It produces **multiple outputs**
- It **doesn't change** the main value in the document
- For the **search**, ES uses the results of it
- Apply analyzers to **text** fields for language-specific processing
- Choose analyzers based on your language and search requirements

If you don't specify an analyzer for a **text** field in Elasticsearch, the default analyzer applied is typically the "**standard**" analyzer.
The "standard" analyzer is a good general-purpose choice and includes tokenization, lowercasing, and removal of stop words.
