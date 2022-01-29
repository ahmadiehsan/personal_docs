# Elasticsearch

## simple query

```bash
curl -X GET "http://localhost:9200/_search?pretty"
```

## remove all data

```bash
curl -X DELETE "http://localhost:9200/*"
```

## create index and type

```bash
curl -X PUT "http://localhost:9200/<IndexName>/<TypeName>"
```

## clustering

![](_static/images/elasticsearch/elasticsearch_cluster.jpg)

## Elasticsearch DSL and Django ORM

![](_static/images/elasticsearch/django_orm_map_to_elasticsearch_dsl.jpg)