# Importance Sampling

## Description

Importance sampling is one of the most important sampling methods. It allows us to sample from a distribution when we only have access to another distribution.

For example, we want to sample from a distribution P(x), but can't access it. However, we can access another distribution Q(x). **The following equation shows that, in expectation, x sampled from P(x) equals to x sampled from Q(x) weighted by P(x)/Q(x).**

Therefore, **instead of sampling from P(x), we can alternatively sample from Q(x) which is accessible, and weight the sampled results by P(x)/Q(x).** The results are the same as we directly sample from P(x).
