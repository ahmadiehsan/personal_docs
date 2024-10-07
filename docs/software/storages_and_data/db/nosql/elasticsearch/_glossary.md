# Glossary

## Document

- A record of one entity

## Type

- Table of documents
- it has been removed from V8 and we should create a separate index for each type

## Index (Indices)

- Database of tables

## Alias

- An alternative name for an index
- Multiple indices can have the same alias

## Engine

- A facade over the ingested documents inside an index

## Content Sources

- Connector for reading data from 3rd party sources like Google Drive and Dropbox

## Mapping

- Mapping is the process of defining how a document, and the fields it contains, are stored and indexed.

## Field

- Each document is a collection of fields

## Metadata Field

- Each document has metadata associated with it, such as the \_index and \_id
- List of metadata fields: [Link](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-fields.html)

## Data Type

- Each field has its data type
- While **text** fields work well for full-text searches, **keyword** fields are not analyzed and may work better for sorting or aggregations.
- List of data types: [Link](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-types.html)
