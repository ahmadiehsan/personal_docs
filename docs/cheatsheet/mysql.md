# Mysql

## Links

- [MySQL Data Types](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

## Install

!!! info

    Installation flow needs an active VPN

```shell
sudo apt update
sudo apt install gnupg
cd /tmp
wget https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb
sudo dpkg -i mysql-apt-config*
sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation
```

## Data Types

- String:

  | Data Type     | Range                              | Storage size              |
  | ------------- | ---------------------------------- | ------------------------- |
  | CHAR(size)    | Fixed length, 0 to 255 chars       | 1 to 255 bytes            |
  | VARCHAR(size) | Variable length, 0 to 65,535 chars | 1 to 65,535 bytes         |
  | TEXT          | Up to 65,535 chars                 | Up to 65,535 bytes        |
  | MEDIUMTEXT    | Up to 16,777,215 chars             | Up to 16,777,215 bytes    |
  | LONGTEXT      | Up to 4,294,967,295 chars          | Up to 4,294,967,295 bytes |
  | TINYBLOB      | Up to 255 bytes                    | Up to 255 bytes           |
  | BLOB          | Up to 65,535 bytes                 | Up to 65,535 bytes        |
  | MEDIUMBLOB    | Up to 16,777,215 bytes             | Up to 16,777,215 bytes    |
  | LONGBLOB      | Up to 4,294,967,295 bytes          | Up to 4,294,967,295 bytes |
  | ENUM          | Enumerated list of values          | Depends on values         |
  | SET           | Set of values                      | Depends on values         |

- Numeric:

  | Data Type                      | Range (signed) (Default)                                | Range (unsigned)                   | Storage size |
  | ------------------------------ | ------------------------------------------------------- | ---------------------------------- | ------------ |
  | TINYINT(size)                  | -128 to 127                                             | 0 to 255                           | 1 byte       |
  | SMALLINT(size)                 | -32,768 to 32,767                                       | 0 to 65,535                        | 2 bytes      |
  | MEDIUMINT(size)                | -8,388,608 to 8,388,607                                 | 0 to 16,777,215                    | 3 bytes      |
  | INT(size), INTEGER(size)       | -2,147,483,648 to 2,147,483,647                         | 0 to 4,294,967,295                 | 4 bytes      |
  | BIGINT(size)                   | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 | 0 to 18,446,744,073,709,551,615    | 8 bytes      |
  | FLOAT(size, d)                 | -3.402823466E+38 to 3.402823466E+38                     | Not applicable                     | 4 bytes      |
  | DOUBLE(size, d)                | -1.7976931348623157E+308 to 1.7976931348623157E+308     | Not applicable                     | 8 bytes      |
  | DECIMAL(size, d), DEC(size, d) | Depends on the precision and scale                      | Depends on the precision and scale | Varies       |
  | BIT(size)                      | Not applicable                                          | 1 to 64                            | Varies       |

- Date and time:

  | Data Type      | Range                                              | Storage size |
  | -------------- | -------------------------------------------------- | ------------ |
  | DATE           | 1000-01-01 to 9999-12-31                           | 3 bytes      |
  | DATETIME(fsp)  | 1000-01-01 00:00:00 to 9999-12-31 23:59:59         | 8 bytes      |
  | TIMESTAMP(fsp) | 1970-01-01 00:00:01 UTC to 2038-01-19 03:14:07 UTC | 4 bytes      |
  | TIME(fsp)      | -838:59:59 to 838:59:59                            | 3 bytes      |
  | YEAR           | 1901 to 2155                                       | 1 byte       |

- Boolean:

  | Data Type     | Range  | Storage size |
  | ------------- | ------ | ------------ |
  | BOOL, BOOLEAN | 0 or 1 | 1 byte       |

## Export/Import

- Import data to database:

  ```shell
  mysql [-h <host>] -u <username: root> -p <db_name> < <file_path/file_name.sql>
  ```

- Export data from database:

  ```shell
  mysqldump [-h <host>] -u <username: root> -p [--no-data] [--set-gtid-purged=OFF] <db_name> > <file_path/file_name.sql>
  ```

## Shell

- Connect:

  ```shell
  mysql -u root -p
  ```

- Run command without connection:

  ```shell
  mysql -u root -p <<< 'SHOW DATABASES;'
  ```

- Vertical show fields:

  ```sql
  SELECT * FROM <table_name>\G
  ```

## User

- Show all users:

  ```sql
  SELECT user, host FROM mysql.user
  ```

- Accepting all IPs:

  ```sql
  UPDATE mysql.user SET host='<host: %>' WHERE user='<user: root>'
  ```

- Create user:

  ```sql
  CREATE USER '<username>'@'localhost' IDENTIFIED BY '<password>'
  ```

- Drop user:

  ```sql

  ```

- Change pass for any user:

  ```sql

  ```

- Change pass of root user:

  ```sql
  ALTER USER 'root'@'%' IDENTIFIED BY '<new_password>'
  ```

- Add all privileges to user for one database:

  ```sql
  GRANT ALL PRIVILEGES ON <db_name>.* TO '<user>'@'localhost'
  ```

## Database

- Show all database:

  ```sql
  SHOW DATABASES
  ```

- Create db:

  ```sql
  CREATE DATABASE <db_name>
  ```

- Drop database:

  ```sql
  DROP DATABASE <db_name>
  ```

- Show database owner:

  ```sql
  SHOW processlist
  ```

- Change db owner:

  ```sql

  ```

- Connect to database:

  ```sql
  USE <db_name>
  ```

- Get size of databases:

  ```sql
  SELECT table_schema "<db_name>", ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) "DB Size in MB" FROM information_schema.tables GROUP BY table_schema
  ```

## Tables

- Show all of db tables:

  ```sql
  SHOW TABLES
  ```

- Show table schema:

  ```sql
  DESCRIBE <table_name>
  ```

- Show table full schema:

  ```sql
  SHOW FULL COLUMNS FROM <table_name>
  ```

- Create table simple:

  ```sql
  CREATE TABLE <table_name> (id INT NOT NULL AUTO_INCREMENT, <column2> <datatype>, PRIMARY KEY(id))
  ```

- Create table complex:

  ```sql
  CREATE TABLE <table_name> (
      id BINARY(16) PRIMARY KEY,  # UUID
      created DATETIME(6) NOT NULL,
      <column3> INT NOT NULL DEFAULT 0,
      <column4> BINARY(16) UNIQUE NOT NULL,  # FK (1:1)

      INDEX (<column3>),  # custom index
      FOREIGN KEY (<column4>) REFERENCES <other_table>(id)  # automatically will create an index
  );
  ```

- Create table based on other table:

  ```sql

  ```

- Delete table:

  ```sql
  DROP TABLE <table_name>
  ```

- Show indexes:

  ```sql
  SHOW INDEXES IN <table_name>
  ```

## Row

- Updating row:

  ```sql
  UPDATE <table_name> SET <column1>=<value>
  ```

- Create row in table:

  ```sql
  INSERT INTO <table_name> (column1, column2) VALUES (value1, value2)
  ```

- Create row in table base on other table rows:

  ```sql

  ```

- Delete row in table:

  ```sql
  DELETE FROM <table_name> WHERE <column1>=<value>
  ```

## Index

- Partial index:

  ```sql
  CREATE [UNIQUE] INDEX <index_name> ON <table> (<column1, column2>) WHERE <conditions>
  ```

## Other

- Version:

  ```sql
  SHOW VARIABLES LIKE "%version%";
  ```
