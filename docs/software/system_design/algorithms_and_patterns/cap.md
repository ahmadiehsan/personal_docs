# CAP Theorem

## Description

When designing distributed systems, engineers must often make trade-offs between three core properties: **Consistency**, **Availability**, and **Partition Tolerance**.
This balance is formalized in the **CAP Theorem**, which helps guide architectural decisions in real-world scenarios.

The CAP Theorem, introduced by Eric Brewer, states that a distributed system can satisfy only **two** out of the following **three guarantees**:

1. Consistency (C): Every read receives the most recent write. All nodes see the same data at the same time.
2. Availability (A): Every request receives a response (non-error), even if some of the nodes are down.
3. Partition Tolerance (P): The system continues to operate despite arbitrary network failures that prevent communication between nodes.

## Why Can't We Have All Three

In a distributed environment, network partitions are a fact of life—hardware fails, packets drop, links go down.
Once a partition occurs, you must choose between:

- **Consistency**: Reject requests that can't guarantee the latest state.
- **Availability**: Serve stale or partial data to keep the system responsive.

Hence, you can only reliably achieve two of the three properties **at the same time**.

## CP vs AP Systems

CP Systems (Consistency + Partition Tolerance):

- Prioritize correctness over availability.
- System may reject requests when partitioned.
- Examples: Traditional RDBMS with strong replication, HBase, MongoDB (in certain configs).

AP Systems (Availability + Partition Tolerance)

- Prioritize uptime and responsiveness.
- May return stale or eventually consistent data.
- Examples: Cassandra, DynamoDB, Couchbase.
