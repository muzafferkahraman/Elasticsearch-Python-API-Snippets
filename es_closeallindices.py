from elasticsearch import Elasticsearch as ES 
import json
es=ES(['124.252.253.124:9200'])
for res in es.indices.get('*'):
  es.indices.close(index=res)






