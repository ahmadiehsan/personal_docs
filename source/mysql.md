# Mysql

## Links

- [MySQL Data Types](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

## Installation

Tip: installation flow needs an active VPN

```
sudo apt update
sudo apt install gnupg
cd /tmp
wget https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb
sudo dpkg -i mysql-apt-config*
sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation
```

## Export/Import

- import data to database:

  `mysql [-h <host>] -u <username: root> -p <db name> < <file_path/file_name.sql>`

- export data from database:

  `mysqldump [-h <host>] -u <username: root> -p [--no-data] [--set-gtid-purged=OFF] <db name> > <file_path/file_name.sql>`

## Connection

- connect to MySQL interactive shell: `mysql -u root -p`
- run command without connection: `mysql -u root -p <<< 'SHOW DATABASES;'`

## User

- show all users: `SELECT user, host FROM mysql.user`

- accepting all IPs: `UPDATE mysql.user SET host='<host: %>' WHERE user='<user: root>';`

- create user: `CREATE USER '<username>'@'localhost' IDENTIFIED BY '<password>'`

- drop user: ``

- change pass for any user: ``

- change pass of root user: `ALTER USER 'root'@'%' IDENTIFIED BY '<new password>';`

- add all privileges to user for one database:

  `GRANT ALL PRIVILEGES ON <db name>.* TO '<user>'@'localhost'`

## Database

- show all database: `SHOW DATABASES`

- create db: `CREATE DATABASE <db name>`

- drop database: `DROP DATABASE <db name>`

- show database owner: `SHOW processlist`

- change db owner: ``

- connect to database: `USE <db name>`

- get size of databases:

  `SELECT table_schema "<db name>", ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) "DB Size in MB" FROM information_schema.tables GROUP BY table_schema`

## Tables

- show all of db tables: `SHOW TABLES`
- show table schema: `DESCRIBE <tablename>`
- show table full schema: `SHOW FULL COLUMNS FROM <tablename>;`
- create table simple: `CREATE TABLE <tablename> (id INT NOT NULL AUTO_INCREMENT, <column2> <datatype>, PRIMARY KEY(id))`
- create table complex:

  ```
  CREATE TABLE <tablename> (
      id BINARY(16) PRIMARY KEY,  # UUID
      created DATETIME(6) NOT NULL,
      <column3> INT NOT NULL DEFAULT 0,
      <column4> BINARY(16) UNIQUE NOT NULL,  # FK (1:1)
  
      INDEX (<column3>),  # custom index
      FOREIGN KEY (<column4>) REFERENCES <othertable>(id)  # automatically will create an index
  );
  ```
- create table based on other table: ``
- delete table: `DROP TABLE <tablename>`
- show indexes: `SHOW INDEXES IN <tablename>`

## Row

- updating row: `UPDATE <table name> SET <column A>=<value>`

- create row in table:

  `INSERT INTO <table name> (column A, column B) VALUES (value a, value b)`

- create row in table base on other table rows: ``

- delete row in table:

  `DELETE FROM <table name> WHERE <column A>=<value>`

## Partial Index

`CREATE [UNIQUE] INDEX <index name> ON <table> (<column A, column B>) WHERE <conditions>`

## Vertical Show Fields

`SELECT * FROM <table_name>\G`

## MySQL Version

`SHOW VARIABLES LIKE "%version%";`

