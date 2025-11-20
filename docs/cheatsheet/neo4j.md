# Neo4j

## Shell

=== "Connect"

    ```shell
    cypher-shell -u <username: neo4j> -p <password> [-d <database_name>]
    ```

=== "Exit"

    ```shell
    :exit
    ```

## Database

=== "List"

    ```cypher
    SHOW DATABASES
    ```

=== "Create"

    ```cypher
    CREATE DATABASE <database_name>
    ```

=== "Drop"

    ```cypher
    DROP DATABASE <database_name>
    ```

=== "Switch"

    ```shell
    :use <database_name>
    ```

## Node

=== "Create (simple)"

    ```cypher
    CREATE (n:<Node: Book>)
    RETURN n
    ```

=== "Create (with properties)"

    ```cypher
    CREATE (n:<Node> {<property1> <value1>, <property2> <value2>})
    RETURN n
    ```

=== "Create (multiple)"

    ```cypher
    CREATE
        (a:<Node1> {<property>: <value>}),
        (b:<Node2> {<property>: <value>})
    RETURN a, b
    ```

=== "Update"

    ```cypher
    MATCH (n:<Node>)
    WHERE n.<property> = <value>
    SET n.<property> = <new_value>
    RETURN n
    ```

=== "Delete"

    ```cypher
    MATCH (n:<Node>)
    WHERE n.<property> = <value>
    DELETE n
    ```

=== "Query"

    ```cypher
    MATCH (n:<Node>)
    WHERE n.<property> = <value>
    RETURN n
    LIMIT <limit: 10>
    ```

## Relationship

=== "Create (simple)"

    ```cypher
    MATCH (a:<Node1>), (b:<Node2>)
    CREATE (a)-[r:<REL_TYPE>]->(b)
    RETURN r
    ```

=== "Create (with properties)"

    ```cypher
    MATCH (a:<Node1> {<property>: <value>}), (b:<Node2> {<property>: <value>})
    CREATE (a)-[r:<REL_TYPE> {<property>: <value>}]->(b)
    RETURN r
    ```

=== "Update"

    ```cypher
    MATCH (a:<Node1>)-[r:<REL_TYPE>]->(b:<Node2>)
    SET r.<property> = <new_value>
    RETURN r
    ```

=== "Delete"

    ```cypher
    MATCH (a:<Node1>)-[r:<REL_TYPE>]->(b:<Node2>)
    DELETE r
    ```

=== "Query (1 length path)"

    ```cypher
    MATCH (a:<Node1>)-[r:<REL_TYPE> {property: <value>}]->(b:<Node2>)
    RETURN a, r, b
    ```

=== "Query (variable length path)"

    ```cypher
    # Matches paths of length 1 to 3
    MATCH (a:<Node1>)-[r:<REL_TYPE>*1..3]->(b:<Node2>)
    RETURN a, b
    ```

=== "Query (any length path)"

    ```cypher
    # Matches any length
    MATCH (a:<Node1>)-[r:<REL_TYPE>*]->(b:<Node2>)
    RETURN a, b
    ```

=== "Query (shortest path)"

    ```cypher
    MATCH (a:<Node1>), (b:<Node2>)
    WHERE a.name = <value> AND b.name = <value>
    MATCH path = shortestPath((a)-[*]->(b))
    RETURN path
    ```

=== "Query (all shortest paths)"

    ```cypher
    MATCH (a:<Node1>), (b:<Node2>)
    WHERE a.name = <value> AND b.name = <value>
    MATCH path = allShortestPaths((a)-[*]->(b))
    RETURN path
    ```

## Constraints

=== "List"

    ```cypher
    SHOW CONSTRAINTS
    ```

=== "Create (unique)"

    ```cypher
    CREATE CONSTRAINT <constraint_name> FOR (n:<Node>) REQUIRE n.<property> IS UNIQUE
    ```

=== "Create (key)"

    ```cypher
    CREATE CONSTRAINT <constraint_name> FOR (n:<Node>) REQUIRE n.<property> IS NODE KEY
    ```

=== "Create (existence)"

    ```cypher
    CREATE CONSTRAINT <constraint_name> FOR (n:<Node>) REQUIRE n.<property> IS NOT NULL
    ```

=== "Drop"

    ```cypher
    DROP CONSTRAINT <constraint_name>
    ```

## Index

=== "List"

    ```cypher
    SHOW INDEXES
    ```

=== "Create (simple)"

    ```cypher
    CREATE INDEX <index_name> FOR (n:<Node>) ON (n.<property>)
    ```

=== "Create (composite)"

    ```cypher
    CREATE INDEX <index_name> FOR (n:<Node>) ON (n.<property1>, n.<property2>)
    ```

=== "Drop"

    ```cypher
    DROP INDEX <index_name>
    ```

## Operations

=== "And"

    ```cypher
    MATCH (n:<Node>)
    WHERE n.<property1> = <value1> AND n.<property2> > <value2>
    RETURN n
    ```

=== "In"

    ```cypher
    MATCH (n:<Node>)
    WHERE n.<property> IN [<value1>, <value2>, <value3>]
    RETURN n
    ```

=== "Starts with"

    ```cypher
    MATCH (n:<Node>)
    WHERE n.<property> STARTS WITH "<prefix>"
    RETURN n
    ```

=== "Contains"

    ```cypher
    MATCH (n:<Node>)
    WHERE n.<property> CONTAINS "<substring>"
    RETURN n
    ```

=== "Exists"

    ```cypher
    MATCH (n:<Node>)
    WHERE EXISTS(n.<property>)
    RETURN n
    ```

=== "Count"

    ```cypher
    MATCH (n:<Node>)
    RETURN COUNT(n) AS count
    ```

=== "Order and limit"

    ```cypher
    MATCH (n:<Node>)
    RETURN n
    ORDER BY n.<property> <ASC or DESC>
    LIMIT <limit: 10>
    ```

=== "Aggregate"

    ```cypher
    MATCH (n:<Node>)
    RETURN n.<property>, COUNT(*), AVG(n.<property>), MAX(n.<property>), MIN(n.<property>)
    ```

=== "Distinct"

    ```cypher
    MATCH (n:<Node>)
    RETURN DISTINCT n.<property>
    ```

=== "Group by"

    ```cypher
    MATCH (n:<Node>)
    RETURN n.<property>, COUNT(*) AS count
    ```
