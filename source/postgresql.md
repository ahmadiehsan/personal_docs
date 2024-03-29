# Postgresql

## Links

- [Peer Authentication Failed For User "Postgres"](https://stackoverflow.com/questions/8167602/django-connection-to-postgresql-peer-authentication-failed#answer-8232004)
- [Peer Authentication Failed For User "Postgres" V2](https://stackoverflow.com/questions/18664074/getting-error-peer-authentication-failed-for-user-postgres-when-trying-to-ge#answer-18664239)
- [Postgresql Data Types](https://www.tutorialspoint.com/postgresql/postgresql_data_types.htm)

## Connection Url

`postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]`

## Export/Import

- import data to database from sql file:

  `psql -d <db_name> -f <file_name.sql>`

- export data from database to sql file:

  `pg_dump -U <db_user> <db_name> > <file_name>.sql`
  
- insert to table from other table

  `INSERT INTO <table1> select * from <table2>`

## User

- show all users: `\du`

- create user: `CREATE USER <username>`

- drop user: `DROP USER <username>`

- change pass for any user:

  `ALTER USER <username> WITH PASSWORD '<new password>'`

## Database

- show all database: `\l`
- create db: `CREATE DATABASE <db name>`
- drop database: `DROP DATABASE <db name>`
- change db owner: `ALTER DATABASE <db name> OWNER TO <username>`
- connect to database: `\c <db name>`

## Tables

- show all of db tables: `\dt`

- show table schema: `\d+ <table name>`

- create table: `CREATE TABLE <table name>`

- create table based on other talbe:

  `CREATE TABLE <table name> (LIKE <other table name> INCLUDING ALL);`

- delete table: `DROP TABLE <table name>`

## Row

- updating row: `UPDATE <table name> SET <column A>=<value>`

- create row in table:

  `INSERT INTO <table name> (column A, column B) VALUES (value a, value b)`

- create row in table base on other table rows:

  `INSERT INTO <table name> SELECT * FROM <other table name>;`

- delete row in table:

  `DELETE FROM <table name> WHERE <column A>=<value>`

## Column

- create column in table:

  for creating new column need to temporarily disable all connections to table

  `ALTER TABLE <table name> ADD COLUMN <column name> <data type> [NOT NULL] [DEFAULT <value>]`
  
- show table column

  `select column_name, data_type from information_schema.columns where table_name = '<table name>'`

- make column nullable

  `ALTER TABLE <table name> ALTER COLUMN <column name> DROP NOT NULL`

- make column not nullable

  `ALTER TABLE <table name> ALTER COLUMN <column name> SET NOT NULL`

- update column value base other column

  `Update <table> SET <column one> = <column two>`

## Temporarily Disable All Connections To Table

`select oid from pg_class where relname='<table name>'`

## Partial Index

`CREATE [UNIQUE] INDEX <index name> ON <table> (<column A, column B>) WHERE <conditions>`

#### Vertical Show Fields

`\x`

## Postgres Version

`SHOW server_version`

## Change Sequence Number

`ALTER SEQUENCE <table>_id_seq RESTART WITH <number: 100>`

## Run Command By Sudo

`sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"`