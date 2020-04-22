# PostgreSQL

`sudo apt install postgresql`

## export/import

- import data to database from sql file:

  `pg_restore -d <db name> < <file_name.sql>`
  `psql ...`

- export data from database to sql file:

  `pg_dump -d <db name> > <file_name.sql>`
  `psql ...`

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

## temporarily disable all connections to table

`select oid from pg_class where relname='<table name>'`

## partial index

`CREATE [UNIQUE] INDEX <index name> ON <table> (<column A, column B>) WHERE <conditions>`

#### vertical show fields

`\x`

## postgres version

`SHOW server_version`

## run command by sudo

`sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"`