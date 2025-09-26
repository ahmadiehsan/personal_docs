# MongoDB

## Shell

=== "Connect"

    ```shell
    mongo <db_name> -u <user> -p <pass>
    ```

## Database

=== "List"

    ```shell
    # Quick
    show databases

    # Normal
    db.adminCommand({listDatabases: 1})
    ```

## Collection

=== "List"

    ```shell
    # Quick
    show collections

    # Normal
    db.runCommand({listCollections: 1})
    ```

## Document

=== "Simple query"

    ```shell
    db.<collection_name>.find().pretty()  # find() or findOne()
    db.<collection_name>.find({<query_field>: "<value>"})
    ```

=== "Complex query"

    ```shell
    db.<collection_name>.find(
      {"<query_field>.<child_query_field>": "<value>"},
      {<include_field>: 1, <exclude_field>: 0}
    ).pretty()
    ```
