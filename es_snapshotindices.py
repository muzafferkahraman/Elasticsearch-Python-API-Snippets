from elasticsearch import Elasticsearch as ES 
es=ES(['124.252.253.124:9200'])
body={
  "indices": "nuage_acl-2021-02-21,nuage_dpi_flowstats-2021-02-21",
  "metadata": {
    "taken_by": "muzo",
    "taken_because": "test"
  }
}
es.snapshot.create(repository='backup', snapshot='muzo2', body=body)

