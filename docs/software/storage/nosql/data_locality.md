# Data Locality

## Description

Data locality refers to the proximity or closeness of data elements that are accessed together in a computer system.
The principle of data locality is essential for optimizing the performance and efficiency of various computing processes, particularly in the context of storage and memory access.
The idea is to minimize the time and resources required to access data by keeping related data physically close to each other.

## Practical View

A document is usually stored as a single continuous string, encoded as JSON, XML, or a binary variant thereof (such as MongoDB's BSON).
If your application often needs to access the entire document (for example, to render it on a web page), there is a performance advantage to this storage locality.
If data is split across multiple tables, multiple index lookups are required to retrieve it all, which may require more disk seeks and take more time.

## Disadvantages

The locality advantage only applies if you need large parts of the document at the same time.
The database typically needs to load the entire document, even if you access only a small portion of it, which can be wasteful on large documents.
On updates to a document, the entire document usually needs to be rewritten—only modifications that don't change the encoded size of a document can easily be performed in place.
For these reasons, it is generally recommended that you keep documents fairly small and avoid writes that increase the size of a document.
These performance limitations significantly reduce the set of situations in which document databases are useful.
