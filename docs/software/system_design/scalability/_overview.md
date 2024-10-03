# _Overview

## Description

As the system grows (in data volume, traffic volume, or complexity), there should be reasonable ways of dealing with that growth

## What is Load

Load can be described with a few numbers which we call load parameters. The best choice of parameters depends on the architecture of your system: it may be the number of requests per second to a web server, the ratio of reads to writes in a database, the number of simultaneously active users in a chat room, the hit rate on a cache, or something else.

## Latency and Response Time

Latency and response time are often used synonymously, but they are not the same. The response time is what the client sees: besides the actual time to process the request (the service time), it includes network delays and queueing delays. Latency is the duration that a request is waiting to be handled—during which it is latent, awaiting service

Percentiles are often used in service level objectives (SLOs) and service level agreements (SLAs), contracts that define the expected performance and availability of a service. An SLA may state that the service is considered to be up if it has a median (50th percentile) response time of less than 200 ms and a 99th percentile under 1s (if the response time is longer, it might as well be down), and the service may be required to be up at least 99.9% of the time.
