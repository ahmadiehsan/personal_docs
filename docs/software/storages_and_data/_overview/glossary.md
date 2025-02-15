# Glossary

## Heterogeneous Systems

When no one database can do everything well, applications need to integrate several different databases, caches, indexes, and so on.

## Stream Processing

Send a message to another process, to be handled asynchronously

## Batch Processing

Periodically crunch a large amount of accumulated data

## Declarative Query Language

In a declarative query language, like SQL or relational algebra, you just specify the pattern of the data you want—what conditions the results must meet, and how you want the data to be transformed (e.g., sorted, grouped, and aggregated)—but not how to achieve that goal. It is up to the database system's query optimizer to decide which indexes and which join methods to use, and in which order to execute various parts of the query.

When SQL was defined, it followed the structure of the relational algebra fairly closely:

```sql
SELECT * FROM animals WHERE family = 'Sharks';
```

## Imperative Query Language

An imperative language tells the computer to perform certain operations in a certain order. You can imagine stepping through the code line by line, evaluating conditions, updating variables, and deciding whether to go around the loop one more time.

Many commonly used programming languages are imperative. For example, if you have a list of animal species, you might write something like this to return only the sharks in the list:

```javascript
function getSharks() {
  var sharks = [];
  for (var i = 0; i < animals.length; i++) {
    if (animals[i].family === "Sharks") {
      sharks.push(animals[i]);
    }
  }
  return sharks;
}
```
