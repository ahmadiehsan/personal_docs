# Atomicity

## Description

This property ensures that a transaction is treated as a single, indivisible unit of work.
Either all the changes made by the transaction are committed to the database, or none of them are.
If any part of the transaction fails, the entire transaction is rolled back, and the database is left unchanged.
