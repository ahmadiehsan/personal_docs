# Metrics

## Description

- Metrics are usually aggregatable information from the system
- For example, service QPS, API responsiveness, service latency, etc
- The raw data is recorded in time-series databases like InfluxDB
- Prometheus pulls the data and transforms the data based on predefined alerting rules. Then the data is sent to Grafana for display or to the alert manager which then sends out email, SMS, or Slack notifications or alerts
