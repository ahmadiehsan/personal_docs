# Elasticsearch

## Document

### query simple

```bash
curl -X GET "http://localhost:9200/_search?pretty" -u <username_and_password: elastic:pass123>
```

### query complex

```bash
curl -X GET "http://localhost:9200/<index_name>/<_search or _count>?pretty" -H 'Content-Type: application/json' -d '{
  "query": {
    "bool": {
      "must": {
        "match": {"<field>": "<value>"}
      }
    }
  }
}'
```

### create

```bash
curl -X POST "http://localhost:9200/<index_name>/_doc?pretty" -H 'Content-Type: application/json' -d '{
  "<field>": "<value>"
}'
```

### update

```bash
# fully replace
curl -X PUT "http://localhost:9200/<index_name>/_doc/<_id>?pretty" -H 'Content-Type: application/json' -d '{
  "<field>": "<value>"
}'
```

### get

```bash
# return document and its related data
curl -X GET "http://localhost:9200/<index_name>/_doc/<_id>?pretty"
```

```bash
# return document only
curl -X GET "http://localhost:9200/<index_name>/_source/<_id>?pretty"
```

### delete

```bash
curl -X DELETE "http://localhost:9200/<index_name>/_doc/<_id>?pretty"
```

## Index

### get all

```bash
curl -X GET "http://localhost:9200/_aliases?pretty"
```

### create simple

```bash
curl -X PUT "http://localhost:9200/<index_name>?pretty"
```

### create with mapping

```bash
curl -X PUT "http://localhost:9200/<index_name>?pretty" -H 'Content-Type: application/json' -d '{
  "mappings": {
    "dynamic": "<dynamic_type: strict>",
    "properties": {
      "<field>": {
        "type": "<data_type>"
      }
    }
  }
}'
```

### delete

```bash
curl -X DELETE "http://localhost:9200/<index_name>?pretty"
```

```bash
curl -X DELETE "http://localhost:9200/<index1>,<index2>,<index3>?pretty"
```

```bash
# action.destructive_requires_name=false
curl -X DELETE "http://localhost:9200/*?pretty"
```

## Mapping

### get current

```bash
curl -X GET "http://localhost:9200/<index_name>/_mapping?pretty"
```

### create or update

```bash
curl -X PUT "http://localhost:9200/<index_name>/_mapping?pretty" -H 'Content-Type: application/json' -d '{
  "dynamic": "<dynamic_type: strict>",
  "properties": {
    "<field>": {
      "type": "<data_type>"
    }
  }
}'
```

### delete

There is no way to delete a field from mapping. Even if you delete all documents that contain this field

## clustering

![](_static/images/elasticsearch/elasticsearch_cluster.jpg)

## Elasticsearch DSL and Django ORM

![](_static/images/elasticsearch/django_orm_map_to_elasticsearch_dsl.jpg)