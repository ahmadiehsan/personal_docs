# Circuit Breaker

## Description

A pattern used to handle failures in a microservice architecture.
When a microservice fails or becomes unresponsive the circuit breaker trips and redirects requests to a fallback service.

Prevents system-wide failures by halting requests to a failing or unresponsive service.
