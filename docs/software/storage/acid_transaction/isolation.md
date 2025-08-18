# Isolation

## Description

Isolation means that a transaction should take place in a system in such a way that it is the only transaction that is accessing the resources in a database system.

Database isolation defines the degree to which a transaction must be isolated from the data modifications made by any other transaction(even though in reality there can be a large number of concurrently running transactions).
The overarching goal is to prevent reads and writes of temporary, aborted, or otherwise incorrect data written by concurrent transactions.

## Transaction isolation level is defined by the following phenomena

### Dirty Reads

A transaction reads data written by a concurrent uncommitted transaction. (uncommitted data is called "dirty.")

<img src="image10.png" style="width:3.10947in" />

For example, Let's say transaction 1 updates a row and leaves it uncommitted, meanwhile, Transaction 2 reads the updated row. If transaction 1 rolls back the change, transaction 2 will have read data that is considered never to have existed.

### Non-Repeatable Reads, and Read Skew

A transaction re-reads data it has previously read and finds that data has been modified by another transaction (that has been committed since the initial read).

Note that this differs from a dirty read in that the other transaction has been committed.
Also, this phenomenon requires two reads to manifest.

<img src="image3.png" style="width:3.23884in" />

For example, suppose transaction T1 reads data.
Due to concurrency, another transaction T2 updates the same data and commits, now if transaction T1 rereads the same data, it will retrieve a different value

### Phantom Reads

A transaction re-executes a query returning a set of rows that satisfy a search condition and finds that the set of rows satisfying the condition has changed due to another recently committed transaction.

This is similar to a non-repeatable read except it involves a changing collection matching a predicate rather than a single item.

<img src="image5.png" style="width:3.15202in" />

For example, suppose transaction T1 retrieves a set of rows that satisfy some search criteria.
Now, Transaction T2 generates some new rows that match the search criteria for Transaction T1.
If transaction T1 re-executes the statement that reads the rows, it gets a different set of rows this time.

### Serialization Anomaly (Write Skew)

Two concurrent transactions each determine what they are writing based on reading a data set that overlaps what the other is writing.

<img src="image9.png" style="width:3.1745in" />

For example, suppose 2 transactions read that x and y have the value of 100, so individually it's fine for each transaction to negate one of the values, the total would still be non-negative. However negating both values results in x+y=-200, violating the constraint. For emotional gravity, this is usually framed in terms of bank accounts where account balances are allowed to go negative as long as the sum of commonly held balances remains non-negative.

## Based on these phenomena, These isolation levels have been defined

### Read Uncommitted

<img src="image7.png" style="width:3.86352in" />

Read Uncommitted is the lowest isolation level.
At this level, make sure **no transaction can update a database row if another transaction has already been updated and not committed.** This protects against lost updates, but won't stand in the way of dirty reads.

### Read Committed

<img src="image2.png" style="width:3.66447in" />

This isolation level **does not allow any other transaction to write or read a row to which another transaction has written to but not yet committed.** Thus it does not allow dirty read.
The transaction holds a read or write lock on the current row, and thus prevents other transactions from reading, updating, or deleting it.

### Repeatable Read

<img src="image1.png" style="width:3.14166in" />

This isolation level makes sure any **transaction that reads data from a row blocks any other writing transactions from accessing the same row.** This is the most restrictive isolation level that holds read locks on all rows it references and writes locks on all rows it inserts, updates, or deletes.
Since other transactions cannot read, update, or delete these rows, consequently it avoids non-repeatable reading.

### Serializable

<img src="image4.png" style="width:5.11096in" />

This isolation level is the highest. serializable isolation level requires a lot more than restricting access to a single row.
Typically this isolation mode would **lock the whole table**, to prevent any other transactions from inserting or reading data from it.

Serializable execution is defined to be an execution of operations in which concurrently executing transactions appear to be serially executing.

### Snapshot Isolation

<img src="image6.png" style="width:4.75565in" />

This isolation level can greatly increase concurrency at a lower cost than transactional isolation.
When data is modified, the committed versions of affected rows are copied to temp and given version numbers.
This operation is called copy-on-write and is used for all inserts, updates, and deletes using this technique.
When another session reads the same data, the committed version of the data as of the time the reading transaction began is returned.

## Which transaction isolation to choose

| Isolation level      | Dirty read | Nonrepeatable read | Phantom |
|----------------------|------------|--------------------|---------|
| **Read uncommitted** | Yes        | Yes                | Yes     |
| **Read committed**   | No         | Yes                | Yes     |
| **Repeatable read**  | No         | No                 | Yes     |
| **Snapshot**         | No         | No                 | No      |
| **Serializable**     | No         | No                 | No      |

The choice of transaction isolation level depends on the details of each specific case.
These hints may be helpful, but please consider each situation individually.

When designing your application, you want to ensure that none of your database transactions read uncommitted changes of other transactions.

because changes can easily harm your data integrity, as reverted changes in one transaction can be read and potentially accepted by another.
The minimum isolation level to ensure in your application, therefore, is Read Committed.

Most of the time you probably don't need Serializable isolation, as it can cause big performance issues with a large volume of concurrent transactions.

so it's always depends on your business requirements
