# PostgreSQL

`sudo apt install postgresql`

## export/import

- import data to database from sql file:

  `psql -d <db name> -f <file_name.sql>`

- export data from database to sql file:

  `pg_dump --no-owner -d <database_name> -t <table_name> > <file_name>.sql`
  
- insert to table from other table

  `INSERT INTO <table1> select * from <table2>`

## user

- show all users: `\du`

- create user: `CREATE USER <username>`

- drop user: `DROP USER <username>`

- change current user password: `\password`

- change pass for any user:

  `ALTER USER <username> WITH PASSWORD '<new password>'`

## database

- show all database: `\l`
- create db: `CREATE DATABASE <db name>`
- drop database: `DROP DATABASE <db name>`
- change db owner: `ALTER DATABASE <db name> OWNER TO <username>`
- connect to database: `\c <db name>`

## tables

- show all of db tables: `\dt`

- show table schema: `\d+ <table name>`

- create table: `CREATE TABLE <table name>`

- create table based on other talbe:

  `CREATE TABLE <table name> (LIKE <other table name> INCLUDING ALL);`

- delete table: `DROP TABLE <table name>`

## row

- updating row: `UPDATE <table name> SET <column A>=<value>`

- create row in table:

  `INSERT INTO <table name> (column A, column B) VALUES (value a, value b)`

- create row in table base on other table rows:

  `INSERT INTO <table name> SELECT * FROM <other table name>;`

- delete row in table:

  `DELETE FROM <table name> WHERE <column A>=<value>`

## column

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

## temporarily disable all connections to table

`select oid from pg_class where relname='<table name>'`

## partial index

`CREATE [UNIQUE] INDEX <index name> ON <table> (<column A, column B>) WHERE <conditions>`

#### vertical show fields

`\x`

## postgres version

`SHOW server_version`

## Change sequence number

`ALTER SEQUENCE <table>_id_seq RESTART WITH <number: 100>`

## run command by sudo

`sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"`