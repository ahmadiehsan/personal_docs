# Data Mart

## Description

A data mart is a subset of a data warehouse. It's designed to cater to the needs of a specific business unit or team. Think of it as a department store within the larger shopping mall (the data warehouse).

Specifications:

- A mechanism through which business users access data that lives in a data warehouse
- Is a subset of a data warehouse

Types:

- Independent Data Mart

   - Functions without relying on an existing data warehouse

   - Focuses on one specific business objective

   - Data is stored from either internal or external sources

- Dependent Data Mart

   - lives on top of an existing data warehouse

   - data lives in a centralized location and when it's time to run analytics, only the relevant data is accessed

- Hybrid Data Mart

   - integrates data from external operational sources with an existing data warehouse

   - higher speed, flexibility, and capacity to handle large storage structures
