# Approach: Multi-Leader Replication

## Description

Leader-based replication has one major downside: there is only one leader, and all writers must go through it.
If you can't connect to the leader for any reason, for example, due to a network interruption between you and the leader, you can't write to the database.

A natural extension of the leader-based replication (**Multi-Leader Replication**) model is to allow **more than one node to accept writes**.
Replication still happens in the same way: each node that processes a write must forward that data change to all the other nodes.

<img src="image2.png" style="width:600px" />

As multi-leader replication is a somewhat retrofitted feature in many databases, there are often subtle configuration pitfalls and surprising interactions with other database features.
For example, auto-incrementing keys, triggers, and integrity constraints can be problematic.
**For this reason, multi-leader replication is often considered dangerous territory that should be avoided if possible.**

## Conflict Resolution

Although multi-leader replication has advantages, it also has a big downside: the same data may be concurrently modified in two different data centers, and those write conflicts must be resolved (indicated as "conflict resolution" in the above picture)

<img src="image1.png" style="width:688px" />
