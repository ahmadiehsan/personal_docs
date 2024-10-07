# Vs (Single-Leader & Multi-Leader)

## Performance

In a single-leader configuration, every write must go over the internet to the data center with the leader. This can add significant latency to writes and might contravene the purpose of having multiple data centers in the first place. In a multi-leader configuration, every write can be processed in the local data center and is replicated asynchronously to the other data centers. Thus, the inter-datacenter network delay is hidden from users, which means the perceived performance may be better.

## Tolerance of Data Center Outages

In a single-leader configuration, if the data center with the leader fails, failover can promote a follower in another data center to be the leader. In a multi-leader configuration, each data center can continue operating independently of the others, and replication catches up when the failed data center comes back online.

## Tolerance of Network Problems

Traffic between data centers usually goes over the public internet, which may be less reliable than the local network within a data center. A single-leader configuration is very sensitive to problems in this inter-datacenter link because writes are made synchronously over this link. A multi-leader configuration with asynchronous replication can usually tolerate network problems better: a temporary network interruption does not prevent writes from being processed.
