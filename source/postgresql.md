# Postgresql

## Links

- [Peer Authentication Failed For User "Postgres"](https://stackoverflow.com/questions/8167602/django-connection-to-postgresql-peer-authentication-failed#answer-8232004)
- [Peer Authentication Failed For User "Postgres" V2](https://stackoverflow.com/questions/18664074/getting-error-peer-authentication-failed-for-user-postgres-when-trying-to-ge#answer-18664239)
- [Postgresql Data Types](https://www.tutorialspoint.com/postgresql/postgresql_data_types.htm)

## Data Types

- Numeric:

  | Data Type        | Range                                                        | Storage size |
  | ---------------- | ------------------------------------------------------------ | ------------ |
  | SMALLINT         | -32,768 to +32,767                                           | 2 bytes      |
  | INTEGER          | -2,147,483,648 to +2,147,483,647                             | 4 bytes      |
  | BIGINT           | -9,223,372,036,854,775,808 to +9,223,372,036,854,775,807     | 8 bytes      |
  | DECIMAL          | Up to 131,072 digits before the decimal point; up to 16,383 digits after the decimal point | Variable     |
  | NUMERIC          | Up to 131,072 digits before the decimal point; up to 16,383 digits after the decimal point | Variable     |
  | REAL             | Approx. ±1.7E–308 to ±1.7E+308 (6 decimal digits precision)  | 4 bytes      |
  | DOUBLE PRECISION | Approx. ±1.7E–308 to ±1.7E+308 (15 decimal digits precision) | 8 bytes      |
  | SMALLSERIAL      | 1 to 32,767                                                  | 2 bytes      |
  | SERIAL           | 1 to 2,147,483,647                                           | 4 bytes      |
  | BIGSERIAL        | 1 to 9,223,372,036,854,775,807                               | 8 bytes      |

## Export/Import

- Import data to database from sql file:

  ```
  psql -d <db_name> -f <file_name.sql>
  ```

- Export data from database to sql file:

  ```
  pg_dump -U <db_user> <db_name> > <file_name>.sql
  ```
  
- Insert to table from other table:

  ```
  INSERT INTO <table1> select * from <table2>
  ```

## Shell

- Connect:

  ```
  psql
  ```

- Run command by sudo:

  ```
  sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"
  ```

- Vertical show fields:

  ```
  \x
  ```

## User

- Show all users:

  ```
  \du
  ```

- Create user:

  ```
  CREATE USER <username>
  ```

- Drop user:

  ```
  DROP USER <username>
  ```

- Change pass for any user:

  ```
  ALTER USER <username> WITH PASSWORD '<new_password>'
  ```

## Database

- Show all database:

  ```
  \l
  ```
- Create db:

  ```
  CREATE DATABASE <db_name>
  ```
- Drop database:

  ```
  DROP DATABASE <db_name>
  ```
- Change db owner:

  ```
  ALTER DATABASE <db_name> OWNER TO <username>
  ```
- Connect to database:

  ```
  \c <db_name>
  ```

## Tables

- Show all of db tables:

  ```
  \dt
  ```

- Show table schema:

  ```
  \d+ <table_name>
  ```

- Create table:

  ```
  CREATE TABLE <table_name>
  ```

- Create table based on other talbe:

  ```
  CREATE TABLE <table_name> (LIKE <other_table_name> INCLUDING ALL);
  ```

- Delete table:

  ```
  DROP TABLE <table_name>
  ```

- Temporarily disable all connections to table:

  ```
  select oid from pg_class where relname='<table_name>'
  ```

## Row

- Updating row:

  ```
  UPDATE <table_name> SET <column1>=<value>
  ```

- Create row in table:

  ```
  INSERT INTO <table_name> (column1, column2) VALUES (value1, value2)
  ```

- Create row in table base on other table rows:

  ```
  INSERT INTO <table_name> SELECT * FROM <other_table_name>
  ```

- Delete row in table:

  ```
  DELETE FROM <table_name> WHERE <column1>=<value>
  ```

## Column

- Create column in table: For creating new column need to temporarily disable all connections to table

  ```
  ALTER TABLE <table_name> ADD COLUMN <column_name> <data_type> [NOT NULL] [DEFAULT <value>]
  ```
  
- Show table column:

  ```
  select column_name, data_type from information_schema.columns where table_name='<table_name>'
  ```

- Make column nullable:

  ```
  ALTER TABLE <table_name> ALTER COLUMN <column_name> DROP NOT NULL
  ```

- Make column not nullable:

  ```
  ALTER TABLE <table_name> ALTER COLUMN <column_name> SET NOT NULL
  ```

- Update column value base other column:

  ```
  Update <table> SET <column1>=<column2>
  ```

## Index

- Partial index:

  ```
  CREATE [UNIQUE] INDEX <index_name> ON <table> (<column1, column2>) WHERE <conditions>
  ```

## Other

- Version:

  ```
  SHOW server_version
  ```

- Connection URL:

  ```
  postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]
  ```

  