# DSL (Query Contexts)

## Query

In the query context, a query clause answers the question “How well does this document match this query clause?” Besides deciding whether or not the document matches, the query clause also calculates a relevance score in the _score metadata field.

Query context is in effect whenever a query clause is passed to a query parameter, such as:

- The **query** parameter in the search API.

  !!! info

      Use query clauses in query context for conditions which should affect the score of matching documents (i.e. how well does the document match), and use all other query clauses in filter context.

## Filter

In a filter context, a query clause answers the question “**Does this document match this query clause?**” The answer is a simple Yes or No — no scores are calculated. Filter context is mainly used for filtering structured data, e.g.

- Does this timestamp fall into the range of 2015 to 2016?
- Is the status field set to "published"?

Frequently used filters will be cached automatically by Elasticsearch, to speed up performance.

Filter context is in effect whenever a query clause is passed to a filter parameter, such as:

- The **filter** or **must_not** parameters in the **bool** query
- The **filter** parameter in the **constant_score** query
- The **filter** in the **aggregation**.

## Aggregation

An aggregation summarizes your data as metrics, statistics, or other analytics. Aggregations help you answer questions like:

- What's the average load time for my website?
- Who are my most valuable customers based on transaction volume?
- What would be considered a large file on my network?
- How many products are in each product category?

You can run aggregations as part of a search by specifying the search API's **aggs** parameter.

Elasticsearch organizes aggregations into three categories:

- **Metric** aggregations that calculate metrics, such as a sum or average, from field values.
- **Bucket** aggregations that group documents into buckets also called bins, based on field values, ranges, or other criteria.
- **Pipeline** aggregations that take input from other aggregations instead of documents or fields.
