# DSL (Query Clauses)

## Leaf

look for a particular value in a particular field, such as the **match**, **term**, or **range** queries. These queries can be used by themselves.

Popular ones:

- **match**: field contains the word (accepts typo if we use *fuzziness* option in it)
- **multi_match**: multiple fields contain the word
- **query_string**: supports Lucene syntax to interpret the text (Query string is therefore far more powerful than **match** and **multi_match**, but it can also lead to unexpected scenarios, such as where / may cause part of the string to be interpreted as a regular expression)
- **match_phrase**: field contains the phrase
- **term**: field contains the exact phrase
- **range**: field contains a range

## Compound

Compound query clauses wrap other leaf or compound queries. They are used to combine multiple queries logically (such as the **bool** or **dis_max** query) or to alter their behavior (such as the **constant_score** query).

Popular ones:

- **bool**: a query that matches documents matching boolean combinations of other queries. (*must*, *filter*, *should*, and *must_not* are its subqueries)
- **boosting**: returns documents matching a positive query while reducing the relevance score of documents that also match a negative query. (*positive*, and *negative* are its subqueries)
- **constant_score**: wraps a filter query and returns every matching document with a relevance score equal to the boost parameter value. (*filter* is its subquery)
- **dis_max**: returns documents matching one or more wrapped queries. if a returned document matches multiple query clauses, the dis_max query assigns the document the highest relevance score from any matching clause. (*queries* is its subquery)
