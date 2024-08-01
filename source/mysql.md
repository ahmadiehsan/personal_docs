# Mysql

## Links

- [MySQL Data Types](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

## Install

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

- Import data to database:

  ```
  mysql [-h <host>] -u <username: root> -p <db_name> < <file_path/file_name.sql>
  ```

- Export data from database:

  ```
  mysqldump [-h <host>] -u <username: root> -p [--no-data] [--set-gtid-purged=OFF] <db_name> > <file_path/file_name.sql>
  ```

## Shell

- Connect:

  ```
  mysql -u root -p
  ```

- Run command without connection:

  ```
  mysql -u root -p <<< 'SHOW DATABASES;'
  ```

- Vertical show fields:

  ```
  SELECT * FROM <table_name>\G
  ```

## User

- Show all users:

  ```
  SELECT user, host FROM mysql.user
  ```

- Accepting all IPs:

  ```
  UPDATE mysql.user SET host='<host: %>' WHERE user='<user: root>'
  ```

- Create user:

  ```
  CREATE USER '<username>'@'localhost' IDENTIFIED BY '<password>'
  ```

- Drop user:

  ```
  
  ```

- Change pass for any user:

  ```
  
  ```

- Change pass of root user:

  ```
  ALTER USER 'root'@'%' IDENTIFIED BY '<new_password>'
  ```

- Add all privileges to user for one database:

  ```
  GRANT ALL PRIVILEGES ON <db_name>.* TO '<user>'@'localhost'
  ```

## Database

- Show all database:

  ```
  SHOW DATABASES
  ```

- Create db:

  ```
  CREATE DATABASE <db_name>
  ```

- Drop database:

  ```
  DROP DATABASE <db_name>
  ```

- Show database owner:

  ```
  SHOW processlist
  ```

- Change db owner:

  ```
  
  ```

- Connect to database:

  ```
  USE <db_name>
  ```

- Get size of databases:

  ```
  SELECT table_schema "<db_name>", ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) "DB Size in MB" FROM information_schema.tables GROUP BY table_schema
  ```

## Tables

- Show all of db tables:

  ```
  SHOW TABLES
  ```
- Show table schema:

  ```
  DESCRIBE <table_name>
  ```
- Show table full schema:

  ```
  SHOW FULL COLUMNS FROM <table_name>
  ```
- Create table simple:

  ```
  CREATE TABLE <table_name> (id INT NOT NULL AUTO_INCREMENT, <column2> <datatype>, PRIMARY KEY(id))
  ```
- Create table complex:

  ```
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

  ```
  
  ```
- Delete table:

  ```
  DROP TABLE <table_name>
  ```
- Show indexes:

  ```
  SHOW INDEXES IN <table_name>
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
  
  ```

- Delete row in table:

  ```
  DELETE FROM <table_name> WHERE <column1>=<value>
  ```

## Index

- Partial index:

  ```
  CREATE [UNIQUE] INDEX <index_name> ON <table> (<column1, column2>) WHERE <conditions>
  ```

## Other

- Version:

  ```
  SHOW VARIABLES LIKE "%version%";
  ```

