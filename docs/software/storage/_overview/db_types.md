# DB Types

## Log-Oriented Databases

- Focus on storing data in an append-only log structure.
- Data is sequentially written to a log file, making writing efficient.
- Well-suited for scenarios where write performance is critical, such as logging or event sourcing.
- Retrieving specific records might require scanning the entire log.

## Page-Oriented Databases

- Organize data into pages or blocks, allowing for random access.
- Commonly used in traditional relational databases.
- Efficient for read-heavy workloads, as specific pages can be targeted.
- Updates and deletes may involve more overhead due to the need to manage pages efficiently.
