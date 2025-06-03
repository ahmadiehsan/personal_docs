# Points

## Description

How we scale our system to support millions of users:

- Keep web tier stateless
- Build redundancy at every tier
- Cache data as much as you can
- Support multiple data centers
- Host static assets in CDN
- Scale your data tier by sharding
- Split tiers into individual services
- Monitor your system and use automation tools

<img src="image1.jpg" style="width:4.7198in" />

## One cache cluster to rule them all

Be careful not to have multiple services share the same cache cluster! Shared memory can cause one service to evict critical data of another, making issues harder to detect and debug.

## Queues are non-negotiable

Queues are essential. They give your system breathing room during traffic spikes and prevent services from being overwhelmed. They also help with autoscaling.

## Measuring end-to-end latency

Don’t forget to monitor async message latency. Dequeue latency (time a message waits before being processed) can significantly impact your total system latency.

## Design for failure

Failures will happen—network issues, rate limiting, downstream crashes. Plan for them. Use retries, circuit breakers, and dead-letter queues to handle failures gracefully.

## Design for idempotency

Duplicate messages are inevitable. Your consumers must be idempotent to avoid processing the same event multiple times (e.g., double charges, duplicate records).
