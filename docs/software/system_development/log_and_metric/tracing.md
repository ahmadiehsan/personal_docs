# Tracing

## Description

- Tracing is usually request-scoped
- For example, a user request goes through the API gateway, load balancer, service A, service B, and database, which can be visualized in the tracing systems
- This is useful when we are trying to identify the bottlenecks in the system
- We use OpenTelemetry to showcase the typical architecture, which unifies the 3 pillars in a single framework
