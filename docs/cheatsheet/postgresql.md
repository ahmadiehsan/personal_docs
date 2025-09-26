# Postgresql

## Data Types

=== "String"

    | Data Type     | Range                              | Storage Size              |
    | ------------- | ---------------------------------- | ------------------------- |
    | CHAR(size)    | Fixed length, 1 to 1,024 chars     | 1 to 1,024 bytes          |
    | VARCHAR(size) | Variable length, 1 to 65,535 chars | 1 to 65,535 bytes         |
    | TEXT          | Up to 1 GB of text                 | Up to 1 GB                |
    | BYTEA         | Up to 1 GB of binary data          | Up to 1 GB                |
    | ENUM          | Enumerated list of values          | Depends on values         |
    | ARRAY         | Array of any data type             | Depends on the array size |

=== "Numeric"

    | Data Type        | Range                                                    | Storage Size |
    | ---------------- | -------------------------------------------------------- | ------------ |
    | SMALLINT         | -32,768 to 32,767                                        | 2 bytes      |
    | INT, INTEGER     | -2,147,483,648 to 2,147,483,647                          | 4 bytes      |
    | BIGINT           | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807  | 8 bytes      |
    | NUMERIC(p, s)    | Depends on precision (p) and scale (s)                   | Varies       |
    | DECIMAL(p, s)    | Depends on precision (p) and scale (s)                   | Varies       |
    | REAL             | -3.4028235E+38 to 3.4028235E+38                          | 4 bytes      |
    | DOUBLE PRECISION | -1.7976931348623157E+308 to 1.7976931348623157E+308      | 8 bytes      |
    | SERIAL           | Auto-incrementing integer (equivalent to INTEGER)        | 4 bytes      |
    | BIGSERIAL        | Auto-incrementing large integer (equivalent to BIGINT)   | 8 bytes      |
    | SMALLSERIAL      | Auto-incrementing small integer (equivalent to SMALLINT) | 2 bytes      |

=== "Date and time"

    | Data Type   | Range                                                  | Storage Size |
    | ----------- | ------------------------------------------------------ | ------------ |
    | DATE        | 4713-01-01 (BC) to 5874897-12-31 (AD)                  | 4 bytes      |
    | TIMESTAMP   | 4713-01-01 00:00:00 (BC) to 294276-12-31 23:59:59 (AD) | 8 bytes      |
    | TIMESTAMPTZ | 4713-01-01 00:00:00 (BC) to 294276-12-31 23:59:59 (AD) | 8 bytes      |
    | TIME        | 00:00:00 to 24:00:00                                   | 8 bytes      |
    | INTERVAL    | Varies, up to 178000 years                             | 16 bytes     |

=== "Boolean"

    | Data Type | Range         | Storage Size |
    | --------- | ------------- | ------------ |
    | BOOLEAN   | TRUE or FALSE | 1 byte       |

=== "Full list"

    [Full Data Types](https://www.tutorialspoint.com/postgresql/postgresql_data_types.htm)

## Export/Import

=== "Import"

    ```shell
    psql -d <db_name> -f <file_name.sql>
    ```

=== "Export"

    ```shell
    pg_dump -U <db_user> <db_name> > <file_name>.sql
    ```

## Shell

=== "Connect"

    ```shell
    psql
    ```

=== "Run command by sudo"

    ```shell
    sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"
    ```

=== "Vertical show fields"

    ```text
    \x
    ```

## User

=== "Show all"

    ```text
    \du
    ```

=== "Create"

    ```sql
    CREATE USER <username>
    ```

=== "Drop"

    ```sql
    DROP USER <username>
    ```

=== "Change pass"

    ```sql
    ALTER USER <username> WITH PASSWORD '<new_password>'
    ```

## Database

=== "Show all"

    ```text
    \l
    ```

=== "Create"

    ```sql
    CREATE DATABASE <db_name>
    ```

=== "Drop"

    ```sql
    DROP DATABASE <db_name>
    ```

=== "Change owner"

    ```sql
    ALTER DATABASE <db_name> OWNER TO <username>
    ```

=== "Connect"

    ```text
    \c <db_name>
    ```

## Tables

=== "Show all"

    ```text
    \dt
    ```

=== "Show schema"

    ```text
    \d+ <table_name>
    ```

=== "Create"

    ```sql
    # Simple
    CREATE TABLE <table_name>

    # Based on other table
    CREATE TABLE <table_name> (LIKE <other_table_name> INCLUDING ALL);
    ```

=== "Delete"

    ```sql
    DROP TABLE <table_name>
    ```

## Row

=== "Update"

    ```sql
    UPDATE <table_name> SET <column1>=<value>
    ```

=== "Create"

    ```sql
    # Simple
    INSERT INTO <table_name> (column1, column2) VALUES (value1, value2)

    # Based on other table row
    INSERT INTO <table_name> SELECT * FROM <other_table_name>
    ```

=== "Delete"

    ```sql
    DELETE FROM <table_name> WHERE <column1>=<value>
    ```

## Column

=== "Create"

    ```sql
    # For creating new column need to temporarily disable all connections to table
    ALTER TABLE <table_name> ADD COLUMN <column_name> <data_type> [NOT NULL] [DEFAULT <value>]
    ```

=== "Show table column"

    ```sql
    SELECT column_name, data_type FROM information_schema.columns WHERE table_name='<table_name>'
    ```

=== "To nullable"

    ```sql
    ALTER TABLE <table_name> ALTER COLUMN <column_name> DROP NOT NULL
    ```

=== "To not nullable"

    ```sql
    ALTER TABLE <table_name> ALTER COLUMN <column_name> SET NOT NULL
    ```

## Index

=== "Partial index"

    ```sql
    CREATE [UNIQUE] INDEX <index_name> ON <table> (<column1, column2>) WHERE <conditions>
    ```

## Other

- Version:

  ```sql
  SHOW server_version
  ```

- Connection URL:

  ```text
  postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]
  ```
