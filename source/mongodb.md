# MongoDB

## Shell

- connect: `mongo <db_name> -u <user> -p <pass>`

## Database

- list (quick): `show databases`
- list: `db.adminCommand({listDatabases: 1})`

## Collection

- list (quick): `show collections`
- list: `db.runCommand({listCollections: 1})`

## Document

### Simple Query

```
db.<collection_name>.find().pretty()  # find() or findOne()
db.<collection_name>.find({<query_field>: "<value>"})
```

### Complex Query

```
db.<collection_name>.find(
	{"<query_field>.<child_query_field>": "<value>"},
	{<include_field>: 1, <exclude_field>: 0}
).pretty()
```

