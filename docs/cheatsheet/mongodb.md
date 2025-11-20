# MongoDB

## Shell

=== "Connect"

    ```shell
    mongosh
    ```

## Database

=== "List"

    ```shell
    show databases
    ```

=== "Connect"

    ```shell
    use <db_name>
    ```

=== "Drop"

    ```shell
    # Drops the current database
    db.dropDatabase()
    ```

## Collection

=== "List"

    ```shell
    show collections
    ```

=== "Create (simple)"

    ```shell
    db.createCollection("<collection_name>")
    ```

=== "Create (advance)"

    ```shell
    db.createCollection("<collection_name>", {capped: true, size: 10000000, max: 100, autoIndexId: false})
    ```

=== "Drop"

    ```shell
    db.<collection_name>.drop()
    ```

## Document

=== "Query (simple)"

    ```shell
    # or findOne()
    db.<collection_name>.find().pretty()
    db.<collection_name>.find({<query_field>: <value>}).sort({<sort_field>: 1}).limit(<limit_size: 3>)
    ```

=== "Query (complex)"

    ```shell
    db.<collection_name>.find(
        {"<query_field>.<child_query_field>": <value>},
        {<include_field>: 1, <exclude_field>: 0}
    ).pretty()
    ```

=== "Insert (one)"

    ```shell
    db.<collection_name>.insertOne({<field1: name>: <value1: "Patrick">, <field2: age>: <value2: 30>})
    ```

=== "Insert (many)"

    ```shell
    db.<collection_name>.insertMany([
        {<field1: name>: <value1: "Patrick">, <field2: age>: <value2: 30>},
        {<field1: name>: <value1: "Sandy">, <field2: age>: <value2: 27>},
    ])
    ```

=== "Insert (complex)"

    ```shell
    db.<collection_name>.insertOne(
        {
            name: "Larry",
            age: 32,
            GPA: 2.8,
            "full time": false,
            "register date": new Date(),
            "graduation date": null,
            courses: ["biology", "chemistry", "calculus"],
            address: {
                street: "one two three fake street",
                city: "Bikini Bottom",
                "zip code": "one two three four five"
            }
        }
    )
    ```

=== "Update"

    ```shell
    # or updateMany
    db.<collection_name>.updateOne({<query_field>: <value>}, {$set: {<update_field>: <value>}})
    ```

=== "Delete"

    ```shell
    # or deleteMany
    db.<collection_name>.deleteOne({<query_field>: <value>})
    ```

## Operators

=== "!="

    ```shell
    db.<collection_name>.find({<query_field>: {$ne: <value>}})
    ```

=== "<"

    ```shell
    db.<collection_name>.find({<query_field>: {$lt: <value>}})
    ```

=== "<="

    ```shell
    db.<collection_name>.find({<query_field>: {$lte: <value>}})
    ```

=== ">"

    ```shell
    db.<collection_name>.find({<query_field>: {$gt: <value>}})
    ```

=== ">="

    ```shell
    db.<collection_name>.find({<query_field>: {$gte: <value>}})
    ```

=== "Between"

    ```shell
    db.<collection_name>.find({<query_field>: {$gte: <value: 3>, $lte: <value: 4>}})
    ```

=== "In"

    ```shell
    db.<collection_name>.find({<query_field>: {$in: [<value1>, <value2>, <value3>] } })
    ```

=== "Not in"

    ```shell
    db.<collection_name>.find({<query_field>: {$nin: [<value1>, <value2>, <value3>] } })
    ```

=== "&"

    ```shell
    db.<collection_name>.find({$and: [{<query_field1>: <value1>}, {<query_field2>: <value2>}]})
    ```

=== "|"

    ```shell
    db.<collection_name>.find({$or: [{<query_field1>: <value1>}, {<query_field2>: <value2>}]})
    ```

=== "neither"

    ```shell
    db.<collection_name>.find({$nor: [{<query_field1>: <value1>}, {<query_field2>: <value2>}]})
    ```

## Index

=== "List"

    ```shell
    db.<collection_name>.getIndexes()
    ```

=== "Create"

    ```shell
    db.<collection_name>.createIndex({<field>: 1})
    ```

=== "Drop"

    ```shell
    db.<collection_name>.dropIndex("<index_name>")
    ```

=== "Execution statistics"

    ```shell
    db.<collection_name>.find({<query_field>: <value>}).explain("executionStats")
    ```
