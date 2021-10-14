from elasticsearch import Elasticsearch as ES 
import json
es=ES(['124.252.253.124:9200'])
res=es.cat.indices()
print(res)

