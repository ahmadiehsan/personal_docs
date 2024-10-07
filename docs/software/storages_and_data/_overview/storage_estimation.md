# Storage Estimation

## Overview

For example, we want to estimate Twitter QPS and storage requirements

Assumptions:

- 300 million monthly active users.
- 50% of users use Twitter daily.
- Users post 2 tweets per day on average.
- 10% of tweets contain media.
- Data is stored for 5 years.

Query per second (QPS) estimate:

- Daily active users (DAU) = 300 million * 50% = 150 million
- Tweets QPS = 150 million * 2 tweets / 24 hour / 3600 seconds = ~3500
- Peak QPS = 2 * QPS = ~7000

Estimate media storage:

- Average tweet size:

   - tweet\_id 64 bytes
   - text 140 bytes
   - media 1 MB

- Media storage: `150 million * 2 * 10% * 1 MB = 30 TB` per day
- 5-year media storage: `30 TB * 365 * 5 = ~55 PB`
